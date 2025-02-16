USE DB_PROJECT;

SELECT
    Students.Student_ID,
    Timestamp,
    Income,
    Expenses
FROM
    Students
    INNER JOIN Student_Transactions ON Student_Transactions.Student_ID = Students.Student_ID
    INNER JOIN Transactions ON Transactions.Transaction_ID = Student_Transactions.Transaction_ID
    INNER JOIN Transaction_Timestamps ON Transaction_Timestamps.Transaction_ID = Transactions.Transaction_ID
WHERE
    Students.Student_ID = 6630250435
    AND Date BETWEEN '2025-01-11' AND '2025-01-20'
ORDER BY
    Expenses DESC;