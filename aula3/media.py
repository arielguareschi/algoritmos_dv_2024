# Solicite para o usuário digitar duas notas,
# b1 e b2, imprima se o aluno foi aprovado ou
# reprovado.
# Considere que a media de aprovacao é 7.0
# e para o calculo da média utilize a
# média aritmética simples.

nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))

# media = (nota1 + nota2)/2

if ((nota1 + nota2)/2) >= 7:
    print('Aprovado')
else:
    print('Reprovado')
