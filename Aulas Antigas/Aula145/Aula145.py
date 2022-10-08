import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gabriel",
    password="abc123",
    database="mydatabase"
)

mycursor = mydb.cursor()
# sql = "DROP TABLE pessoas"
sql = "DROP TABLE IF EXISTS pessoas"
mycursor.execute(sql)
