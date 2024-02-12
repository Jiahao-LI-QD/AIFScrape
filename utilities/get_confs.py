import os
import sys
from datetime import datetime

from ia_selenium.ia_contract_list import save_contract_list
from utilities.get_account import account


def get_confs(company):
    """
    This method get all the configurations for a given company
    :param company:
    :return:
    """
    control_unit, maximum_iteration, thread_number, contract_file = get_control(sys.argv)
    # Get required parameters for ia_app
    try:
        match company:
            case 'IA':
                parameters = account("ia_conf")
            case 'CL':
                parameters = account("cl_conf")
            case _:
                print("No Such Company！ Will Exit!")
                exit()
    except Exception as e:
        print(e)
        exit()

    date_today, csvs = generate_date_csv_confs(parameters, company)

    if company == 'IA' and contract_file is None:
        contract_file = save_contract_list(parameters, date_today)

    result = {
        'csvs': csvs,
        'parameters': parameters,
        'control_unit': control_unit,
        'maximum_iteration': maximum_iteration,
        'date_today': date_today,
        'threading_tables': {},
        'thread_number': thread_number
    }

    if company == 'IA':
        result['contract_file'] = contract_file
        result['contract_path'] = os.path.join(parameters['csv_path'], parameters['contracts'], contract_file)
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
    14.Return the values of control, max_iteration, thread_number, and file_name as a tuple.
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
    if len(args) > 3:
        thread_number = int(args[3])

    if len(args) > 4:
        file_name = args[4]

    return control, max_iteration, thread_number, file_name


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
