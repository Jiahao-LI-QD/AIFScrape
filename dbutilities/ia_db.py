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

def save_fund(cursor, values):
    print("leyi branch")

    pass