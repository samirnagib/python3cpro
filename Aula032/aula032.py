nomes = ["Gabriel", "Danny", "Arthur", "João", "Lucas"]
# novaLista = []
# for x in nomes:
#     if "u" in x:
#         novaLista.append(x)

# novaLista = [x for x in nomes if x != "Danny"]
# novaLista = [x for x in nomes if "u" in x]
# novaLista = [x for x in nomes]
# novaLista = [x for x in range(10) if x % 2 != 0]
# novaLista = [x.upper() for x in nomes]
# novaLista = ["Ola" for x in nomes]
novaLista = [x if x != "Danny" else "Danielle" for x in nomes]

print(novaLista)
