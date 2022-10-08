import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gabriel",
    password="abc123",
    database="mydatabase"
)

mycursor = mydb.cursor()
# sql = "SELECT * FROM pessoas ORDER BY nome"
# sql = "SELECT * FROM pessoas ORDER BY nome ASC"
sql = "SELECT * FROM pessoas ORDER BY nome DESC"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
