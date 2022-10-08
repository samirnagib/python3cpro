usuario = {
    "Nome":"Samir",
    "Sobrenome":"Nagib",
    "Idade":42,
    "Altura": 1.76,
    "Filhos": ["Arthur", "Lucas"],
    "Pets":True
}
print(usuario)
print(usuario["Idade"])
print(len(usuario))

y = usuario.get("Pets")

print(y)

print(usuario.keys() )