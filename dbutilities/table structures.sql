CREATE TABLE Client_Current (
    Clientinfo_id bigint PRIMARY KEY NONCLUSTERED IDENTITY(1,1) NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Sex varchar(255) NOT NULL,
    Language varchar(255) NOT NULL,
    Birthday date NOT NULL,
    Address varchar(255) NOT NULL,
    AddressLine2 varchar(255),
    City varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    Postal_Code varchar(255) NOT NULL,
    Main_Phone varchar(255),
    Office_Phone varchar(255),
    Fax varchar(255),
    Cell_Phone varchar(255),
    Primary_Email varchar(255) NOT NULL,
    Secondary_Email varchar(255),
    Contract_number_as_owner varchar(255) UNIQUE NOT NULL,
    Snapshot_time datetime NOT NULL
);

CREATE TABLE Contract_Current (
    Contractinfo_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Applicant_last_name varchar(255) NOT NULL,
    Applicant_first_name varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    Postal_code varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    Country varchar(255),
    Address_validity varchar(255) NOT NULL,
    Latest_change_of_address DATE NOT NULL,
    Main_phone varchar(255),
    Office_phone varchar(255),
    Cell_phone varchar(255),
    Applicant_email varchar(255) NOT NULL,
    Applicant_age int NOT NULL,
    Birthday date NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Product varchar(255) NOT NULL,
    Type varchar(255) NOT NULL,
    Contract_start_date date NOT NULL,
    Contract_market_value money NOT NULL,
    Last_update_of_contract_market_value date NOT NULL,
    PAC_amount money NOT NULL,
    PAC_frequency int,
    Day_of_the_PAC DATE NOT NULL,
    Representative_name varchar(255) NOT NULL,
    District varchar(255) NOT NULL,
    U_S_ varchar(255) NOT NULL,
    Representative_status varchar(255) NOT NULL,
    Source varchar(255) NOT NULL,
    Snapshot_time datetime NOT NULL
);

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
    CONSTRAINT FK_Contract_number FOREIGN KEY (Contract_number) REFERENCES Client_Current (Contract_number_as_owner)
);

CREATE TABLE Saving_Current (
    HI_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Statement_Date DATE NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Account_type varchar(255) NOT NULL,
    Investment_type varchar(255) NOT NULL,
    Rate real NOT NULL,
    Balance money NOT NULL,
    Snapshot_time datetime NOT NULL,
    CONSTRAINT FK_Saving_Contract_number FOREIGN KEY (Contract_number) REFERENCES Client_Current (Contract_number_as_owner)
);

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
    CONSTRAINT FK_Fund_Contract_number FOREIGN KEY (Contract_number) REFERENCES Client_Current (Contract_number_as_owner)
);

CREATE TABLE Participant_Current (
    Participant_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Role varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Birthday DATE NOT NULL,
    Snapshot_time DATETIME NOT NULL,
    CONSTRAINT FK_Participant_Contract_number FOREIGN KEY (Contract_number) REFERENCES Client_Current (Contract_number_as_owner)
);

CREATE TABLE Beneficiary_Current (
    Bene_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Allocation real NOT NULL,
    Relationship varchar(255) NOT NULL,
    Class varchar(255) NOT NULL,
    Snapshot_time DATETIME NOT NULL,
    CONSTRAINT FK_Beneficiary_Contract_number FOREIGN KEY (Contract_number) REFERENCES Client_Current (Contract_number_as_owner)
);

CREATE TABLE Client_History (
    Clientinfo_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Sex varchar(255) NOT NULL,
    Language varchar(255) NOT NULL,
    Birthday date NOT NULL,
    Address varchar(255) NOT NULL,
    Address_line2 varchar(255),
    City varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    Postal_Code varchar(255) NOT NULL,
    Main_Phone varchar(255),
    Office_Phone varchar(255),
    Fax varchar(255),
    Cell_Phone varchar(255),
    Primary_Email varchar(255) NOT NULL,
    Secondary_Email varchar(255),
    Contract_number_as_owner varchar(255) NOT NULL,
    Snapshot_time datetime NOT NULL
);

CREATE NONCLUSTERED INDEX IX_Client_History_name_birthday
ON Client_History (LastName, FirstName, Birthday);

CREATE TABLE Contract_History (
    Contractinfo_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Applicant_last_name varchar(255) NOT NULL,
    Applicant_first_name varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    Postal_code varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    Country varchar(255),
    Address_validity varchar(255) NOT NULL,
    Latest_change_of_address DATE NOT NULL,
    Main_phone varchar(255),
    Office_phone varchar(255),
    Cell_phone varchar(255),
    Applicant_email varchar(255) NOT NULL,
    Applicant_age int NOT NULL,
    Birthday date NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Product varchar(255) NOT NULL,
    Type varchar(255) NOT NULL,
    Contract_start_date date NOT NULL,
    Contract_market_value money NOT NULL,
    Last_update_of_contract_market_value date NOT NULL,
    PAC_amount money NOT NULL,
    PAC_frequency int,
    Day_of_the_PAC DATE NOT NULL,
    Representative_name varchar(255) NOT NULL,
    District varchar(255) NOT NULL,
    U_S_ varchar(255) NOT NULL,
    Representative_status varchar(255) NOT NULL,
    Source varchar(255) NOT NULL,
    Snapshot_time datetime NOT NULL
);

CREATE NONCLUSTERED INDEX IX_Contract_History_Contract_number
ON Contract_History (Contract_number);

CREATE TABLE Transaction_History (
    Transactioninfo_ID BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Transaction_Date DATE NOT NULL,
    Transaction_type varchar(255) NOT NULL,
    Fundcode varchar(255) NOT NULL,
    Gross_amount money NOT NULL,
    Units real,
    Unit_value real,
    Snapshot_time datetime NOT NULL
);

CREATE TABLE Saving_History (
    HI_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Statement_Date DATE NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Account_type varchar(255) NOT NULL,
    Investment_type varchar(255) NOT NULL,
    Rate real NOT NULL,
    Balance money NOT NULL,
    Snapshot_time datetime NOT NULL
);


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
    Snapshot_time datetime NOT NULL
);


CREATE TABLE Participant_History (
    Participant_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Role varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Birthday DATE NOT NULL,
    Snapshot_time DATETIME NOT NULL
);

CREATE TABLE Beneficiary_History (
    Bene_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Allocation real NOT NULL,
    Relationship varchar(255) NOT NULL,
    Class varchar(255) NOT NULL,
    Snapshot_time DATETIME NOT NULL
);
-- drop table Beneficiary_Current, Beneficiary_History, Client_Current, Client_History, Fund_Current, Fund_History, Participant_Current, Participant_History,
-- Saving_Current, Saving_History, Transaction_Current, Transaction_History;
-- drop table Contract_Current, Contract_History;

drop table Beneficiary_Current, Beneficiary_History, Client_Current, Client_History, Fund_Current, Fund_History, Participant_Current, Participant_History,
Saving_Current, Saving_History, Transaction_Current, Transaction_History;
drop table Contract_Current, Contract_History;