# HIGH INTEREST TABLE CREATION
"""
create table investment_high_interest (
    HI_id bigint IDENTITY(1,1) PRIMARY KEY,
    _Date date not null,
    contract_number varchar(10) not null ,
    account_type varchar(10) not null ,
    investment_type varchar(50) not null,
    rate real not null,
    balance money not null,
    snapshot_time datetime not null
);

drop table investment_high_interest;

select * from investment_high_interest;

delete from investment_high_interest;

DBCC CHECKIDENT ('investment_high_interest', reseed,0);
"""
def save_hi(cursor, values):
    cursor.executemany("insert into investment_high_interest values (?, ?, ?, ?, ?, ?, getdate())", values)
    cursor.commit()

def save_fund(cursor, values):
    print("Eva branch")

    pass