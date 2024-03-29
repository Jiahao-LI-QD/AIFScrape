def login_paths():
    return {
        'sign_in_button': '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div[5]/button',
        'username': '//*[@id="email-input-id"]',
        'password': '//*[@id="pass-input-id"]',
        'web_url': 'https://lifeco.my.site.com/workspace/s/login/',
        'page_load': '/html/body/div[3]/div/div[1]/div/div/div[1]/div/div[3]/div/div/div/c-w-page-title/div'
    }


def fund_paths():
    return {
        'statement_date': '//*[@id="1"]/div[1]/div[6]/div/div[2]/span',
        'contract_number': '/html/body/div[3]/div/div[1]/div/div/div/div/'
                           'div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'guarantee': '//*[@id="1"]/div[1]/div[5]/div/div[2]/span',
        'holdings_button': '//*[@id="2__item"]',
        'text': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/'
                'div/div/div[1]/header/div[2]/ul/li[3]/div/div/div/span'
    }


def traverse_paths():
    return {
        'search_field': '//*[@id="178:0"]',
        'dropdown_layer': '/html/body/div[3]/div/header/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/ul/li',
        'policy_submit': '/html/body/div[3]/div/header/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/ul/li[2]',
        'policy_search': '/html/body/div[3]/div/header/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/ul/li[1]',
        'table_data': '/html/body/div[3]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div/table/tbody',
        'row_data': '/html/body/div[3]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div/table/tbody/tr[1]',
        'asset_name1': '/html/body/div[3]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div/table/tbody/tr[1]/td[1]/a',
        'asset_name2': '/html/body/div[3]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div/table/tbody/tr[2]/td[1]/a',
        'asset_name3': '/html/body/div[3]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div/table/tbody/tr[3]/td[1]/a',
        'holdings': '//*[@id="2__item"]',
        'account_header': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/header/div[2]/ul/li[4]/div/div/div/span',
        'account_error': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div/div/div[1]',
        # 'account_error': '<div class="slds-align_absolute-center error-title" data-aura-rendered-by="3187:0">Sorry, something went wrong</div>',
        'summary_table': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]',
        'page_load': '/html/body/div[3]/div/div[1]/div/div/div[1]/div/div[3]/div/div/div/c-w-page-title/div'
    }


def client_paths():
    return {
        'contract_number': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'client_account': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/header/div[2]/ul/li[1]/div/div/div',
        'client_kind': '/html/body/div[3]/div/div[1]/div/div/div[1]/div/div[3]/div/div/div[2]/c-w-custom-compact-layout/div/div[2]/div/ul/li[2]/div[2]',
        'client_hide': '/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/span/lightning-helptext/div/lightning-button-icon/button',
        'client_c1': {
            'c1_main': '/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[2]/div[1]',
            'c1_row': './div/div'
        },
        'client_c2': {
            'c2_main': '/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[2]/div[2]',
            'c2_row': './div/div'
        },
        'client_r3': '/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[2]/div[3]/div/div/div',
        'client_address': '/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[5]/div[3]/div[1]/span',
        'client_c3': {
            'c3_main': '/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/div/section/div/div/article/div/div[4]',
            'c3_row': './div/div/div/div'
        },
        # 'summary_button': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/lightning-tab-bar/ul/li[1]/a',
        'summary_button': '//*[@id="1__item"]'
    }


def participant_paths():
    return {
        'contract_number': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'participant_table': {
            'participant_main': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr',
            'hide_row': './td[3]/div/span/lightning-helptext/div/lightning-button-icon/button',
            'participant_row': './td/div'
        },
        'hidden': lambda
            x: f"/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[{x}]/td[3]/div/span/lightning-helptext/div/lightning-button-icon/button",
        'hidden_1':'/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[3]/div/span/lightning-helptext/div/lightning-button-icon/button',
        'block': '//*[@id="1"]/div[1]/*',
        'participant_t1':{
            'participant_m1':'/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr',
            'participant_r1':'./td/div'
        }
    }


def beneficiary_paths():
    return {
        'contract_number': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'beneficiary_table': {
            'beneficiary_main': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[5]/div[2]/table/tbody/tr',
            'beneficiary_row': './td/div'
        },
        'block':'//*[@id="1"]/div[1]/*',
        'beneficiary_t1':{
            'beneficiary_m1':'/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div/div[1]/div[5]/div[2]/table/tbody/tr',
            'beneficiary_r1':'./td/div'
        }
    }


def holdings_paths():
    return {
        'statement_date': '//*[@id="1"]/div[1]/div[6]/div/div[2]/span',
        'contract_number': '/html/body/div[3]/div/div[1]/div/div/div/div/'
                           'div[3]/div/div/div[1]/header/div[2]/div/div[1]/div[2]/h1/div[2]/span',
        'guarantee': '//*[@id="1"]/div[1]/div[5]/div/div[2]/span',
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
        # 'summary_button': '/html/body/div[3]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/lightning-tab-bar/ul/li[1]',
        'summary_button': '//*[@id="1__item"]',
        'page_2': '//*[@id="4"]/article/div[3]/div/span[2]/a',
        'page_1': '//*[@id="4"]/article/div[3]/div/span[1]/a',
        'page_count': '//*[@id="4"]/article/div[3]/div/span'
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
