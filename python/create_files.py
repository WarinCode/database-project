from pandas import read_csv

# อ่านข้อมูล csv อันใหม่ที่ format ข้อมูลเรียบร้อยแล้ว
df = read_csv("../db/data/new_data.csv")

# เขียนไฟล์ insert ข้อมูลสำหรับ table Students 
with open("../db/sql/INSERT_STUDENTS.sql", "w", encoding="utf8") as file:
    file.write("USE DB_PROJECT;\n\n")

    for i in range(4):
        std_name = df.loc[i, "Student_Name"]
        std_id = df.loc[i, "Student_ID"]
        email = df.loc[i, "Email"]
        major_id = df.loc[i, "Major_ID"]
        
        file.write(f"/* INSERT QUERY NO: {i + 1} */\n")
        file.write(f"INSERT INTO Students VALUES({std_id}, '{std_name}', '{email}', '{major_id}');\n\n")

# เขียนไฟล์ insert ข้อมูลสำหรับ table Majors
with open("../db/sql/INSERT_MAJORS.sql", "w", encoding="utf8") as file2:
    file2.write("USE DB_PROJECT;\n\n")

    major_id = df.loc[0, "Major_ID"]
    major_name = df.loc[0, "Major_Name"]
    programe_name = df.loc[0, "Programe_Name"]
            
    file2.write(f"INSERT INTO Majors VALUES('{major_id}', '{major_name}', '{programe_name}');\n")

# เขียนไฟล์ insert ข้อมูลสำหรับ table Transactions
with open("../db/sql/INSERT_TRANSACTIONS.sql", "w", encoding="utf8") as file3:
    file3.write("USE DB_PROJECT;\n\n")

    for j in df.index:
        trans_id = df.loc[j, "Transaction_ID"]
        income = "NULL" if df.loc[j, "Income"] == 0 else df.loc[j, "Income"]
        expenses = "NULL" if df.loc[j, "Expenses"] == 0 else df.loc[j, "Expenses"]

        file3.write(f"/* INSERT QUERY NO: {j + 1} */\n")
        file3.write(
            f"INSERT INTO Transactions VALUES({trans_id}, {income}, {expenses});\n\n"
        )

# เขียนไฟล์ insert ข้อมูลสำหรับ table Transaction_Timestamps
with open("../db/sql/INSERT_TRANSACION_TIMESTAMPS.sql", "w", encoding="utf8") as file4:
    file4.write("USE DB_PROJECT;\n\n")

    for k in df.index:
        trans_id = df.loc[k, "Transaction_ID"]
        timestamp = df.loc[k, "Timestamp"]
        time = df.loc[k, "Time"]
        date = df.loc[k, "Date"]

        file4.write(f"/* INSERT QUERY NO: {k + 1} */\n")
        file4.write(
            f"INSERT INTO Transaction_Timestamps VALUES({trans_id}, '{timestamp}', '{date}', '{time}');\n\n"
        )
        
# เขียนไฟล์ insert ข้อมูลสำหรับ table Student_Transactions
with open("../db/sql/INSERT_STUDENT_TRANSACTIONS.sql", "w", encoding="utf8") as file5:
    file5.write("USE DB_PROJECT;\n\n")
    
    for v in df.index:
        trans_id = df.loc[v, "Transaction_ID"]
        std_id = df.loc[v, "Student_ID"]
        
        file5.write(f"/* INSERT QUERY NO: {v + 1} */\n")
        file5.write(f"INSERT INTO Student_Transactions VALUES({trans_id}, {std_id});\n\n")
       
# เขียนไฟล์ insert ข้อมูลสำหรับ table Expense_Types        
with open("../db/sql/INSERT_EXPENSE_TYPES.sql", "w", encoding="utf8") as file6:
    file6.write("USE DB_PROJECT;\n\n")
    
    for a in df.index:
        trans_id = df.loc[a, "Transaction_ID"]
        ex_type = df.loc[a, "Expense_Type"]
        
        file6.write(f"/* INSERT QUERY NO: {a + 1} */\n")
        file6.write(f"INSERT INTO Expense_Types VALUES({trans_id}, '{ex_type}');\n\n")