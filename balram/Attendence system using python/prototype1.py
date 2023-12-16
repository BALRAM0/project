import pyqrcode
import png
import sqlite3

comm=sqlite3.connect("students.db")
cur=comm.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS students(rollnumber int)')
query='''Insert into students values(1000)'''
cur.execute(query)
result = cur.execute("SELECT * FROM students")
data=result.fetchall()
s=''
for i in data:
    s+=str(i)
print(s)

s=pyqrcode.create(s)
s.png('myqr.png', scale = 6)