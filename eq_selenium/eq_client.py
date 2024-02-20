from selenium.webdriver.common.by import By

from eq_selenium import eq_selectors
from time import sleep

from utilities.companys import companies

def scrape_client():
    paths = eq_selectors.client_paths()

