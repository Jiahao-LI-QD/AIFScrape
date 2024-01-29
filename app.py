from ia_selenium import ia_scrap
from ia_selenium.ia_scrap import ia_get_start

# ia_wd : chrome driver
# maximum_iteration: max iteration of scrap loop
# control_unit: get control unit for scrap
# ia_parameters: get parameters setting
# tables: information containers
# csvs: the file location
ia_wd, maximum_iteration, control_unit, ia_parameters, tables, csvs = ia_get_start()

# do - while loop to traverse through the contract numbers until no exception
iteration_time = 0
while iteration_time < maximum_iteration:
    ia_scrap.scrape_traverse(ia_wd, control_unit, tables, csvs, iteration_time, ia_parameters)
    if len(tables['recover']) == 0:
        break
    iteration_time += 1

ia_scrap.scrape_cleanup(ia_wd, tables)

# record file names
files = ia_scrap.get_csv_file_names(csvs)

# save tables into csv files
ia_scrap.save_table_into_csv(control_unit, tables, files)

# save csv files into db
ia_scrap.save_csv_to_db(control_unit, files, tables)

# request contract numbers
ia_scrap.click_contract_list(ia_wd)
