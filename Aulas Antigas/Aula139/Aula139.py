import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gabriel",
    password="abc123",
    database="mydatabase"
)

mycursor = mydb.cursor()

# sql = """CREATE TABLE pessoas (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             nome VARCHAR(255), 
#             idade INT(2)
#         )"""

sql = "ALTER TABLE pessoas ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST"

mycursor.execute(sql)
