CREATE TABLE Client_Current (
    ClientInfoId bigint PRIMARY KEY NONCLUSTERED IDENTITY(1,1) NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Sex varchar(255) NOT NULL,
    Language varchar(255) NOT NULL,
    Birthday date NOT NULL,
    Address varchar(255) NOT NULL,
    AddressLine2 varchar(255),
    City varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    PostalCode varchar(255) NOT NULL,
    MainPhone varchar(255),
    OfficePhone varchar(255),
    Fax varchar(255),
    CellPhone varchar(255),
    PrimaryEmail varchar(255) NOT NULL,
    SecondaryEmail varchar(255),
    ContractNumberAsOwner varchar(255) UNIQUE NOT NULL,
    SnapshotTime datetime NOT NULL
);

CREATE TABLE Contract_Current (
    ContractInfoId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    ApplicantLastName varchar(255) NOT NULL,
    ApplicantFirstName varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    PostalCode varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    Country varchar(255),
    AddressValidity varchar(255) NOT NULL,
    LatestChangeOfAddress DATE NOT NULL,
    MainPhone varchar(255),
    OfficePhone varchar(255),
    CellPhone varchar(255),
    ApplicantEmail varchar(255) NOT NULL,
    ApplicantAge int NOT NULL,
    Birthday date NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    Product varchar(255) NOT NULL,
    Type varchar(255) NOT NULL,
    ContractStartDate date NOT NULL,
    ContractMarketValue money NOT NULL,
    LastUpdateOfContractMarketValue date NOT NULL,
    PACAmount money NOT NULL,
    PACFrequency int,
    DayOfThePAC DATE NOT NULL,
    RepresentativeName varchar(255) NOT NULL,
    District varchar(255) NOT NULL,
    US varchar(255) NOT NULL,
    RepresentativeStatus varchar(255) NOT NULL,
    Source varchar(255) NOT NULL,
    SnapshotTime datetime NOT NULL,
    CONSTRAINT FKContractNumber FOREIGN KEY (ContractNumber) REFERENCES Client_Current (ContractNumberAsOwner)
);

CREATE TABLE Transaction_Current (
    TransactionInfoId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    TransactionDate DATE NOT NULL,
    TransactionType varchar(255) NOT NULL,
    FundCode varchar(255) NOT NULL,
    GrossAmount money NOT NULL,
    Units real,
    UnitValue real,
    SnapshotTime datetime NOT NULL,
    CONSTRAINT FKTransactionContractNumber FOREIGN KEY (ContractNumber) REFERENCES Client_Current (ContractNumberAsOwner)
);

CREATE TABLE Fund_Current (
    FundId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    StatementDate DATE NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    AccountType varchar(255) NOT NULL,
    InvestmentType varchar(255) NOT NULL,
    Category varchar(255) NOT NULL,
    FundName varchar(255) NOT NULL,
    Units real NOT NULL,
    UnitValue real NOT NULL,
    Value money NOT NULL,
    ACB money,
    SnapshotTime datetime NOT NULL
);

CREATE TABLE Saving_Current (
    HiId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    StatementDate DATE NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    AccountType varchar(255) NOT NULL,
    InvestmentType varchar(255) NOT NULL,
    Rate real NOT NULL,
    Balance money NOT NULL,
    SnapshotTime datetime NOT NULL,
    CONSTRAINT FKSavingContractNumber FOREIGN KEY (ContractNumber) REFERENCES Client_Current (ContractNumberAsOwner)
);

CREATE TABLE Participant_Current (
    ParticipantId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    Role varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Birthday DATE NOT NULL,
    SnapshotTime DATETIME NOT NULL,
    CONSTRAINT FKParticipantContractNumber FOREIGN KEY (ContractNumber) REFERENCES Client_Current (ContractNumberAsOwner)
);

CREATE TABLE Beneficiary_Current (
    BeneId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Allocation real NOT NULL,
    Relationship varchar(255) NOT NULL,
    Class varchar(255) NOT NULL,
    SnapshotTime DATETIME NOT NULL,
    CONSTRAINT FKBeneficiaryContractNumber FOREIGN KEY (ContractNumber) REFERENCES Client_Current (ContractNumberAsOwner)
);

CREATE TABLE Client_History (
    ClientInfoId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255) NOT NULL,
    Sex varchar(255) NOT NULL,
    Language varchar(255) NOT NULL,
    Birthday date NOT NULL,
    Address varchar(255) NOT NULL,
    AddressLine2 varchar(255),
    City varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    PostalCode varchar(255) NOT NULL,
    MainPhone varchar(255),
    OfficePhone varchar(255),
    Fax varchar(255),
    CellPhone varchar(255),
    PrimaryEmail varchar(255) NOT NULL,
    SecondaryEmail varchar(255),
    ContractNumberAsOwner varchar(255) NOT NULL,
    SnapshotTime datetime NOT NULL
);

CREATE NONCLUSTERED INDEX IX_ClientHistoryNameBirthday
ON Client_History (LastName, FirstName, Birthday);

CREATE TABLE Contract_History (
    ContractInfoId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    ApplicantLastName varchar(255) NOT NULL,
    ApplicantFirstName varchar(255) NOT NULL,
    City varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    PostalCode varchar(255) NOT NULL,
    Province varchar(255) NOT NULL,
    Country varchar(255),
    AddressValidity varchar(255) NOT NULL,
    LatestChangeOfAddress DATE NOT NULL,
    MainPhone varchar(255),
    OfficePhone varchar(255),
    CellPhone varchar(255),
    ApplicantEmail varchar(255) NOT NULL,
    ApplicantAge int NOT NULL,
    Birthday date NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    Product varchar(255) NOT NULL,
    Type varchar(255) NOT NULL,
    ContractStartDate date NOT NULL,
    ContractMarketValue money NOT NULL,
    LastUpdateOfContractMarketValue date NOT NULL,
    PACAmount money NOT NULL,
    PACFrequency int,
    DayOfThePAC DATE NOT NULL,
    RepresentativeName varchar(255) NOT NULL,
    District varchar(255) NOT NULL,
    US varchar(255) NOT NULL,
    RepresentativeStatus varchar(255) NOT NULL,
    Source varchar(255) NOT NULL,
    SnapshotTime datetime NOT NULL
);

CREATE NONCLUSTERED INDEX IX_ContractHistoryContractNumber
ON Contract_History (ContractNumber);

CREATE TABLE Transaction_History (
    TransactionInfoId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    TransactionDate DATE NOT NULL,
    TransactionType varchar(255) NOT NULL,
    FundCode varchar(255) NOT NULL,
    GrossAmount money NOT NULL,
    Units real,
    UnitValue real,
    SnapshotTime datetime NOT NULL
);

CREATE NONCLUSTERED INDEX IX_TransactionHistoryContractNumber
ON Transaction_History (ContractNumber);

CREATE TABLE Saving_History (
    HiId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    StatementDate DATE NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    AccountType varchar(255) NOT NULL,
    InvestmentType varchar(255) NOT NULL,
    Rate real NOT NULL,
    Balance money NOT NULL,
    SnapshotTime datetime NOT NULL
);

CREATE NONCLUSTERED INDEX IX_SavingHistoryContractNumber
ON Saving_History (ContractNumber);

CREATE TABLE Fund_History (
    FundId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    StatementDate DATE NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    AccountType varchar(255) NOT NULL,
    InvestmentType varchar(255) NOT NULL,
    Category varchar(255) NOT NULL,
    FundName varchar(255) NOT NULL,
    Units real NOT NULL,
    UnitValue real NOT NULL,
    Value money NOT NULL,
    ACB money,
    SnapshotTime datetime NOT NULL
);

CREATE NONCLUSTERED INDEX IX_FundHistoryContractNumber
ON Fund_History (ContractNumber);


CREATE TABLE Participant_History (
    ParticipantId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    Role varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Birthday DATE NOT NULL,
    SnapshotTime DATETIME NOT NULL
);

CREATE NONCLUSTERED INDEX IX_ParticipantHistoryContractNumber
ON Participant_History (ContractNumber);

CREATE TABLE Beneficiary_History (
    BeneId BIGINT PRIMARY KEY IDENTITY(1,1) NOT NULL,
    ContractNumber varchar(255) NOT NULL,
    Name varchar(255) NOT NULL,
    Allocation real NOT NULL,
    Relationship varchar(255) NOT NULL,
    Class varchar(255) NOT NULL,
    SnapshotTime DATETIME NOT NULL
);

CREATE NONCLUSTERED INDEX IX_BeneficiaryHistoryContractNumber
ON Beneficiary_History (ContractNumber);

-- drop table Beneficiary_Current, Beneficiary_History, Client_Current, Client_History, Fund_Current, Fund_History, Participant_Current, Participant_History,
-- Saving_Current, Saving_History, Transaction_Current, Transaction_History;
-- drop table Contract_Current, Contract_History;

drop table Beneficiary_Current, Beneficiary_History, Client_Current, Client_History, Fund_Current, Fund_History, Participant_Current, Participant_History,
Saving_Current, Saving_History, Transaction_Current, Transaction_History;
drop table Contract_Current, Contract_History;