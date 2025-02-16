from pandas import read_csv
from functions import format_date, format_time, format_date_time

# อ่านข้อมูลไฟล์ csv ได้ dataframe
df = read_csv("../db/data/data.csv")

# แสดงผลข้อมูล
df.info()
print(df.head())

# วน loop แก้ไขทีละคอลัมน์
for i in df.index:
    # เปลี่ยนรูปแบบวันที่จาก DD/MM/YYYY เป็น YYYY-MM-DD
    date, month, year = df["Date"][i].split("/")
    df.loc[i, "Date"] = format_date(date, month, year)

    # แก้ไขเวลาที่เป็นเลข 1 หลักให้เป็น 2 หลักทั้งหมดเช่น 1 เป็น 01
    hours, minutes, seconds = df["Time"][i].split(":")
    df.loc[i, "Time"] = format_time(hours, minutes, seconds)

    # # แก้ไขรูปแบบ timestamp อันเก่าจาก DD/MM/YYYY, HH:MI:SS เป็น YYYY-MM-DD HH:MI:SS
    df.loc[i, "Timestamp"] = format_date_time(year, month, date, hours, minutes, seconds)

    # # เพิ่มข้อมูลในคอลัมน์ Expense_Type, Major_ID, Major_Name, Programe_Name, Transaction_ID
    df.loc[i, "Expense_Type"] = "ค่าใช้จ่ายพื้นฐาน"
    df.loc[i, "Major_ID"] = "S06"
    df.loc[i, "Major_Name"] = "วิทยาการคอมพิวเตอร์"
    df.loc[i, "Programe_Name"] = "พิเศษ"
    df.loc[i, "Transaction_ID"] = i + 1
    
# แก้ไขชนิดของคอลัมน์
df[["Transaction_ID"]] = df[["Transaction_ID"]].astype("int")
df[["Income"]] = df[["Income"]].astype("float")
df[["Expenses"]] = df[["Expenses"]].astype("float")
df[["Date"]] = df[["Date"]].astype("object")
df[["Time"]] = df[["Time"]].astype("object")
df[["Timestamp"]] = df[["Timestamp"]].astype("object")

# # ส่งออกเป็นไฟล์ csv อันใหม่
df.to_csv("../db/data/new_data.csv", index=False)