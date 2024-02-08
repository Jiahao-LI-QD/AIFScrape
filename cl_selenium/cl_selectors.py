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


def policies_paths():
    return {
        'filter_button': '//*[@id="report-00O5o000000XMr4EAG"]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div['
                         '3]/div/div/button',
        'clear_search': '#report-00O5o000000XMr4EAG > div > div.dashboard-container.with-header > '
                        'div.dashboard-builder-body.dashboard-show-header > div > div > div '
                        '> div > div > div > div.grid-layout > div > div > '
                        'div.widget-container.widget-container_queryBuilder > div > div > div > '
                        'div > div > div > div > div.sectionable-table-section-content > div >'
                        'div.sectionable-table-group-content > ul > li:nth-child(4) > div > div '
                        '> div > div > div > button',
        'subtotal_button': '//*[@id="report-00O5o000000XMr4EAG"]/div/div[1]/'
                           'div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/div'
                           '/div[3]/div/div/div/div/div[3]/label/span[2]/span',
        'grand_total_button': '//*[@id="report-00O5o000000XMr4EAG"]/div/div[1]/'
                              'div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/div'
                              '/div[3]/div/div/div/div/div[4]/label/span[2]/span',
        'table': {'rows': "//div[@class='data-grid-table-ctr' and not(@aria-hidden='true')]/table/tbody/tr",
                  'columns_of_row': './*/div/div',
                  'account_name': './/a'
                  }

    }
