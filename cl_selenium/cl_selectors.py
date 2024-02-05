def login_paths():
    return {
        'sign_in_button': '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div[5]/button',
        'username': '//*[@id="email-input-id"]',
        'password': '//*[@id="pass-input-id"]',
    }


def traverse_paths():
    return {
        'search_field': '//*[@id="178:0"]',
        'test_Account': '410351753',
        'search_button': '/html/body/div[3]/div/header/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/ul/li[2]',
        'holdings': '//*[@id="2__item"]',
    }


def transaction_paths():
    return {
        'Transactions_button': '//*[@id="4__item"]',
        'issue_date': '//*[@id="1"]/div[2]/div[2]/div/div[2]/span',
        'start_date': 'transactionStartDay',
        'start_date_full': '<input class="slds-input" type="text" id="input-875" part="input" name="transactionStartDay" placeholder="MMM DD, YYYY" autocomplete="off" aria-describedby="range-message-875">',
        'end_date': 'transactionEndDay',
        'end_date_full': '<input class="slds-input" type="text" id="input-878" part="input" name="transactionEndDay" placeholder="MMM DD, YYYY" autocomplete="off" aria-describedby="range-message-878">',
        'date_apply': '//*[@id="4"]/article/div[2]/div[1]/div/span[2]/button[1]',
        'contract_number': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'table_body': '//*[@id="4"]/article/div[2]/div[2]/table/tbody'
    }