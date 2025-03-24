
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="practice")

mycursor = mydb.cursor()

sql = "INSERT INTO students (Name,Roll_no) VALUES (%s, %s)"
val = ("Ram", 85)

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount,"record inserted.")