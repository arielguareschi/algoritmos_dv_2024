# 14.    Faça um programa que leia um número 
# inteiro positivo par N e imprima todos os 
# números pares de 0 até N em ordem decrescente.

num = int(input("Digite um numero: "))

if num >= 0 and num % 2 == 0:
    for i in range(num, 0, -1):
        if(i % 2 == 0):
            print(f"O numero {i} é par")