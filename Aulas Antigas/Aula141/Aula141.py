import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gabriel",
    password="abc123",
    database="mydatabase"
)

mycursor = mydb.cursor()
# sql = "SELECT * FROM pessoas"
sql = "SELECT nome,idade FROM pessoas"

mycursor.execute(sql)

# myresult = mycursor.fetchone()
# print(myresult)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
