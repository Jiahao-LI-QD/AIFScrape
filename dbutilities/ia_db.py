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
def save_fund(cursor, values):
    print("leyi branch")

    pass