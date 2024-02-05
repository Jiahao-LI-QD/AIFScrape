from time import sleep

from selenium.webdriver.common.by import By

from cl_selenium import cl_scrap, cl_selectors

# save cl_conf as parameters
parameters = cl_scrap.cl_account()
print(parameters)

# set up Chrome driver
wd = cl_scrap.driver_setup(parameters)
wd.get(parameters['web_url'])

# testing for log in function
cl_scrap.login(wd, parameters['username'], parameters['password'])

# Going to an account for testing
paths = cl_selectors.traverse_paths()
wd.find_element(By.XPATH, paths['search_field']).send_keys(410351753)
sleep(1)
wd.find_element(By.XPATH, paths['search_button']).click()
sleep(5)

# TODO: Eva's code here

wd.find_element(By.XPATH, paths['holdings']).click()
sleep(5)

# TODO: Christina's code here
