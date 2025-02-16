USE DB_PROJECT;

SELECT
    Students.Student_ID,
    MAX(Income) AS MAX_INCOME,
    MAX(Expenses) AS MAX_EXPENSES,
    AVG(Income) AS Average_Income,
    AVG(Expenses) AS Average_Expenses
FROM
    Students
    INNER JOIN Student_Transactions ON Student_Transactions.Student_ID = Students.Student_ID
    INNER JOIN Transactions ON Transactions.Transaction_ID = Student_Transactions.Transaction_ID
WHERE 
    Students.Student_ID = 6630250435
GROUP BY Students.Student_ID;