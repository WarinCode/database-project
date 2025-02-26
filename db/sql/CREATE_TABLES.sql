USE DB_PROJECT;

CREATE TABLE Majors (
    Major_ID VARCHAR(10) PRIMARY KEY NOT NULL,
    Major_Name VARCHAR(50) NULL,
    Program_Name VARCHAR(50) NULL
);
CREATE TABLE Students (
    Student_ID BIGINT NOT NULL PRIMARY KEY,
    Student_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    Major_ID VARCHAR(10) NULL,
    CONSTRAINT fk_major FOREIGN KEY (Major_ID) REFERENCES Majors (Major_ID)
);
CREATE TABLE Transactions (
    Timestamp DATETIME NOT NULL,
    Student_ID BIGINT NOT NULL,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Income FLOAT NULL,
    Expenses FLOAT NULL,
    Expesnse_Type VARCHAR(50) NULL,
    CONSTRAINT fk_student FOREIGN KEY (Student_ID) REFERENCES Students (Student_ID)
)