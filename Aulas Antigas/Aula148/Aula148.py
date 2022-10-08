import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="gabriel",
    password="abc123",
    database="mydatabase"
)

mycursor = mydb.cursor()
# sql = """
# SELECT 
#     usuarios.nome AS nome, produtos.nome AS favorito
#     FROM usuarios
#     INNER JOIN produtos ON usuarios.fav = produtos.id
# """

# sql = """
# SELECT 
#     usuarios.nome AS nome, produtos.nome AS favorito
#     FROM usuarios
#     LEFT JOIN produtos ON usuarios.fav = produtos.id
# """
sql = """
SELECT 
    usuarios.nome AS nome, produtos.nome AS favorito
    FROM usuarios
    RIGHT JOIN produtos ON usuarios.fav = produtos.id
"""
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
