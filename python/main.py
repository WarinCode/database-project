from pandas import read_csv
from functions import format_date, format_time

# อ่านข้อมูลไฟล์ csv ได้ dataframe
df = read_csv("../db/data/data.csv")

# แสดงผลข้อมูล
df.info()
print(df.head())

# ลบตอลัมน์แรก
df.drop(columns=["timestamp"], axis=1, inplace=True)

# สร้าง list มาเก็บ date time
date_time = []

# วน loop แก้ไขทีละคอลัมน์
for i in df.index:
    # เปลี่ยนรูปแบบวันที่จาก DD/MM/YYYY เป็น YYYY-MM-DD
    date, month, year = df["date"][i].split("/")
    df.loc[i, "date"] = format_date(date, month, year)

    # แก้ไขเวลาที่เป็นเลข 1 หลักให้เป็น 2 หลักทั้งหมดเช่น 1 เป็น 01
    hours, minutes, seconds = df["time"][i].split(":")
    df.loc[i, "time"] = format_time(hours, minutes, seconds)

    # แก้ไขรูปแบบ timestamp อันเก่าจาก DD/MM/YYYY, HH:MI:SS เป็น YYYY-MM-DD HH:MI:SS
    new_date_time = (
        format_date(date, month, year) + " " + format_time(hours, minutes, seconds)
    )
    date_time.append(new_date_time)

# เพิ่มแถวใหม่
df.insert(0, "datetime", date_time)
print(df.head(10))

# แปลงชนิดข้อมูลของแต่ละคอลัมน์
df[["datetime"]] = df[["datetime"]].astype("datetime64[ms]")
df[["income"]] = df[["income"]].astype("float16")
df[["expenses"]] = df[["expenses"]].astype("float16")
print(df.dtypes)

# ส่งออกเป็นไฟล์ csv อันใหม่
df.to_csv("../db/data/new_data.csv", index=False)
