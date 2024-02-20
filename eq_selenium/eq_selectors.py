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
        'magnifier_button': '/html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/app-dashboard/app-search/div/div/div/form/div[2]/div[4]/div/button',
        'code_table_rows': 'html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/simple-modal-holder/simple-modal-wrapper/div/app-organization-lookup/div/div/div[1]/div/div[4]/div/ul/li/span',
        'next_advisor_page': '/html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/simple-modal-holder/simple-modal-wrapper/div/app-organization-lookup/div/div/div[1]/div/div[5]/div[2]/app-pagination/nav/ul/li',
        'close_advisor_page': '/html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/simple-modal-holder/simple-modal-wrapper/div/app-organization-lookup/div/div/div[2]/button',
        'reset_button': '/html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/app-dashboard/app-search/div/div/div/form/div[3]/button[2]',
        'search_button': '/html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/app-dashboard/app-search/div/div/div/form/div[3]/button[1]',
        'code_input': '/html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/app-dashboard/app-search/div/div/div/form/div[2]/div[3]/div/input',
        'policy_table_rows': '/html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/app-dashboard/app-results/div/div/div[2]/div/div/ngx-datatable/table/tbody/tr'
    }


def client_paths():
    return{
        'contract_no':'/html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/app-dashboard/app-results/div/div/div[2]/div/div/ngx-datatable/table/tbody/tr/td[4]/a[1]',
        'birthday':'/html/body/main/div[6]/div/div[1]/div/div/div/app-policyinquiry/app-dashboard/app-results/div/div/div[2]/div/div/ngx-datatable/table/tbody/tr/td[3]',
        'client_tb':{
             'client_main':'//*[@id="policy_details"]/div[3]/div/div[2]',
            'client_row':'.//*'

        }
    }