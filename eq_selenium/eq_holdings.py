from datetime import datetime

from selenium.webdriver.common.by import By

from eq_selenium import eq_scrap, eq_selectors


def scrape_holdings(wd, holdings):
    paths = eq_selectors.holdings_paths()
    statement_date = datetime.today().strftime('%Y-%m-%d')
    text = wd.find_element(By.XPATH, paths['text']).text.split(' (', 1)
    if len(text) > 1:
        investment_type = text[0]
        policy_number = text[1][:-1]
    else:
        investment_type = None
        policy_number = ''.join(s.replace('(', '').replace(')', '') for s in text)
    account_type = wd.find_element(By.XPATH, paths['account_type']).text
    result = [statement_date, policy_number, account_type, investment_type]

    row = wd.find_elements(By.XPATH, paths['table_data'])
    data = [data.text for data in row]
    raw = [[data[i + 1], data[i]] + [data[i + 3]] + [data[i:i + 6][-2].replace('$', '')]
           + data[i:i + 6][-1:] for i in range(0, len(data), 6)]

    if raw == []:
        result.append('TERMINATED')
        raw = [[None] * 5]

    else:
        result.extend([None])

    final_result = []
    for raw_list in raw:
        final_result.append(result + raw_list + [None, 'EQ'])

    if final_result[0][-5] is not None:
        final_result[0][-5] = float((final_result[0][-5].replace(",", "")))

    holdings.loc[len(holdings)] = final_result[0]
