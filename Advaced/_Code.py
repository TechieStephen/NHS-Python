# import mysql.connector as connector
# from student import *
#
# db_conn = connector.connect(
#   host ="localhost",
#   user="python",
#   password="1234",
#   database="schoolDB"
# )
# db_cursor = db_conn.cursor()
# '''
# student1 = Student("James Alex", 28, "Python")
# student2 = Student("Ada Ada", 23, "C#")
# student3 = Student("Semi Lola", 24, "Flutter")
#
# query = "INSERT INTO students (name, age, class) VALUES(%s, %s, %s)"
# val = [
# (student1.name, student1.age, student1.student_class),
# (student2.name, student2.age, student2.student_class),
# (student3.name, student3.age, student3.student_class)
# ]
# db_cursor.executemany(query, val)
# db_conn.commit()
#
# print(db_cursor.rowcount, "was inserted")
#
# '''
# query = "SELECT * FROM students"
# db_cursor.execute(query)
# records = db_cursor.fetchall()
#
# java_records = []
# python_records = []
# flutter_records = []
#
# for record in records:
#   if record[3] == 'Python':
#     python_records.append(record)
#   elif record[3] == 'Flutter':
#     flutter_records.append(record)
#   elif record[3] == 'Java':
#     java_records.append(record)
#   else:
#     continue
#
# #print(db_cursor.rowcount, "records found")
#
# print("Java Records")
# print(java_records)
# print("-----------------")
#
# print("Python Records")
# print(python_records)
# print("-----------------")
#
# print("Flutter Records")
# print(flutter_records)
# print("-----------------")
# '''
#
# db_conn.close()
# db_cursor.execute("show databases")
# for database in db_cursor:
#   print(database)
#
# '''
#
#
# def showLogin():
#   login = tk.Tk()
#   login.title('LOGIN')
#   login.geometry('200x200')
#   tk.Button(login, text='show Home').pack()
#   login.mainloop()

from tkinter import *

x = StringVar() # Holds a string; default value ""
x = IntVar() # Holds an integer; default value 0
x = DoubleVar() # Holds a float; default value 0.0
x = BooleanVar() # Holds a boolean, returns 0 for False and 1 for True
