salario_carlos=float(input("O salario de carlos é:"))
salario_joao=salario_carlos /3

taxa_poupanca=float(input("Digite a taxa poupança:"))

taxa_fundo=float(input("Digite a taxa do fundo:"))


valor_carlos = salario_carlos
valor_joao = salario_joao

meses = 0

while valor_joao < valor_carlos:
    valor_carlos += valor_carlos * taxa_poupanca / 100
    valor_joao += valor_joao * taxa_fundo / 100
    meses += 1
print(f"O valor de joao ultrapasse o valor de carlos {meses}")
