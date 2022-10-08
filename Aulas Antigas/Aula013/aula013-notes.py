import os
os.system('cls') or None
texto = "  Cidade de Lyman, localizada em Donetsk e controlada pela Rússia desde maio, é estratégica e um importante centro ferroviário  "
palavras = ["Cidade", "de ", "Lyman","localizada","em", "Donetsk", "e", "controlada", "pela", "Rússia", "desde", "maio", "é", "estratégica", "e um", "importante", "centro", "ferroviário"]

for x in texto:
    print(x)
os.system('cls') or None
for y in palavras:
    print(y)
    
print("Palavras")
print(len(palavras))

print("texto")
print(len(texto))

print(texto.upper())

print(texto.lower())

print(texto.strip())
print(texto.replace("r","*").upper())
print(texto.split(","))