from datetime import datetime

from dbutilities import connection, db_method
from utilities.companys import companies


def save_csv_to_db(confs, files, tables, company):
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
        if confs['delete_flag']:
            db_method.delete_current_contract(cursor, company)
        control_unit = confs['control_unit']
        if control_unit & 1:
            # delete current table of fund & saving for later insertion
            if confs['delete_flag']:
                db_method.delete_current_fund_saving(cursor, company)

            # save saving & fund history
            if company == companies['iA']:
                db_method.save_data_into_db(cursor, files['saving'], db_method.save_saving_history, batch_size)
            db_method.save_data_into_db(cursor, files['fund'], db_method.save_fund_history, batch_size)
        if control_unit & 2:
            # delete current table of transaction for later insertion
            if confs['delete_flag']:
                db_method.delete_current_transaction(cursor, company)

            # save transaction history
            db_method.save_data_into_db(cursor, files['transaction'], db_method.save_transaction_history, batch_size)
        if control_unit & 4:
            # delete current client information related tables for later insertion
            # if there is no new contracts
            # otherwise just extend the table
            # if not new_contracts:
            if confs['delete_flag']:
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
            if company == companies['iA']:
                db_method.save_data_into_db(cursor, files['saving'], db_method.save_saving, batch_size)
            db_method.save_data_into_db(cursor, files['fund'], db_method.save_fund, batch_size)
        if control_unit & 2:
            db_method.save_data_into_db(cursor, files['transaction'], db_method.save_transaction, batch_size)
        db_method.save_data_into_db(cursor, files['contracts'], db_method.save_contract, batch_size)

        cursor.close()

    print(f"{datetime.now()}: Saving to Databases")
    print("=========================")
