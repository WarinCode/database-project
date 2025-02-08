USE DABASE_PROJECT;

CREATE TABLE Students (
    Student_ID BIGINT NOT NULL PRIMARY KEY,
    Student_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(50) NOT NULL,
)

CREATE TABLE Transactions(
    Income FLOAT NULL,
    Expenses FLOAT NULL,
    Student_ID BIGINT NOT NULL,

	CONSTRAINT fk_transaction
        FOREIGN KEY(Student_ID)
        REFERENCES Students(Student_ID),
)

CREATE TABLE DateTime_Records (
    DT DATETIME NOT NULL,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Student_ID BIGINT NOT NULL,

	CONSTRAINT fk_datetime
        FOREIGN KEY(Student_ID)
        REFERENCES Students(Student_ID)
)

