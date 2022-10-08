import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gabriel",
    password="abc123",
    database="mydatabase"
)

mycursor = mydb.cursor()
# sql = "SELECT * FROM pessoas WHERE sobrenome = 'Logan'"
# sql = "SELECT * FROM pessoas WHERE id = '4'"
# sql = "SELECT * FROM pessoas WHERE idade > '30'"
# sql = "SELECT * FROM pessoas WHERE sobrenome LIKE '%ga%'"

sql = "SELECT * FROM pessoas WHERE sobrenome = %s"
sobrenome = ("Logan",)

mycursor.execute(sql, sobrenome)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
