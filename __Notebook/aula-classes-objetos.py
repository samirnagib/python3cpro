class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
    
    def nomeCompleto(self):
        print(self.nome, self.sobrenome)
    

#Herança
class Estudante(Pessoa):
    def __init__(self, nome, sobrenome):
        super().__init__(nome,sobrenome)

p2 = Estudante("Samir", "Nagib")
p2.nomeCompleto()
