# CURRENT SAVING TABLE CREATION
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
#CURRENT FUND TABLE CREATION

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
    cursor.executemany("insert into Fund_Current values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()
def save_fund(cursor, values):
    print("leyi branch")

    pass