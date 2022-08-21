import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "Jimmy@123")
#print(mydb)
cursor = mydb.cursor()
#cursor.execute("create database autoconnect")
cursor.execute("show databases")
s = "create table autoconnect.AutoDetails(employee_id int(10), employee_name varchar(80), employee_mailid varchar(40), employee_salary int(8), employee_attendance int(3))"
#cursor.execute(s)
#print(cursor.fetchall())
cursor.execute(s)