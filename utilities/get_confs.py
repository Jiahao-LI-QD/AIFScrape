import os
import sys
from datetime import datetime

from ia_selenium.ia_contract_list import save_contract_list
from utilities.companys import companies
from utilities.get_account import account


def get_confs(company):
    """
    This method get all the configurations for a given company
    :param company: (string) The name of the company for which configurations are needed.
    :return: a dictionary containing various parameters and settings.

    Workflow:
    1.The function first calls the get_control function to retrieve the control mode, maximum iteration,
      thread number, and contract file from the command line arguments.
    2.It then uses a match statement to determine the appropriate configuration file based on the company name.
    3.If the company name is not recognized, it prints an error message and exits the program.
    4.The function calls the account function to retrieve the parameters for the specified company.
    5.It calls the generate_date_csv_confs function to generate the date and CSV directory for saving the app result.
    6.If the company is 'iA' and no contract file is provided, it calls the save_contract_list function
      to download and save the contract list.
    7.The function constructs a dictionary containing the CSV directory, parameters, control unit, maximum iteration,
      date today, threading tables, and thread number.
    8.If the company is 'iA', it adds the contract file and contract path to the dictionary.
    9.The dictionary is returned as the output of the function.
    """
    control_unit, maximum_iteration, thread_number, contract_file, head_mode, delete_flag = get_control(sys.argv)
    # Get required parameters for ia_app
    try:
        match company:
            case 'iA':
                parameters = account("ia_conf")
            case 'CL':
                parameters = account("cl_conf")
            case 'EQ':
                parameters = account("eq_conf")
            case _:
                print("No Such Company！ Will Exit!")
                exit()
    except Exception as e:
        print(e)
        exit()

    date_today, csvs = generate_date_csv_confs(parameters, company)
    thread_names = []
    for i in range(thread_number):
        thread_names.append('thread' + str(i))

    result = {
        'csvs': csvs,
        'parameters': parameters,
        'control_unit': control_unit,
        'maximum_iteration': maximum_iteration,
        'date_today': date_today,
        'thread_tables': {},
        'thread_number': thread_number,
        'head_mode': head_mode,
        'delete_flag': delete_flag,
        'thread_status': {},
        'thread_names': thread_names
    }

    if company == companies['iA'] and (contract_file is None or contract_file == '_'):
        contract_file = save_contract_list(result)
        result['contract_path'] = os.path.join(result['csvs'], str(contract_file))
    else:
        result['contract_path'] = os.path.join(parameters['csv_path'], contract_file)

    if company == companies['iA']:
        result['contract_file'] = contract_file
    return result


def get_control(args):
    """
    This method
    1: mixed control modes for app, default mode is 1
    mode 1: scraping investments only
    mode 2: scraping transactions only
    mode 4: scraping clients only
    or combine 3 modes arbitrarily
    2:number of iteration
    set up default iteration to 3, range from 1-5
    3:number of thread
    set up default thread to 1, when filename is not defined
    4: filename(Excel file)
    :param args: system arguments
    :return: control mode, iteration times, thread number and filename
    5. head_mode: Web-driver runs with window if True. Default: False
    6. delete_flag: delete the current data in SQL server if True. Default: True

    Workflow:
    1.Set the default control mode to 1.
    2.If the length of args is greater than 1, set the control mode to be the first argument.
    3.If control is not in the range of 1 to 8, print a message indicating that the control mode is not supported
    and use the default scrape mode.
    4.If control mode set to 1, print a message indicating that the task is to scrape investments only.
    5.If control mode set to 2, print a message indicating that the task is to scrape transactions only.
    6.If control mode set to 4, print a message indicating that the task is to scrape clients information only.
    7.control mode can be mixed up scrape for all or two of the tasks
    8.Set the default maximum iteration to 3.
    9.If the length of args is greater than 2, set the maximum iteration to be the second argument.
    10.If max_iteration is less than 1 or greater than 5, raise an exception indicating that the maximum number of
    iterations must be between 1 and 5.
    11.Set the default thread number to 1.
    12.If the length of args is greater than 3, set the thread number to be the third argument.
    13.If the length of args is greater than 4, assign the fourth argument to file_name.
    13.If the length of args is greater than 5, assign the fifth argument to head_mode.
    13.If the length of args is greater than 6, assign the sixth argument to delete_flag.
    14.Return the values of control, max_iteration, thread_number, file_name, head_mode and delete_flag as a tuple.
    """
    control = 1
    if len(args) > 1:
        control = int(args[1])
    if control not in range(1, 8):
        print(f"The control model is not supported, will use default scrape mode")

    if control & 1:
        print("Task: Scrape Investments")
    if control & 2:
        print("Task: Scrape Transactions")
    if control & 4:
        print("Task: Scrape Clients Information")
    print("======================")

    max_iteration = 3
    if len(args) > 2:
        try:
            max_iteration = int(args[2])
            if max_iteration < 1 or max_iteration > 5:
                raise Exception("The maximum number of iterations must be between 1 and 5")
        except TypeError as e:
            print("Max iteration setting is not a valid number between 1 and 5")
        except Exception as e:
            print(e)

    thread_number = 1
    file_name = None
    head_mode = False
    delete_flag = True
    if len(args) > 3:
        thread_number = int(args[3])

    if len(args) > 4:
        file_name = args[4]

    if len(args) > 5:
        if args[5].lower() in ['h', 'head']:
            head_mode = True

    if len(args) > 6:
        if args[6].lower() in ['k', 'keep']:
            delete_flag = False

    return control, max_iteration, thread_number, file_name, head_mode, delete_flag


def generate_date_csv_confs(parameters, company_name):
    """
    Generates the date and csv directory for saving the app result, and return the date and csv
    :param company_name: the company name
    :param parameters: for configuration
    :return date_today: timestamp of the app start
    :return csvs: the saving directory of the results
    """
    date_today = "{:%Y_%m_%d_%H_%M_%S}".format(datetime.now())

    csvs = os.path.join(parameters['csv_path'], date_today + '_' + company_name)

    # make directory for current scarp process
    try:
        os.mkdir(csvs)
        print(f"Create {csvs} directory!")
    except Exception as e:
        print(f"The directory {csvs} already exist!")

    return date_today, csvs
