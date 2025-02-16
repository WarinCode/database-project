USE DB_PROJECT;

CREATE TABLE Majors (
    Major_ID VARCHAR(10) PRIMARY KEY NOT NULL,
    Major_Name VARCHAR(50) NULL,
    Programe_Name VARCHAR(50) NULL
)
CREATE TABLE Students (
    Student_ID BIGINT NOT NULL PRIMARY KEY,
    Student_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    Major_ID VARCHAR(10) NOT NULL,
    CONSTRAINT fk_major 
        FOREIGN KEY (Major_ID) 
        REFERENCES Majors(Major_ID)
)
CREATE TABLE Transactions (
    Transaction_ID INT PRIMARY KEY NOT NULL,
    Income FLOAT NULL,
    Expenses FLOAT NULL,    
)
CREATE TABLE Expense_Types (
    Transaction_ID INT PRIMARY KEY NOT NULL, 
    Expense_Type VARCHAR(30) NULL
)
CREATE TABLE Transaction_Timestamps (
    Transaction_ID INT PRIMARY KEY NOT NULL,
    Timestamp DATETIME NOT NULL,
    Date DATE NOT NULL,
    Time TIME NOT NULL
)
CREATE TABLE Student_Transactions (
    Transaction_ID INT PRIMARY KEY NOT NULL,
    Student_ID BIGINT NOT NULL,
    CONSTRAINT fk_transaction 
        FOREIGN KEY (Transaction_ID) 
        REFERENCES Transactions(Transaction_ID),
    CONSTRAINT fk_student
        FOREIGN KEY (Student_ID)
        REFERENCES Students(Student_ID),
    CONSTRAINT fk_transaction_timestamp
        FOREIGN KEY (Transaction_ID)
        REFERENCES Transaction_Timestamps(Transaction_ID),
    CONSTRAINT fk_expense_type
        FOREIGN KEY(Transaction_ID)
        REFERENCES Expense_Types(Transaction_ID)
)