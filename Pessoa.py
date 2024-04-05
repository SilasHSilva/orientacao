class Pessoa:
    "Isto é uma nova classe chamada Pessoa"
    
    idade = 15
    
    def saudacao(self):
        print("Olá Pessoas!!!")

print(Pessoa.idade)
print(Pessoa.saudacao) #Não funciona pois precisa instanciar um objeto


objetoPessoa = Pessoa()

objetoPessoa.saudacao()
print(objetoPessoa.idade)