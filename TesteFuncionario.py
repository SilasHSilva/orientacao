'''
    Criação de objetos e chamadas dos métodos
'''

from Funcionario import Funcionario


funcionario = Funcionario('Antonio', 'Tonho@ymail.com')

print(funcionario)

funcionario.cadastro_hora("Jan", 200)
funcionario.cadastro_hora("Feb", 230)
funcionario.cadastro_salario_hora("Jan", 250)
funcionario.cadastro_salario_hora("Feb", 250)
print(funcionario.calcular_salario('Jan'))
print(funcionario)
print(funcionario.calcular_salario('Feb'))
print(funcionario)
