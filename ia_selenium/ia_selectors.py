def saving_paths():
    return {
        'investment_button': '//*[@id="Placements"]/a',
        'date_text': '//*[@id="content"]/div[3]',
        'contract_number_account_type': '//*[@id="content"]/div[1]/div[1]/div/span',
        'rate': './div[2]/table/tbody/tr[2]/td[1]',
        'balance': './div[2]/table/tbody/tr[2]/td[2]',
        'table_body': {
            'main_body': './div[2]/table/tbody/*',
            'table_rows': ".//*"
        }
    }


def fund_paths():
    return {
        'investment_block':'//*[@id="content"]/div[@class="row sub-row entete-fonds"]',
        'investment_type': './div[1]/div/div[1]',
        'title': '//*[@id="content"]/div[1]/div[1]/div/span',
        'statement_date': '//*[@id="content"]/div[3]',
        'investment_page':'//*[@id="Placements"]/a',
        'table_body': {
            'main_body': './div[2]/table/tbody/*',
            'table_rows': ".//*",
            'table_data': ".//td"
        }
    }


def login_paths():
    return {
        'sign_in_button': '//*[@id="eeCleanLoader"]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/a',
        'username': '//*[@id="idp-discovery-username"]',
        'cookie_button': '/html/body/div[2]/div[2]/a[1]',
        'submit_username': '//*[@id="idp-discovery-submit"]',
        'password': '//*[@id="okta-signin-password"]',
        'submit_password': '//*[@id="okta-signin-submit"]',
        'cookie_consent': 'body > div.cc-window.cc-banner.cc-type-opt-in.cc-theme-classic.cc-bottom.cc-color-override'
                          '-218275418',
    }


def scrape_paths():
    return {
        'myclient_button': '//*[@id="mnMesClients"]/a',
        'contract_number_input': '//*[@id="ContractNumber"]',
        'search_button': '//*[@id="btnSearch"]',
        'cookie_button': '/html/body/div[2]/div[2]/a[1]',
        'cookie_consent': 'body > div.cc-window.cc-banner.cc-type-opt-in.cc-theme-classic.cc-bottom.cc-color-override'
                          '-218275418',
        'error_page': "/html/body/div[1]/ee-header-fullpage/div/div[1]/span/div[1]/div"
    }


def transactions_path():
    return {
        'transaction_button': '//*[@id="Transactions"]/a',
        'issue_date': '//*[@id="Debut"]',
        'refresh_Button': '//*[@id="rechercheTransactions"]',
        'contract_number_account_type': '//*[@id="content"]/div[1]/div[1]/div/span',
        'table_header': '//*[@id="TransactionsTrouveesDiv"]/div[3]/table/thead/tr/th[6]',
        'table_data': '//*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr',
        'has_transaction': '//*[@id="TransactionsTrouveesDiv"]/div[3]/table/tbody/tr/td',
        'next_page': '//*[@id="TransactionsTrouveesDiv"]/div[3]/table/tfoot/tr/td/a/span',
        'CSS_next_page': '#TransactionsTrouveesDiv > div:nth-child(6) > table > tfoot > tr > td > a.suivant > span'
    }


def client_paths():
    return {
        'contract_specifications': '//*[@id="Specifications"]/a',
        'personal_information': '//*[@id="content"]/div[3]/table[2]/tbody/tr[4]/td[2]/a',
        'table_client': {
            'main_client': '//*[@id="search_content"]/div/div[3]/table/tbody/tr',
            'row_client': './td[2]'
        }
    }


def participant_paths():
    return {
        'contract_number': '//*[@id="content"]/div[3]/table[1]/tbody/tr[1]/td[2]',
        'table_participant': {
            'main_participant': '//*[@id="content"]/div[3]/div[1]/table/tbody/tr',
            'items_participant': './/*'
            # 'role_participant': './td[1]',
            # 'name_participant':'./td[2]',
            # 'birthday_participant':'./td[3]'
        }
    }


def beneficiary_paths():
    return {
        'contract_number': '//*[@id="content"]/div[3]/table[1]/tbody/tr[1]/td[2]',
        'beneficiary_Category': '//*[@id="content"]/div[3]/div[2]/p',
        'table_beneficiary': {
            'main_beneficiary': '//*[@id="content"]/div[3]/div[2]/table/tbody/tr',
            'items_beneficiary': './/*'
            # 'name_beneficiary': './td[1]',
            # 'allocation_beneficiary': './td[2]',
            # 'birthday_beneficiary':'./td[3]',
            # 'relationship_beneficiary': './td[3]',
            # 'class_beneficiary': './td[4]'

        }

    }


def save_path():
    return {
        'mailbox_button': '//*[@id="mnSectExpAgence"]/a[2]',
        'file_link1': '//*[@id="inboxMessageTable"]/tbody/tr[1]/td[3]/span[3]/a',
        'file_link2': '//*[@id="Attachments"]/ul/li/a',
        'next_button': '//*[@id="PreviousNext"]/a[2]',
        'download_file': '//*[@id="Attachments"]/ul/li/a'
    }


def download_path():
    return {
        'myclient_button': '//*[@id="mnMesClients"]/a',
        'group': '//*[@id="HierarchyBtn"]',
        'FV6_group': '//*[@id="hierarchy_treeview"]/div[2]/div[1]/span[2]',
        'GK4_group': '//*[@id="hierarchy_treeview"]/div[2]/div[3]/span[2]',
        'download_option': '//*[@id="SearchCriteriaForm"]/div/div[6]/div/div[6]/label',
        'search_button': '//*[@id="btnSearch"]',
        'submit_button': '//*[@id="ia-ali-2c-floating-portlet-layout-container"]/div[3]/form/div[2]/input'
    }
