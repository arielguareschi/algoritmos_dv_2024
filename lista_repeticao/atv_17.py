'''
 Faça um programa que leia um numero inteiro 
 positivo n e calcule a soma dos n primeiros 
 números naturais.
'''
numero = int(input("Digite um número: "))
soma = 0

for i in range(numero + 1):
    soma += i 

print(f"Soma de todos os numeros de 0 a {numero} é de : {soma}")