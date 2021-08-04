# WORKING WITH TABLES IN MYSQL
''''''
'''
CHECK FOR EXISTING TABLES
You can check if a table exist by listing all tables in your database 
with the "SHOW TABLES" statement:

///CODE
import mysql.connector

db_conn = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

db_cursor = db_conn.cursor()
db_cursor.execute("SHOW TABLES")

for x in db_cursor:
  print(x)

/// 
  

-------------------------------------------------------
CREATE A TABLE IN A DATABASE

To create a table in MySQL, use the "CREATE TABLE" statement.
Make sure you define the name of the database when you create the connection

When creating a table, you should also create a column with a unique key for each record.

This can be done by defining a PRIMARY KEY.

We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique 
number for each record. Starting at 1, and increased by one for each record.

Create a table named "students":

///CODE
import mysql.connector

db_conn = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

db_cursor = db_conn.cursor()
db_cursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age VARCHAR(255), , class VARCHAR(255)))")
///


NOTE:
________________________________________________________________
If the table already exists, use the ALTER TABLE keyword:
Create primary key on an existing table:

///Code
import mysql.connector

db_conn = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

db_cursor = db_conn.cursor()

db_cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
///
________________________________________________________________


import mysql.connector

db_conn = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="1234",
  database="test"
)

db_cursor = db_conn.cursor()
db_cursor.execute("SELECT * FROM student")
result = db_cursor.fetchall()

for x in result:
  print(x)
  
'''