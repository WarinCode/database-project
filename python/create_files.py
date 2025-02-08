from pandas import read_csv

df = read_csv("../db/data/new_data.csv")

with open("../db/sql/INSERT_STUDENTS.sql", "w", encoding="utf8") as std_file:
    std_file.write("USE DATABASE_PROJECT;\n\n")

    for i in range(4):
        std_name = df.loc[i, "studentName"]
        std_id = df.loc[i, "studentId"]
        email = df.loc[i, "email"]

        std_file.write(f"/* INSERT QUERY NO: {i + 1} */\n")
        std_file.write(f"INSERT INTO Students VALUES({std_id}, '{std_name}', '{email}');\n\n")


with open("../db/sql/INSERT_TRANSACTIONS.sql", "w", encoding="utf8") as trans_file:
    trans_file.write("USE DATABASE_PROJECT;\n\n")

    for j in df.index:
        income = "NULL" if df.loc[j, "income"] == 0 else df.loc[j, "income"]
        expenses = "NULL" if df.loc[j, "expenses"] == 0 else df.loc[j, "expenses"]
        std_id = df.loc[j, "studentId"]

        trans_file.write(f"/* INSERT QUERY NO: {j + 1} */\n")
        trans_file.write(
            f"INSERT INTO Transactions VALUES({income}, {expenses}, {std_id})\n\n"
        )


with open("../db/sql/INSERT_DATETIME_RECORDS.sql", "w", encoding="utf8") as dt_file:
    dt_file.write("USE DATABASE_PROJECT;\n\n")

    for k in df.index:
        datetime = df.loc[k, "datetime"]
        date = df.loc[k, "date"]
        time = df.loc[k, "time"]
        std_id = df.loc[k, "studentId"]

        dt_file.write(f"/* INSERT QUERY NO: {k + 1} */\n")
        dt_file.write(
            f"INSERT INTO DateTime_Records VALUES('{datetime}', '{date}', '{time}', {std_id})\n\n"
        )