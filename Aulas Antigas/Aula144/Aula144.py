import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gabriel",
    password="abc123",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM pessoas WHERE id = %s"
val = ('5',)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "registro(s) excluído(s)")
