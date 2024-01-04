def saving_paths():
    return {
        'investment_button': '//*[@id="Placements"]/a',
        'date_text': '//*[@id="content"]/div[3]',
        'contract_number_account_type': '//*[@id="content"]/div[1]/div[1]/div/span',
        'investment_type': '//*[@id="content"]/div[4]/div[1]/div/div[1]',
        'rate': '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[2]/td[1]',
        'balance': '//*[@id="content"]/div[4]/div[2]/table/tbody/tr[2]/td[2]'
    }


def fund_paths():
    return {
        'table_body':{
            'main_body': '//*[@id="content"]/div[4]/div[2]/table/tbody/*',
            'table_rows':  ".//*"
        }
    }


def login_paths():
    return {
        'sign_in_button': '//*[@id="eeCleanLoader"]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/a',
        'username': '//*[@id="idp-discovery-username"]',
        'cookie_button': '/html/body/div[2]/div[2]/a[1]',
        'submit_username': '//*[@id="idp-discovery-submit"]',
        'password': '//*[@id="okta-signin-password"]',
        'submit_password': '//*[@id="okta-signin-submit"]'
    }


def scrape_paths():
    return {
        'myclient_button': '//*[@id="mnMesClients"]/a',
        'contract_number_input': '//*[@id="ContractNumber"]',
        'search_button': '//*[@id="btnSearch"]',
        'cookie_button': '/html/body/div[2]/div[2]/a[1]'
    }