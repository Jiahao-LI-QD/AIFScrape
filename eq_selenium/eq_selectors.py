def login_paths():
    return {
        'continue_button': '//html/body/main/section/div/div/div/div/div/form/div[2]/button',
        'username': '//*[@id="username"]',
        'password': '//*[@id="password"]',
        'login_button': '/html/body/main/section/div/div/div/form/div[2]/button'
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