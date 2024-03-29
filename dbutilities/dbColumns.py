saving_columns = ["Statement_Date", "Contract_number", "Account_type", "Investment_type", "FundCode", "InvestedDate",
                  "MaturityDate", "Amount", "Rate", "Type", "Balance", "Company"]

client_columns = ["LastName", "FirstName", "Sex", "Language", "Birthday", "Address", "Address_line2", "City",
                  "Province", "Postal_Code", "Main_Phone", "Office_Phone", "Fax", "Cell_Phone", "Primary_Email",
                  "Secondary_Email", "Contract_number_as_owner", "Company"]

contract_columns = ["Applicant_last_name", "Applicant_first_name", "City", "Address", "Postal_code", "Province",
                    "Country", "Address_validity", "Latest_change_of_address", "Main_phone", "Office_phone",
                    "Cell_phone", "Applicant_email", "Applicant_age", "Birthday", "Contract_number", "Product",
                    "Type", "Contract_start_date", "Contract_market_value", "Last_update_of_contract_market_value",
                    "PAC_amount", "PAC_frequency", "Day_of_the_PAC", "Representative_name", "District", "U_S_",
                    "Representative_status", "Source", "Company"]

transaction_columns = ["Contract_number", "Transaction_Date", "Transaction_type", "Fundcode", "Gross_amount", "Units",
                       "Unit_value", "Company"]

fund_columns = ["Statement_Date", "Contract_number", "Account_type", "Investment_type", "Category", "Fund_code",
                "Fund_name", "Units", "Unit_value", "Value", "ACB", "Company"]

participant_columns = ["Contract_number", "Role", "Name", "Birthday", "Company"]

beneficiary_columns = ["Contract_number", "BenefitCategory", "Role", "Name", "Allocation", "Relationship", "Class",
                       "Birthday", "Company"]
