# WORKING WITH TABLES IN MYSQL

''''''
'''
INSERT INTO A TABLE
To fill a table in MySQL, use the "INSERT INTO" statement.

Insert a record in the "students" table:

///CODE
import mysql.connector
db_conn = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

db_cursor = db_conn.cursor()

query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
db_cursor.execute(query, val)

db_conn.commit()

print(db_cursor.rowcount, "record inserted.")
///

NOTE: Notice the statement: mydb.commit(). It is required to make 
the changes, otherwise no changes are made to the table.
'''