import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gabriel",
    password="abc123",
    database="mydatabase"
)

mycursor = mydb.cursor()

# sql = "ALTER TABLE pessoas ADD sobrenome VARCHAR(255)"
# sql = "ALTER TABLE pessoas DROP sobrenome"
# sql = "ALTER TABLE pessoas ADD sobrenome VARCHAR(255) FIRST"
sql = "ALTER TABLE pessoas ADD sobrenome VARCHAR(255) AFTER nome"

mycursor.execute(sql)
