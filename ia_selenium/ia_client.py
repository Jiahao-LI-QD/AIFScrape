from selenium.webdriver.common.by import By
def scrape(wd, client):
    wd.find_element(By.XPATH, '//*[@id="Specifications"]/a').click()
    wd.find_element(By.XPATH, '//*[@id="content"]/div[3]/table[2]/tbody/tr[4]/td[2]/a').click()

    wd.implicitly_wait(10)

    Client_list = wd.find_elements(By.XPATH, '//*[@id="search_content"]/div/div[3]/table/tbody/tr')
    client_ = [Client_row.find_element(By.XPATH, './td[2]').text for Client_row in Client_list]
    client.loc[-1] = client_
    print(client)
