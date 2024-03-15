# Desenvolva uma aplicação Python que
# solicite para o usuário informar o seu nome
# e ano de nascimento, após os dois dados serem 
# informados retorne para o usuário qual a 
# sua idade
# Exemplo: 
# Digite o seu nome: Tibursio
# Digite o ano de nascimento: 1990
# Tibursio você tem 34 anos

nome = input('Digite o seu nome: ')
nascimento = int(input('Digite o seu nascimento: '))

idade = 2024 - nascimento

print(f'{nome} tem {idade} de idade')
