def login_paths():
    return {
        'sign_in_button': '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div[5]/button',
        'username': '//*[@id="email-input-id"]',
        'password': '//*[@id="pass-input-id"]',
    }


def fund_paths():
    return {
        'statement_date': '//*[@id="1"]/div[1]/div[6]/div/div[2]/span',
        'contract_number': '/html/body/div[3]/div/div[1]/div/div/div/div/'
                           'div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'holdings_button': '//*[@id="2__item"]',
        'text': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/'
                'div/div/div[1]/header/div[2]/ul/li[3]/div/div/div/span'
        }



def traverse_paths():
    return {
        'search_field': '//*[@id="178:0"]',
        'test_Account': '410351753',
        'search_button': '/html/body/div[3]/div/header/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/ul/li[2]',
        'holdings': '//*[@id="2__item"]',
    }
def client_paths():
    return {
        'contract_number':'/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'client_account':'/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/header/div[2]/ul/li[1]/div/div/div',
        'client_hide':'/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/span/lightning-helptext/div/lightning-button-icon/button',
        'client_c1':{
            'c1_main':'/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[2]/div[1]',
            'c1_row':'./div/div'
        },
        'client_c2':{
            'c2_main':'/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[2]/div[2]',
            'c2_row':'./div/div'
        },
        'client_province':'/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[2]/div[3]/div/div/div',
        'client_address':'/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[5]/div[3]/div[1]/span',
        'client_c3':{
            'c3_main':'/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[4]',
            'c3_row':'./div/div/div/div'
        }

    }

def participant_paths():
    return{
        'contract_number':'/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'participant_hide':'/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[3]/div/span/lightning-helptext/div/lightning-button-icon/button',
        'participant_table':{
            'participant_main':'/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr',
            'participant_row':'./td/div'
        }
    }

def beneficiary_paths():
    return {
        'contract_number': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'beneficiary_table':{
            'beneficiary_main':'/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[5]/div[2]/table/tbody/tr',
            'beneficiary_row':'./td/div'
        }
    }


def holdings_paths():
    return {
        'statement_date': '//*[@id="1"]/div[1]/div[6]/div/div[2]/span',
        'contract_number': '/html/body/div[3]/div/div[1]/div/div/div/div/'
                           'div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'holdings_button': '//*[@id="2__item"]',
        'table_xpath': '//*[@id="2"]/article/div[2]/div[5]/table/tbody',
        'text': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/'
                'div/div/div[1]/header/div[2]/ul/li[3]/div/div/div/span'
    }


def transaction_paths():
    return {
        'Transactions_button': '//*[@id="4__item"]',
        'issue_date': '//*[@id="1"]/div[2]/div[2]/div/div[2]/span',
        'start_date': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[4]/article/div[2]/div[1]/div/span[1]/lightning-input[1]/lightning-datepicker/div/div/input',
        'end_date': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[4]/article/div[2]/div[1]/div/span[1]/lightning-input[2]/lightning-datepicker/div/div/input',
        'date_apply': '//*[@id="4"]/article/div[2]/div[1]/div/span[2]/button[1]',
        'contract_number': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'table_body': '//*[@id="4"]/article/div[2]/div[2]/table/tbody/tr',
    }
