import sys
import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cl_selenium import cl_selectors


# Read configs from cl_conf to get url, username, password, and folder paths
def cl_account():
    with open(os.path.join(sys.path[1], r"confs\cl_conf")) as f:
        l = [line.rstrip('\n').split("=", 1) for line in f.readlines()]
        d = {key.strip(): value.strip() for key, value in l}
    if "username" not in d or "password" not in d:
        raise Exception("CL account info not found. Please provide it in confs/cl_conf")
    if "web_url" not in d:
        raise Exception("Web url not found. Please provide it in confs/cl_conf")
    if "csv_path" not in d:
        raise Exception("File path for csv files not found. Please provide it in confs/cl_conf")
    return d


def get_control(args):
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


def cl_get_confs():
    control_unit, maximum_iteration, thread_number, contract_file = get_control(sys.argv)
    # Get required parameters for cl_app
    try:
        cl_parameters = cl_account()
    except Exception as e:
        print(e)
        exit()

    date_today = "{:%Y_%m_%d_%H_%M_%S}".format(datetime.now())

    csvs = os.path.join(cl_parameters['csv_path'], date_today)

    # make directory for current scarp process
    try:
        os.mkdir(csvs)
        print(f"Create {cl_parameters['csv_path']}\\{date_today} directory!")
    except Exception as e:
        print(f"The directory {cl_parameters['csv_path']}\\{date_today} already exist!")

    threading_tables = {}

    if contract_file is None:
        # contract_file = save_contract_list(cl_parameters, date_today)
        pass

    return {
        'csvs': csvs,
        'parameters': cl_parameters,
        'control_unit': control_unit,
        'maximum_iteration': maximum_iteration,
        'contract_file': contract_file,
        'date_today': date_today,
        'threading_tables': threading_tables,
        'thread_number': thread_number
    }


def driver_setup(parameters):
    # start web driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': os.path.join(parameters['csv_path'], parameters['contracts'])}
    chrome_options.add_experimental_option('prefs', prefs)
    # chrome_options.add_argument('headless')
    wd = webdriver.Chrome(chrome_options)
    wd.implicitly_wait(10)
    return wd


# Login for Canada Life Advisor Workspace
def login(wd, user, password):
    paths = cl_selectors.login_paths()
    wait = WebDriverWait(wd, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, paths['username'])))
    wd.find_element(By.XPATH, paths['username']).send_keys(user)
    wd.find_element(By.XPATH, paths['password']).send_keys(password)
    time.sleep(1)
    wd.find_element(By.XPATH, paths['sign_in_button']).click()

    print(f"user : {user} login successful!")