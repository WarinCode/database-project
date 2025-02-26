from pandas import read_csv
from functions import get_null

# อ่านข้อมูล csv อันใหม่ที่ format ข้อมูลเรียบร้อยแล้ว
df = read_csv("../db/data/new_data.csv")

# เขียนไฟล์ insert ข้อมูลสำหรับ table Students
with open("../db/sql/INSERT_STUDENTS.sql", "w", encoding="utf8") as file:
    file.write("USE DB_PROJECT;\n\n")

    for i in range(4):
        std_name = df.loc[i, "Student_Name"]
        std_id = df.loc[i, "Student_ID"]
        email = df.loc[i, "Email"]
        major_id = 'S06'

        file.write(f"/* INSERT QUERY NO: {i + 1} */\n")
        file.write(
            f"INSERT INTO Students VALUES({std_id}, '{std_name}', '{email}', '{major_id}');\n\n"
        )

# เขียนไฟล์ insert ข้อมูลสำหรับ table Transactions
with open("../db/sql/INSERT_TRANSACTIONS.sql", "w", encoding="utf8") as file2:
    file2.write("USE DB_PROJECT;\n\n")

    for j in df.index:
        timestamp = df.loc[j, "Timestamp"]
        std_id = df.loc[j, "Student_ID"]
        date = df.loc[j, "Date"]
        time = df.loc[j, "Time"]
        income = get_null(df.loc[j, "Income"])
        expenses = get_null(df.loc[j, "Expenses"])
        expense_type = "NULL" if get_null(df.loc[j, "Expense_Type"]) == "NULL" else f"'{df.loc[j, "Expense_Type"]}'"
        
        file2.write(f"/* INSERT QUERY NO: {j + 1} */\n")
        file2.write(
            f"INSERT INTO Transactions VALUES('{timestamp}', {std_id}, '{date}', '{time}', {income}, {expenses}, {expense_type});\n\n"
        )

with open("../db/sql/INSERT_MAJORS.sql", "w", encoding="utf8") as file3:
    file3.write("USE DB_PROJECT;\n\n")
    
    major_id = df.loc[104, "Major_ID"]
    major_name = df.loc[104, "Major_Name"]
    program_name = df.loc[104, "Program_Name"]
    file3.write(f"INSERT INTO Majors VALUES({major_id}, '{major_name}', '{program_name}');")