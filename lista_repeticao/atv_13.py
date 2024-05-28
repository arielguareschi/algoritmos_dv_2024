 #13.    Faça um programa que leia um numero 
 # inteiro positivo par N e imprima todos os 
 # números pares de 0 até N em ordem crescente.
 
numeros =  int(input("Escreva os números desejados"))

if numeros >=0: 
    for i in  range (numeros):
        if i %2==0: 
            print (f"O seu número é=, {i}")