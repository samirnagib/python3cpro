def nomes(primeiro, segundo, terceiro):
    print("O Primeiro nome é", primeiro)
    print("O Segundo nome é", segundo)
    print("O Terceiro nome é", terceiro)

nomes(segundo="Gabriel", terceiro="Danny", primeiro="Arthur")

def nomeCompleto(**nome):
    print(nome)
    for x in nome.values():
        print(x)

nomeCompleto(pri="Gabriel", seg="Silva", ter="Santos")