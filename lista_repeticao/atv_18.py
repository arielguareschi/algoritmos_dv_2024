18.	#Escreva um algoritmo que leia certa 
#quantidade de números e imprima o maior
# deles e quantas vezes o maior numero foi lido.
# A quantidade de números a serem lidos deve ser 
# fornecida pelo usuário.

QN= int (input (' digite quantos numeros vao ser lidos:'))
maior = 0
qtd_maior = 0
menor = 0

for i in range ( 0, QN):
    valor = int (input("digite um numero"))
    if(valor >= maior):
        maior = valor
        qtd_maior += 1     
    if(valor <= menor or menor == 0):
        menor = valor 
        
print(f"O maior numero {maior}, apareceu {qtd_maior} e o menor foi {menor}")