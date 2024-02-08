import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_serial_number(wd):
    # clear filter
    time.sleep(10)
    wait = WebDriverWait(wd, 10)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))

    # click filter
    wd.find_element(By.XPATH, '//*[@id="report-00O5o000000XMr4EAG"]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div['
                              '3]/div/div/button').click()

    time.sleep(1)
    # click clear search
    wd.find_element(By.CSS_SELECTOR, '#report-00O5o000000XMr4EAG > div > div.dashboard-container.with-header > '
                                     'div.dashboard-builder-body.dashboard-show-header > div > div > div '
                                     '> div > div > div > div.grid-layout > div > div > '
                                     'div.widget-container.widget-container_queryBuilder > div > div > div > '
                                     'div > div > div > div > div.sectionable-table-section-content > div >'
                                     'div.sectionable-table-group-content > ul > li:nth-child(4) > div > div '
                                     '> div > div > div > button').click()
    time.sleep(1)
    # close filter
    wd.find_element(By.XPATH, '//*[@id="report-00O5o000000XMr4EAG"]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div['
                              '3]/div/div/button').click()
    # remove subtotals
    wd.find_element(By.XPATH, '//*[@id="report-00O5o000000XMr4EAG"]/div/div[1]/'
                              'div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/div'
                              '/div[3]/div/div/div/div/div[3]/label/span[2]/span').click()
    # remove grand totals
    wd.find_element(By.XPATH, '//*[@id="report-00O5o000000XMr4EAG"]/div/div[1]/'
                              'div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/div'
                              '/div[3]/div/div/div/div/div[4]/label/span[2]/span').click()
    last_serial = ''
    while True:
        last_serial, ended = loop_list(wd, last_serial)
        if ended:
            break


def loop_list(wd, last_serial=''):
    actions = ActionChains(wd)
    # get row content
    account_name = ''
    ended = False

    rows = wd.find_elements(By.XPATH, "//div[@class='data-grid-table-ctr' and not(@aria-hidden='true')]/table/tbody/tr")
                            #'//*[@id="report-00O5o000000XMr4EAG"]/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[4]/table/tbody/tr')
                            #//*[@id="report-00O5o000000XMr4EAG"]/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[4]/table/tbody/tr

    slice_start = 0
    slice_end = -1
    # remove the first header row
    if 'data-grid-header-row' in rows[slice_start].get_attribute('class'):
        slice_start += 1
    # remove the first and last spacer whice have no content for scrape
    if rows[slice_start].get_attribute('class') == 'data-grid-table-row-spacer':
        slice_start += 1
    if rows[slice_end].get_attribute('class') != 'data-grid-table-row-spacer':
        ended = True
        slice_end = len(rows)
    rows = rows[slice_start:slice_end]

    if last_serial == '':
        new_row = True
    else:
        new_row = False
    for row in rows:
        columns = row.find_elements(By.XPATH, './*/div/div')[:-1]
        if len(columns) > 4:
            account_name = columns[0].find_element(By.XPATH, './/a').text
            columns = columns[1:]
        texts = [c.text for c in columns]
        texts.insert(0, account_name)
        # check the investment is not insurance and it is not empty
        if new_row and not ('insurance' in texts[3] or texts[3] == '-'):
            print(texts)
            last_serial = texts[2]
        if not new_row and texts[2] == last_serial:
            new_row = True

    actions.move_to_element(rows[-1]).perform()
    return last_serial, ended
