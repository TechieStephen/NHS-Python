# WORKING WITH MYSQL DATABASE
'''
in this class we are going to learn how to access and
work with MySQL database.

TO GET STARTED PLEASE DOWNLOAD ANY OF THE FOLLOWING
- MySQL database sever
- XAMPP
- WAMP

NEXT we need to install a driver which would enable us
connect to our database.

we are going to be using MySQL Connector
so we need to install it using pip

/// PIP command
python -m pip install mysql-connector
///

--this would install mysql connector which would serve as
our driver to access the MySQL database.


-------------------------------------------------------
GETTING STARTED
- After install MySQL Connector lets import it
to see if our installation was successful

///Code
import mysql.connector
///

Now lets create a connection to our database server

///Code
import mysql.connector

db_conn = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(db_conn)
///

-------------------------------------------------------
CREATE A DATABASE IN THE SERVER
///CODE
import mysql.connector

db_conn = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

db_cursor = db_conn.cursor()

db_cursor.execute("CREATE DATABASE student")
///

'''



'''
-------------------------------------------------------
CHECK FOR EXISTING DATABASES

You can check if a database exist by listing all databases in your system by using 
the "SHOW DATABASES" statement:

///CODE
import mysql.connector

db_conn = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

db_cursor = db_conn.cursor()
db_cursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
///


-------------------------------------------------------
YOU CAN ALSO TRY CONNECTING TO A DATABASE TO KNOW IF IT EXISTS
///CODE
import mysql.connector

db_conn = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)
///

NOTE: If the database does not exist, you will get an error.

  
'''