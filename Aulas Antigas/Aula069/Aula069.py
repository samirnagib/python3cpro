def nomeCompleto(nome, sobrenome):
    print(nome + " " + sobrenome)

def listaNomes(*nomes):
    for x in nomes:
        print(x)

nomeCompleto("Gabriel", "Artigas")
listaNomes("Gabriel", "Danny", "Arthur")
