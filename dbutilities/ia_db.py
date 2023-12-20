# HIGH INTEREST TABLE CREATION
"""
CREATE TABLE Saving_Current (
    HI_id BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Statement_Date DATE NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Account_type varchar(255) NOT NULL,
    Investment_type varchar(255) NOT NULL,
    Rate real NOT NULL,
    Balance money NOT NULL,
    Snapshot_time datetime NOT NULL,
    CONSTRAINT FK_Saving_Contract_number FOREIGN KEY (Contract_number) REFERENCES Contract_Current (Contract_number)
);

drop table Saving_Current;

select * from Saving_Current;

delete from Saving_Current;

DBCC CHECKIDENT ('Saving_Current', reseed,0);
"""
def save_saving(cursor, values):
    cursor.executemany("insert into Saving_Current values (?, ?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()


# CLIENT TABLE CREATION
"""
CREATE TABLE Client_Current (
    Clientinfo_id bigint PRIMARY KEY IDENTITY(1,1) NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Sex varchar(255) NOT NULL,
    Language varchar(255) NOT NULL,
    Birthday date NOT NULL,
    Address varchar(255) NOT NULL,
    Address_line2 varchar(255) NOT NULL,
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
    cursor.executemany("insert into Client_Current values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()

"""
CREATE TABLE Contract_Current (
    Contractinfo_id bigint PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Applicant_last_name varchar(255) NOT NULL,
    Applicant_first_name varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    Postal_code varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    Country varchar(255) NOT NULL,
    Address_validity varchar(255) NOT NULL,
    Latest_change_of_address varchar(255) NOT NULL,
    Main_phone varchar(255) NOT NULL,
    Office_phone varchar(255),
    Cell_phone varchar(255),
    Applicant_email varchar(255) NOT NULL,
    Applicant_age int Not NULL,
    Birthday date NOT NULL,
    Contract_number varchar(255) NOT NULL,
    Product varchar(255) NOT NULL,
    Type varchar(255) NOT NULL,
    Contract_start_date varchar(255) NOT NULL,
    Contract_market_value money NOT NULL,
    Last_update_of_contract_market_value date NOT NULL,
    PAC_amount money NOT NULL,
    PAC_frequency int,
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
def save_fund(cursor, values):
    print("leyi branch")

    pass