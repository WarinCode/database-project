# ส่งโปรเจควิชา Fundamentals of Database Systems

### รายละเอียดโปรเจค
โปรเจคนี้ได้จัดทำเก็บข้อมูลประจำวันของสมาชิกในกลุ่มเกี่ยวกับรายรับรายจ่ายในชีวิตประจำวันได้ 100 รายการ เพื่อนำข้อมูลที่ได้เก็บบันทึกไว้ใน ฐานข้อมูล SQL Server

แบบฟอร์มที่บันทึก: [Google Forms](https://forms.gle/4unjYZPNaUYVH3N39)

ภาพ ER-diagram ออกแบบฐานข้อมูล
![ER-diagram](/imgs/ER-diagram.png)

---

### ขั้นตอนการนำโปรเจคไปพัฒนาต่อ
เปิด Terminal แล้วทำตามขั้นตอนต่อไปนี้

clone ตัวโปรเจค
```
git clone https://github.com/WarinCode/database-project.git
```

เข้าไปยัง directory
```
cd database-project
```

สร้าง environment
```
py -m venv env
```

ติดตั้ง libraries
```
pip install -r requirements.txt
```

activatate ตัวสภาพแวดล้อมที่เราสร้าง
```
env/Scripts/activate
```

ถ้าต้องการเขียนโค้ด python ให้สร้างไฟล์ที่ directory `python`
รันไฟล์ python
```
py python/<ชื่อไฟล์ที่สร้าง>.py
```

---


### ขั้นตอนสำหรับการนำข้อมูลไปใส่ในฐานข้อมูล SQL Server
1. ให้ติดตั้งโปรแกรม SQL Server และ Microsoft SQL Server Management Studio ให้เรียบร้อย
2. เปิดไฟล์ `CREATE_DATABASE.sql` ไฟล์นี้จะอยู่ใน directory `db/sql` directory นี้ไว้เก็บไฟล์ sql ในโปรเจคนี้ทั้งหมด
3. รันไฟล์นั้นเพื่อสร้าง database
4. เปิดไฟล์ `CREATE_TABLES.sql` แล้วรันไฟล์นี้เพื่อสร้าง tables
5. สร้าง tables สำเร็จแล้วต่อไปจะเป็นการแทรกข้อมูลเข้าไปใน tables ที่เราสร้างให้เปิดไฟล์แล้วรันไฟล์ต่อไปนี้ตามลำดับ
6. รันไฟล์แรก `INSERT_MAJORS.sql`, รันไฟล์ที่ 2 `INSERT_STUDENTS.sql`, รันไฟล์ที่ 3 `INSERT_TRANSACTIONS.sql`, รันไฟล์ที่ 4 `INSERT_EXPENSE_TYPES.sql`, รันไฟล์ที่ 5 `INSERT_TRANSACION_TIMESTAMPS.sql`, รันไฟล์สุดท้าย `INSERT_STUDENT_TRANSACTIONS.sql`
7. ทำตามขั้นตอนที่ 6 เสร็จก็จะเพิ่มข้อมูลเข้า tables ครบหมดแล้ว หากติดปัญหาเพิ่มข้อมูลไม่ได้ให้ลบ tables ทั้งหมดแล้วเริ่มใหม่ทำตามขั้นตอนตามลำดับ
8. เช็คข้อมูลว่ามาไหมให้ลองคลิกเช็คขวาแล้วเลือก select top 1000

---

### สมาชิกในกลุ่ม
1. นาย ปัณณวัฒน์ นิ่งเจริญ รหัสนิสิต 6630250231
2. นาย พันธุ์ธัช สุวรรณวัฒนะ รหัสนิสิต 6630250281
3. นาย วรินทร์ สายปัญญา รหัสนิสิต 6630250435
4. นาย ปุณณภพ มีฤทธิ์ รหัสนิสิต 6630250591
