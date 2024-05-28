# 23.    Faça um algoritmo que leia um numero 
# positivo e imprima seus divisores

numero= int(input("Digite um número"))
for i in range(1, numero):
    if numero %i == 0:
        print (i)