import mysql.connector as conn
DbConn = conn.connect(
    host="localhost",
    user="python",
    password="1234",
    database = "instagram"
)
cursor = DbConn.cursor()
# query = "CREATE DATABASE instagram"
# query = "SHOW DATABASES"
# query = '''
# CREATE TABLE users(
# 	user_id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(30) NOT NULL,
#     password VARCHAR(30) NOT NULL,
#     email VARCHAR(30) NOT NULL
# )
# '''

#INSERT A RECORD
query = '''
INSERT INTO users(username, password, email, phone_number) 
VALUES (%s, %s, %s, %s)
'''

name = 'karma007'
pwd = '111111'
email = 'karma@gmail.com'
phone_number = '07023645641'

values = (name, pwd,email,phone_number)
cursor.execute(query, values)
DbConn.commit()
print(cursor.rowcount, 'rows inserted')
