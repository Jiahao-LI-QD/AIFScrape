from datetime import date
import random
import faker

fake = faker.Faker()
# Client_columns = ["LastName", "FirstName", "Sex", "Language", "Birthday", "Address", "Address_line2", "City", "Province",
#                   "Postal_Code", "Main_Phone", "Office_Phone", "Fax", "Cell_Phone", "Primary_Email", "Secondary_Email"]
Sex = ["Male", "Female", "Other"]
start_date = date(year=1950, month=1, day=1)
client_template = [fake.name().split(' ')[-1], fake.name().split(' ')[:-1], random.choice(Sex), "English",
                   fake.date_between(start_date=start_date, end_date='today'), fake.address(), fake.city(), fake.province(),
                   fake.postcode(), fake.phone_number(), fake.phone_number(), None, fake.phone_number(), fake.email(), fake.email()]

hi_template = [date.today(), "contr" + str(random.randint(1, 10000)), "TFSA", "HI",
               random.random() * 10, random.random() * 10000]
