import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ia_selenium import ia_login, ia_investment, ia_transactions, ia_client
from dbutilities import db_method

from selenium.webdriver.support import expected_conditions as EC
from dbutilities import connection
from ia_selenium import ia_selectors
from utilities.web_driver import driver_setup


def ia_app(wd, confs, thread_name="Main", recursive=0):
    """
    Getting website, and logging in .

    :param wd: represents webdriver
    :param confs: dictionary generated at the start of app
    :param thread_name: Name of the thread (default is "Main").
    :param recursive:Indicates the number of recursive attempts (default is 0).
    :return:

    Flow:
    1.Navigates to the specified web URL using the webdriver.
    2.It checks if the login button is present on the page. If not, it means the user is already logged in.
    3.If the login button is present, the function calls the ia_login function to perform the login process
    4.After logging in, the function waits for the cookie consent button to be clickable and clicks it to accept the cookies.
    5.If an exception occurs during the login process, the function will recursively try again up to 5 times.
      If it still fails, the webdriver is closed and a new one is set up before retrying.
    """

    # get the url and login
    parameters = confs['parameters']
    try:
        paths = ia_selectors.scrape_paths()
        wd.get(parameters['web_url'])
        if len(wd.find_elements(By.XPATH, paths['myclient_button'])) == 0:
            ia_login.login(wd, parameters['username'], parameters['password'], thread_name)
        # accept cookie
        time.sleep(2)
        if len(wd.find_elements(By.CSS_SELECTOR, paths['cookie_consent'])) > 0:
            wait = WebDriverWait(wd, 10)  # seconds want to wait
            wait.until(
                EC.element_to_be_clickable((By.XPATH, paths['cookie_button']))
            ).click()
    except Exception as e:
        # print(e)
        # print(traceback.format_exc())
        print(f"{thread_name}: Exception during login to IA, Will Try Again")
        if recursive < 5:
            ia_app(wd, confs, thread_name, recursive=(recursive + 1))
        else:
            wd.close()
            wd = driver_setup(confs)
            ia_app(wd, confs, thread_name)


def save_csv_to_db(control_unit, files, tables, company):
    """
    This method saves data from CSV files into a database. It performs various operations based on
    the control_unit parameter to determine which tables to update or delete.

    :param control_unit: an integer representing the control unit for determining which tables to update or delete
    :param files: a dictionary containing file paths for different CSV files.
    :param tables: a dictionary containing table names for different data types.
    :param company: a string representing the company name.
    :return: Nothing return. Tables in database are updated.

    Workflow:
    1.Connect to the database using the connection module.
    2.If the connection is successful, set the batch_size (1000) for batch processing.
    3.Save recover data into the database using the db_method.save_recover function.
    4.Save contract history data into the database using the db_method.save_data_into_db function.
    5.Delete the current contract data for the specified company.
    6.If the control mode is 1, delete the current fund and saving data for the company.
    7.Save saving and fund history data into the database.
    8.If the control mode is 2, delete the current transaction data for the company.
    9.Save transaction history data into the database.
    10.If the control mode is 4, delete the current participant, beneficiary, and client data for the company.
    11.Save client, participant, and beneficiary history data into the database.
    12.Save current tables accordingly based on the control unit.
    13.Close the database cursor.
    """
    # change file read to file paths
    try:
        cursor = connection.connect_db().cursor()
    except Exception as e:
        print(e)
        print("Database connection failed!")
    else:
        print("Database connection successful!")
        batch_size = 1000
        db_method.save_recover(cursor,
                               zip(tables['recover'], [None] * len(tables['recover']),
                                   [company] * len(tables['recover'])))
        db_method.save_data_into_db(cursor, files['contracts'], db_method.save_contract_history, batch_size)
        db_method.delete_current_contract(cursor, company)

        if control_unit & 1:
            # delete current table of fund & saving for later insertion
            db_method.delete_current_fund_saving(cursor, company)

            # save saving & fund history
            db_method.save_data_into_db(cursor, files['saving'], db_method.save_saving_history, batch_size)
            db_method.save_data_into_db(cursor, files['fund'], db_method.save_fund_history, batch_size)
        if control_unit & 2:
            # delete current table of transaction for later insertion
            db_method.delete_current_transaction(cursor, company)

            # save transaction history
            db_method.save_data_into_db(cursor, files['transaction'], db_method.save_transaction_history, batch_size)
        if control_unit & 4:
            # delete current client information related tables for later insertion
            # if there is no new contracts
            # otherwise just extend the table
            # if not new_contracts:
            db_method.delete_current_participant_beneficiary(cursor, company)
            db_method.delete_current_client(cursor, company)
            db_method.save_data_into_db(cursor, files['client'], db_method.save_client_history, batch_size)
            db_method.save_data_into_db(cursor, files['participant'], db_method.save_participant_history, batch_size)
            db_method.save_data_into_db(cursor, files['beneficiary'], db_method.save_beneficiary_history, batch_size)

        # save current tables accordingly
        if control_unit & 4:
            db_method.save_data_into_db(cursor, files['client'], db_method.save_client, batch_size)
            db_method.save_data_into_db(cursor, files['participant'], db_method.save_participant, batch_size)
            db_method.save_data_into_db(cursor, files['beneficiary'], db_method.save_beneficiary, batch_size)
        if control_unit & 1:
            db_method.save_data_into_db(cursor, files['saving'], db_method.save_saving, batch_size)
            db_method.save_data_into_db(cursor, files['fund'], db_method.save_fund, batch_size)
        if control_unit & 2:
            db_method.save_data_into_db(cursor, files['transaction'], db_method.save_transaction, batch_size)
        db_method.save_data_into_db(cursor, files['contracts'], db_method.save_contract, batch_size)

        cursor.close()

    print(f"{datetime.now()}: Saving to Databases")
    print("=========================")


## fetch contracts_current table from SQL Server to compare with newly downloaded contract excel file.
def check_new_clients(tables):
    """
    This method  checks for new clients in a database table. It connects to the database,
    retrieves the list of existing clients, and compares it with a list of contract numbers
    from a CSV file. It then identifies the new clients by finding the contract numbers that
    are not present in the database. The function returns a list of the contract numbers of the new clients.
    :param tables: A dictionary containing the tables used in the function. It should have a key 'contracts'
                   with a value of a pandas DataFrame representing the CSV data.
    :return: list of the contract numbers of the new clients.

    Workflow:
    1.Attempt to establish a connection to the database.
    2.If the connection is successful, print a success message and proceed.
    3.Retrieve the list of existing clients from the database.
    4.Extract the contract numbers from the retrieved data and store them in the clients list.
    5.Remove duplicate rows based on the 'Contract_number' column from the 'contracts'.
    6.Create a new DataFrame new_client_df containing only the rows with contract numbers that are not present
      in the clients list.
    7.Store the contract numbers of the new clients in the tables dictionary under the key 'new_contracts'.
    8.Close the database cursor.
    """
    try:
        cursor = connection.connect_db().cursor()
    except Exception as e:
        print(e)
        print(f"{datetime.now()}: Database connection failed!")
    else:
        print(f"{datetime.now()}: Database connection successful!")

        # Query & saving the SQL table into a pd dataframe.
        # conn = connection.connect_db()
        db_method.read_clients(cursor)
        clients = [client[-2] for client in cursor.fetchall()]

        # keeping only the unique contract number row.
        csv_contract_unique_df = tables['contracts'].drop_duplicates(subset=['Contract_number'], keep='first')
        # creating new dataframe with only the new client and getting the list of contract number.
        new_client_df = csv_contract_unique_df[
            ~csv_contract_unique_df['Contract_number'].isin(clients)]
        tables['new_contracts'] = new_client_df['Contract_number'].tolist()
        # print('new_client_df')
        # print(tables['new_contracts'])

        cursor.close()


def scrape_cleanup(tables):
    """
    removes rows from the 'contracts' table on the 'Contract_number' column that are present in the 'recover' table.
    :param tables: a dictionary containing the 'contracts' and 'recover' tables
    :return: None, updated the 'contracts' table.
    """
    tables['contracts'] = tables['contracts'][~tables['contracts']['Contract_number'].isin(tables['recover'])]


def ia_loop_actions(wd, paths, confs, contract_number, tables, start_date):
    """
    This method performs a series of actions using the Selenium WebDriver. It takes in various inputs such
    as the WebDriver object, paths to different elements on the webpage, configurations, contract number,
    tables, and start date. Based on the configurations, it performs different actions like scraping investment
    data, scraping transaction data, and scraping client data.

    :param wd: The Selenium WebDriver object.
    :param paths: A dictionary containing XPaths to different elements on the webpage.
    :param confs: A dictionary containing configurations.
    :param contract_number: The contract number.
    :param tables: A dictionary containing tables to store scraped data.
    :param start_date: The start date for scraping transaction data.
    :return: Nothing return. database tables updated.
    """
    wd.find_element(By.XPATH, paths['myclient_button']).click()

    wd.find_element(By.XPATH, paths['contract_number_input']).clear()

    wd.find_element(By.XPATH, paths['contract_number_input']).send_keys(contract_number)

    wd.find_element(By.XPATH, paths['search_button']).click()

    if confs['control_unit'] & 1:
        ia_investment.scrape_investment(wd, tables['fund'], tables['saving'])
    if confs['control_unit'] & 2:
        ia_transactions.scrape_transaction(wd, tables['transaction'], start_date)
    if confs['control_unit'] & 4:
        ia_client.scrape(wd, tables['client'], tables['beneficiary'], tables['participant'],
                         contract_number)
