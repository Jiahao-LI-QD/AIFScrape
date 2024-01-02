from selenium.webdriver.common.by import By
from ia_selenium import keys


def login(wd, user, password):
    wd.find_element(By.XPATH,
                    '//*[@id="eeCleanLoader"]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/a').click()

    wd.find_element(By.XPATH, '//*[@id="idp-discovery-username"]').send_keys(user)

    # accept cookies
    wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/a[1]').click()

    wd.find_element(By.XPATH, '//*[@id="idp-discovery-submit"]').click()

    wd.find_element(By.XPATH, '//*[@id="okta-signin-password"]').send_keys(password)

    wd.find_element(By.XPATH, '//*[@id="okta-signin-submit"]').click()

    print(f"user : {user} login successful!")