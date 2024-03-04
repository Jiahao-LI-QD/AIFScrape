def login_paths():
    return {
        'continue_button': '//html/body/main/section/div/div/div/div/div/form/div[2]/button',
        'username': '//*[@id="username"]',
        'password': '//*[@id="password"]',
        'login_button': '/html/body/main/section/div/div/div/form/div[2]/button',
        'main_page': '//*[@id="mainnav"]/ul/li[1]/a',
    }

def policy_paths():
    return {
        'search_button': '/html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/app-dashboard/app-search/div/div/div/form/div[3]/button[1]',
        'export_all': '/html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/app-dashboard/app-results/div/div/div[1]/div[2]/button[1]'
    }


def client_paths():
    return{
        'owner':'//*[@id="Owner"]',
        'name':'//*[@id="policy_details"]/div[@class="Owner"]/div/div[2]/div[1]/div[2]/p',
        'c1_table':{
            'c1_main':'//*[@id="policy_details"]/div[@class="Owner"]/div/div[2]/div[2]/div[2]/div',
            'c1_row':'./p'
        },
        'c2_table':{
            'c2_main':'//*[@id="policy_details"]/div[@class="Owner"]/div/div[2]/div[3]',
            'c2_row':'./div/div[2]/p'
        }
    }
def participant_paths():
    return{
        'annuitant':'//*[@id="Annuity"]',
        'a1_table':{
            'a1_main':'//*[@id="policy_details"]/div[@class="Annuity"]/div/div[2]',
            'a1_row':'./div/div/p'
        },
        'a2_table':{
            'a2_main':'//*[@id="policy_details"]/div[@class="Annuity"]/div/div[2]/div/div[2]/div',
            'a2_row':'./div/p[2]'
        }
    }
def beneficiary_paths():
    return {
        'beneficiary':'//*[@id="Beneficiary"]',
        'b_table':{
            'b_main':'//*[@id="policy_details"]/div[@class="Beneficiary"]/div/div[2]',
            'b_row':'./div'
        }
    }


def holdings_paths():
    return {
        'text': '//*[@id="policy_content"]/div[1]/h1[1]',
        'account_type': '//*[@id="policy_content"]/div[3]/div[1]/p[2]',
        'table_data': '//*[@id="policy_details"]/div[3]/div/div[3]/div[1]/table/tbody/tr/td'

    }


def transactions_paths():
    return {
        'transaction_button': '//*[@id="Transactions"]',
        'update_button': '//*[@id="update_period"]',
        'start_date': '//*[@id="policy_content"]/div[3]/div[2]/p[2]',
        'date_range': '//*[@id="periodSelection"]',
        'from_month': '//*[@id="from_month"]',
        'from_year': '//*[@id="from_year"]',
        'to_month': '//*[@id="to_month"]',
        'to_year': '//*[@id="to_year"]',
        'no_transaction_alert': '//*[@id="no_transactions"]',
        'rows': '//*[@id="policy_details"]/div[@class="Transactions"]/div/div[2]/div[2]/table/tbody/tr',
        'columns': './*'
    }