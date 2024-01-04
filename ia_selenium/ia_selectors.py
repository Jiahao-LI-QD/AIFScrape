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