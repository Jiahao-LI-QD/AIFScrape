from datetime import datetime
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
sleep(5)
# Going to an account for testing
paths = cl_selectors.traverse_paths()
wd.find_element(By.XPATH, paths['search_field']).send_keys(410529465)
sleep(10)
wd.find_element(By.XPATH, paths['search_button']).click()
sleep(5)

# TODO: Eva's code here


# TODO: Christina's code here
paths = cl_selectors.fund_paths()
statement_date = wd.find_element(By.XPATH, paths['statement_date']).text
formatted_date = datetime.strptime(statement_date, '%b. %d, %Y').strftime('%Y-%m-%d')
contract_number = wd.find_element(By.XPATH, paths['contract_number']).text
holdings = wd.find_element(By.XPATH, paths['holdings_button']).click()
text = wd.find_element(By.XPATH, paths['text']).text.split(' (', 1)
account_type = text[0]
investment_type = text[1][:-1]
#
result = [formatted_date, contract_number, account_type, investment_type]
# input()
# category = wd.find_elements(By.XPATH, '//*[@id="2"]')
# n = category[0].find_elements(By.XPATH, './*')
# print(len(wd.find_elements(By.TAG_NAME, 'article')))

#TODO: each row data need to have separate list
table_xpath = '//*[@id="2"]/article/div[2]/div[5]/table/tbody'
table_element = wd.find_elements(By.XPATH, table_xpath)

for row in table_element[0].find_elements(By.XPATH, ".//tr"):

        # Check if the row has <td> elements
    if row.find_elements(By.XPATH, ".//th"):
        Category = row.text
        result.append(Category)
        print(Category)  # Debugging print statement

    else:
        columns = row.find_elements(By.XPATH, ".//td")
        for column in columns:
            result.append(column.text)


print(result)
