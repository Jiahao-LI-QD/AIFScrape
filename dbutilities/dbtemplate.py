from datetime import date
import random
import faker

fake = faker.Faker()


class Contract_number:
    value = 0

    def new_contract_number(self):
        self.value += 1
        return self.value


# generate template for client
Sex = ["Male", "Female", "Other"]
start_date = date(year=1950, month=1, day=1)


def client_template(size):
    return [[
        fake.name().split(' ')[-1],  # last name
        " ".join(fake.name().split(' ')[:-1]),  # first name
        random.choice(Sex),  # Sex
        "English",  # language
        fake.date_between(start_date=start_date, end_date='today'),  # birthday
        fake.address(),  # address
        None,
        fake.city(),  # city
        "ON",  # province
        "XXX XXX",  # zip code
        fake.phone_number(),  # Main_Phone
        fake.phone_number(),  # Office_Phone
        None,  # Fax
        fake.phone_number(),  # Cell_Phone
        fake.email(),  # Primary_Email
        None  # Secondary_Email
    ] for _ in range(size)]


# generate template for contract
cn = Contract_number()
Latest_change = date(year=2020, month=1, day=1)
account_type = ["TFSA", "Non-registered"]


def contract_template(size):
    return [[
        fake.name().split(' ')[-1],  # Applicant_last_name varchar(255) NOT NULL,
        " ".join(fake.name().split(' ')[:-1]),  # Applicant_first_name varchar(255) NOT NULL,
        fake.city(),  # City varchar(255) NOT NULL,
        fake.address(),  # Address varchar(255) NOT NULL,
        "XXX XXX",  # Postal_code varchar(255) NOT NULL,
        "ON",  # Province varchar(255) NOT NULL,
        fake.country(),  # Country varchar(255) NOT NULL,
        "Compliant",  # Address_validity varchar(255) NOT NULL,
        fake.date_between(start_date=Latest_change, end_date='today'),
        # Latest_change_of_address varchar(255) NOT NULL,
        fake.phone_number(),  # Main_phone varchar(255) NOT NULL,
        None,  # Office_phone varchar(255),
        None,  # Cell_phone varchar(255),
        fake.email(),  # Applicant_email varchar(255) NOT NULL,
        random.randint(18, 80),  # Applicant_age int Not NULL,
        fake.date_between(start_date=start_date, end_date='today'),  # Birthday date NOT NULL,
        1000000000 + cn.new_contract_number(),  # Contract_number varchar(255) NOT NULL,
        "IAG SRP",  # Product varchar(255) NOT NULL,
        random.choice(account_type),  # Type varchar(255) NOT NULL,
        fake.date_between(start_date=Latest_change, end_date='today'),  # Contract_start_date varchar(255) NOT NULL,
        random.random() * 100000,  # Contract_market_value money NOT NULL,
        fake.date_between(start_date=Latest_change, end_date='today'),
        # Last_update_of_contract_market_value date NOT NULL
        random.random() * 100000,  # PAC_amount money NOT NULL,
        None,  # PAC_frequency int,
        fake.date_between(start_date=Latest_change, end_date='today'),  # Day_of_the_PAC date NOT NULL,
        fake.name(),  # Representative_name varchar(255) NOT NULL,
        "XXX",  # District varchar(255) NOT NULL,
        "XXX",  # U_S_ varchar(255) NOT NULL,
        "Active",  # Representative_status varchar(255) NOT NULL,
        "IFAST"  # Source varchar(255) NOT NULL,
    ] for _ in range(size)]


# generate template for saving
def saving_template(size):
    return [[
        fake.date_between(start_date=Latest_change, end_date='today'),  # Statement_Date
        1000000000 + random.randint(1, 1000),  # Contract_number
        "TFSA",  # Account_type
        "HI",  # Investment_type
        random.random() * 10,  # Rate
        random.random() * 10000  # balance
    ] for _ in range(size)]


# generate template for transaction
def transaction_template(size):
    return [[
        1000000000 + random.randint(1, 1000),  # Contract_number
        fake.date_between(start_date=Latest_change, end_date='today'),  # Transaction_Date
        "Interest Payment",  # Transaction_type
        random.random() * 10000,  # Fundcode
        None,  # Gross_amount
        random.random() * 100,  # Units
        random.random() * 100  # Unit_value
    ] for _ in range(size)]


# generate template for fund
Category = ["U.S. Equities", "Specialty"]


def fund_template(size):
    return [[
        fake.date_between(start_date=Latest_change, end_date='today'),  # Statement_Date DATE NOT NULL,
        1000000000 + random.randint(1, 1000),  # Contract_number varchar(255) NOT NULL,
        "TFSA",  # Account_type varchar(255) NOT NULL,
        "HI",  # Investment_type varchar(255) NOT NULL,
        random.choice(Category),  # Category varchar(255) NOT NULL,
        f"{random.randint(40000, 50000)} U.S.",  # Fund_name varchar(255) NOT NULL,
        random.random() * 100,  # Units real NOT NULL,
        random.random() * 100,  # Unit_value real NOT NULL,
        random.random() * 100000,  # Value money NOT NULL,
        0  # ACB money,
    ] for _ in range(size)]


# generate template for participant
def participant_template(size):
    return [[
        1000000000 + random.randint(1, 1000),  # Contract_number
        "Annuitant",  # Role
        fake.name(),  # Name
        fake.date_between(start_date=start_date, end_date='today')  # Birthday
    ] for _ in range(size)]


# generate template for beneficiary
Relationship = ["Mother", "Father", "Other"]


def beneficiary_template(size):
    return [[
        1000000000 + random.randint(1, 1000),  # Contract_number
        fake.name(),  # NAME
        random.random() * 10,  # %Allocation
        random.choice(Relationship),  # Relationship
        "revocable"  # Class
    ] for _ in range(size)]
