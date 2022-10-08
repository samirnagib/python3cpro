import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gabriel",
    password="abc123",
    database="mydatabase"
)

mycursor = mydb.cursor()
# sql = "SELECT * FROM pessoas LIMIT 5"
sql = "SELECT * FROM pessoas LIMIT 5 OFFSET 2"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
