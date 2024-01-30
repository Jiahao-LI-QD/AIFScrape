# CURRENT SAVING TABLE CREATION
import csv

import pandas as pd

"""
CREATE TABLE Saving_Current (
    HiId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    StatementDate DATE NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    AccountType varchar(255) NOT NULL,
    InvestmentType varchar(255) NOT NULL,
    FundCode varchar(255) NULL,
    InvestedDate DATE NULL,
    MaturityDate DATE NULL,
    Amount money NULL,
    Rate real NOT NULL,
    Type varchar(255) NULL,
    Balance money NOT NULL,
    SnapshotTime datetime NOT NULL;

drop table Saving_Current;

select * from Saving_Current;

delete from Saving_Current;

DBCC CHECKIDENT ('Saving_Current', reseed,0);
"""


def save_saving(cursor, values):
    cursor.executemany("insert into Saving_Current values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()


# CURRENT CLIENT TABLE CREATION
"""
CREATE TABLE Client_Current (
    Clientinfo_id bigint PRIMARY KEY IDENTITY(1,1) NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Sex varchar(255) NOT NULL,
    Language varchar(255) NOT NULL,
    Birthday date NOT NULL,
    Address varchar(255) NOT NULL,
    Address_line2 varchar(255) NULL,
    City varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    Postal_Code varchar(255) NOT NULL,
    Main_Phone varchar(255),
    Office_Phone varchar(255),
    Fax varchar(255),
    Cell_Phone varchar(255),
    Primary_Email varchar(255) NOT NULL,
    Secondary_Email varchar(255),
    Snapshot_time datetime NOT NULL
);

drop table Client_Current;

select * from Client_Current;

delete from Client_Current;

DBCC CHECKIDENT ('Client_Current', reseed,0);
"""


def save_client(cursor, values):
    cursor.executemany(
        "insert into Client_Current values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, getdate())",
        values)
    cursor.commit()


# CURRENT CONTRACT TABLE CREATION
"""
CREATE TABLE Contract_Current (
    Contractinfo_id bigint PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Applicant_last_name varchar(255) NOT NULL,
    Applicant_first_name varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    Postal_code varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    Country varchar(255)  NULL,
    Address_validity varchar(255) NOT NULL,
    Latest_change_of_address date NOT NULL,
    Main_phone varchar(255)  NULL,
    Office_phone varchar(255),NULL,
    Cell_phone varchar(255),NULL,
    Applicant_email varchar(255) NOT NULL,
    Applicant_age int Not NULL,
    Birthday date NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Product varchar(255) NOT NULL,
    Type varchar(255) NOT NULL,
    Contract_start_date date NOT NULL,
    Contract_market_value money NOT NULL,
    Last_update_of_contract_market_value date NOT NULL,
    PAC_amount money NOT NULL,
    PAC_frequency int NULL,
    Day_of_the_PAC date NOT NULL,
    Representative_name varchar(255) NOT NULL,
    District varchar(255) NOT NULL,
    U_S_ varchar(255) NOT NULL,
    Representative_status varchar(255) NOT NULL,
    Source varchar(255) NOT NULL, 
    Snapshot_time datetime NOT NULL
);

drop table Contract_Current;

select * from Contract_Current;

delete from Contract_Current;

DBCC CHECKIDENT ('Contract_Current', reseed,0);
"""


def save_contract(cursor, values):
    cursor.executemany(
        "insert into Contract_Current values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, getdate())",
        values)
    cursor.commit()


# CURRENT TRANSACTION TABLE CREATION
"""
CREATE TABLE Transaction_Current (
    Transactioninfo_ID BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Transaction_Date DATE NOT NULL,
    Transaction_type varchar(255) NOT NULL,
    Fundcode varchar(255) NOT NULL,
    Gross_amount money NOT NULL,
    Units real,
    Unit_value real,
    Snapshot_time datetime NOT NULL,
    CONSTRAINT FK_Contract_number FOREIGN KEY (Contract_number) REFERENCES Contract_Current (Contract_number)
);

drop table Transaction_Current;

select * from Transaction_Current;

delete from Transaction_Current;

DBCC CHECKIDENT ('Transaction_Current', reseed,0);
"""


def save_transaction(cursor, values):
    cursor.executemany("insert into Transaction_Current values (?, ?, ?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()


# CURRENT FUND TABLE CREATION
"""
CREATE TABLE Fund_Current (
    Fund_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Statement_Date DATE NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Account_type varchar(255) NOT NULL,
    Investment_type varchar(255) NOT NULL,
    Category varchar(255) NOT NULL,
    Fund_name varchar(255) NOT NULL,
    Units real NOT NULL,
    Unit_value real NOT NULL,
    Value money NOT NULL,
    ACB money,
    Snapshot_time datetime NOT NULL,
    CONSTRAINT FK_Fund_Contract_number FOREIGN KEY (Contract_number) REFERENCES Contract_Current (Contract_number)
);

drop table Fund_Current;

select * from Fund_Current;

delete from Fund_Current;

DBCC CHECKIDENT ('Fund_Current', reseed,0);
"""


def save_fund(cursor, values):
    cursor.executemany("insert into Fund_Current values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()


# CURRENT PARTICIPANT TABLE CREATION
"""
CREATE TABLE Participant_Current (
    Participant_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Role varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Birthday DATE NOT NULL,
    Snapshot_time DATETIME NOT NULL,
    CONSTRAINT FK_Participant_Contract_number FOREIGN KEY (Contract_number) REFERENCES Contract_Current (Contract_number)
);

drop table Participant_Current;

select * from Participant_Current;

delete from Participant_Current;

DBCC CHECKIDENT ('Participant_Current', reseed,0);
"""


def save_participant(cursor, values):
    cursor.executemany("insert into Participant_Current values (?, ?, ?, ?, getdate())", values)
    cursor.commit()


# CURRENT BENEFICIARY TABLE
"""
CREATE TABLE Beneficiary_Current (
    Bene_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Allocation real NOT NULL,
    Relationship varchar(255) NOT NULL,
    Class varchar(255) NOT NULL,
    Snapshot_time DATETIME NOT NULL,
    CONSTRAINT FK_Beneficiary_Contract_number FOREIGN KEY (Contract_number) REFERENCES Contract_Current (Contract_number)
);
drop table Beneficiary_Current;

select * from Beneficiary_Current;

delete from Beneficiary_Current;

DBCC CHECKIDENT ('Beneficiary_Current', reseed,0);
"""


def save_beneficiary(cursor, values):
    cursor.executemany("insert into Beneficiary_Current values (?, ?, ?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()


# HISTORY SAVING TABLE CREATION
"""
CREATE TABLE Saving_History (
    HiId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    StatementDate DATE NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    AccountType varchar(255) NOT NULL,
    InvestmentType varchar(255) NOT NULL,
    FundCode varchar(255) NULL,
    InvestedDate DATE NULL,
    MaturityDate DATE NULL,
    Amount money NULL,
    Rate real NOT NULL,
    Type varchar(255) NULL,
    Balance money NOT NULL,
    SnapshotTime datetime NOT NULL;

drop table Saving_History;

select * from Saving_History;

delete from Saving_History;

DBCC CHECKIDENT ('Saving_History', reseed,0);
"""


def save_saving_history(cursor, values):
    cursor.executemany("insert into Saving_History values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()


# HISTORY CLIENT TABLE CREATION
"""
CREATE TABLE Client_History (
    Clientinfo_id bigint PRIMARY KEY IDENTITY(1,1) NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Sex varchar(255) NOT NULL,
    Language varchar(255) NOT NULL,
    Birthday date NOT NULL,
    Address varchar(255) NOT NULL,
    Address_line2 varchar(255) NULL,
    City varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    Postal_Code varchar(255) NOT NULL,
    Main_Phone varchar(255),
    Office_Phone varchar(255),
    Fax varchar(255),
    Cell_Phone varchar(255),
    Primary_Email varchar(255) NOT NULL,
    Secondary_Email varchar(255),
    Snapshot_time datetime NOT NULL
);

drop table Client_History;

select * from Client_History;

delete from Client_History;

DBCC CHECKIDENT ('Client_History', reseed,0);
"""


def save_client_history(cursor, values):
    cursor.executemany(
        "insert into Client_History values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, getdate())",
        values)
    cursor.commit()


# HISTORY CONTRACT TABLE CREATION
"""
CREATE TABLE Contract_History (
    Contractinfo_id bigint PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Applicant_last_name varchar(255) NOT NULL,
    Applicant_first_name varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    Postal_code varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    Country varchar(255)  NULL,
    Address_validity varchar(255) NOT NULL,
    Latest_change_of_address date NOT NULL,
    Main_phone varchar(255)  NULL,
    Office_phone varchar(255) NULL,
    Cell_phone varchar(255) NULL,
    Applicant_email varchar(255) NOT NULL,
    Applicant_age int Not NULL,
    Birthday date NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Product varchar(255) NOT NULL,
    Type varchar(255) NOT NULL,
    Contract_start_date date NOT NULL,
    Contract_market_value money NOT NULL,
    Last_update_of_contract_market_value date NOT NULL,
    PAC_amount money NOT NULL,
    PAC_frequency int NULL,
    Day_of_the_PAC date NOT NULL,
    Representative_name varchar(255) NOT NULL,
    District varchar(255) NOT NULL,
    U_S_ varchar(255) NOT NULL,
    Representative_status varchar(255) NOT NULL,
    Source varchar(255) NOT NULL, 
    Record_date Date NOT NULL,
    Snapshot_time datetime NOT NULL
);

drop table Contract_History;

select * from Contract_History;

delete from Contract_History;

DBCC CHECKIDENT ('Contract_History', reseed,0);
"""


def save_contract_history(cursor, values):
    cursor.executemany("insert into Contract_History values "
                       "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, "
                       "getdate())",
                       values)
    cursor.commit()


# HISTORY TRANSACTION TABLE CREATION
"""
CREATE TABLE Transaction_History (
    Transactioninfo_ID BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Transaction_Date DATE NOT NULL,
    Transaction_type varchar(255) NOT NULL,
    Fundcode varchar(255) NOT NULL,
    Gross_amount money NOT NULL,
    Units real,
    Unit_value real,
    Snapshot_time datetime NOT NULL,
    CONSTRAINT FK_Contract_number FOREIGN KEY (Contract_number) REFERENCES Contract_Current (Contract_number)
);

drop table Transaction_History;

select * from Transaction_History;

delete from Transaction_History;

DBCC CHECKIDENT ('Transaction_History', reseed,0);
"""


def save_transaction_history(cursor, values):
    cursor.executemany("insert into Transaction_History values (?, ?, ?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()


# HISTORY FUND TABLE CREATION
"""
CREATE TABLE Fund_History (
    Fund_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Statement_Date DATE NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Account_type varchar(255) NOT NULL,
    Investment_type varchar(255) NOT NULL,
    Category varchar(255) NOT NULL,
    Fund_name varchar(255) NOT NULL,
    Units real NOT NULL,
    Unit_value real NOT NULL,
    Value money NOT NULL,
    ACB money,
    Snapshot_time datetime NOT NULL,
    CONSTRAINT FK_Fund_Contract_number FOREIGN KEY (Contract_number) REFERENCES Contract_Current (Contract_number)
);

drop table Fund_History;

select * from Fund_History;

delete from Fund_History;

DBCC CHECKIDENT ('Fund_History', reseed,0);
"""


def save_fund_history(cursor, values):
    cursor.executemany("insert into Fund_History values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()


# HISTORY PARTICIPANT TABLE CREATION
"""
CREATE TABLE Participant_History (
    Participant_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Role varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Birthday DATE NOT NULL,
    Snapshot_time DATETIME NOT NULL,
    CONSTRAINT FK_Participant_Contract_number FOREIGN KEY (Contract_number) REFERENCES Contract_Current (Contract_number)
);

drop table Participant_History;

select * from Participant_History;

delete from Participant_History;

DBCC CHECKIDENT ('Participant_History', reseed,0);
"""


def save_participant_history(cursor, values):
    cursor.executemany("insert into Participant_History values (?, ?, ?, ?, getdate())", values)
    cursor.commit()


# HISTORY BENEFICIARY TABLE CREATION
"""
CREATE TABLE Beneficiary_History (
    Bene_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Allocation real NOT NULL,
    Relationship varchar(255) NOT NULL,
    Class varchar(255) NOT NULL,
    Snapshot_time DATETIME NOT NULL,
    CONSTRAINT FK_Beneficiary_Contract_number FOREIGN KEY (Contract_number) REFERENCES Contract_Current (Contract_number)
);
drop table Beneficiary_History;

select * from Beneficiary_History;

delete from Beneficiary_History;

DBCC CHECKIDENT ('Beneficiary_History', reseed,0);
"""


def save_beneficiary_history(cursor, values):
    cursor.executemany("insert into Beneficiary_History values (?, ?, ?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()


def delete_current_participant_beneficiary(cursor):
    cursor.execute("exec Delete_Current_Participant_Beneficiary")


def delete_current_contract(cursor):
    cursor.execute("exec Delete_Current_Contract")


def delete_current_fund_saving(cursor):
    cursor.execute("exec Delete_Current_Fund_Saving")


def delete_current_client(cursor):
    cursor.execute("exec Delete_Current_Client")


def delete_current_transaction(cursor):
    cursor.execute("exec Delete_Current_Transaction")


def save_data_into_db(db_cursor, file_name, db_method, batch_size):
    with open(file_name) as f:
        f.readline()  # skip the headers
        data = [tuple(line[1:]) for line in csv.reader(f)]
    # in case of large dataset

    for i in range(-(len(data) // -batch_size)):
        db_method(db_cursor, data[i * batch_size:(i + 1) * batch_size])


def read_clients(db_cursor):
    db_cursor.execute("SELECT * FROM Client_Current")


def save_recover(cursor, values):
    cursor.executemany("insert into Error_contract_number_History values (?, ?, getdate())", values)
    cursor.commit()
