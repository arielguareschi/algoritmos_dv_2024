#par_impar.py
'''
Solicite para o usuario informar um numero e se
ele quer exibir os numeros pares ou impares.
Com base no numero que ele informar exiba todos os 
numeros pares/impares daquele intervalo.
ex:
Digite um numero:
Exibir pares ou impares? (P ou I)
'''
num = int(input('Digite um numero: '))
opcao = input('Exibir pares ou impares? (P ou I)')

for n in range(1, num + 1):
    if n % 2 == 0:
        if opcao.upper() == 'P':
            print(f'O {n} eh par')
    else:
        if opcao.upper() == 'I':
            print(f'O {n} eh impar')
