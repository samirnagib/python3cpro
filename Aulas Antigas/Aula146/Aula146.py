import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gabriel",
    password="abc123",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE pessoas SET nome = %s WHERE id = %s"
val = ('Gabriel', '1')

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "registros(s) afetado(s)")
