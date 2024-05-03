# salario.py
"""
    Quero verificar em qual faixa de contribuicao 
    do inss o salario informado se enquadra.
    de     0,00 até 1.412,00 -  7,5%
    de 1.412,01 até 2.666,68 -  9,0%
    de 2.666,69 até 4.000,03 - 12,0%
    de 4.000,04 até 7.786,02 - 14,0%
    acima de 7.786,03        - R$ 908,85 
"""
salario = float(input('Digite o salario: '))
aliquota = 0.0

if salario <= 1412.0:
    aliquota = 7.5
else:
    if salario >= 1412.01 and salario <= 2666.68:
        aliquota = 9.0
    else:
        if salario >= 2666.69 and salario <= 4000.03:
            aliquota = 12.0
        else:
            if salario >= 4000.04 and salario <= 7786.02:
                aliquota = 14.0
            else:
                valor = 908.85

if salario <= 1412.0:
    aliquota = 7.5
elif salario >= 1412.01 and salario <= 2666.68:
    aliquota = 9.0
elif salario >= 2666.69 and salario <= 4000.03:
    aliquota = 12.0
elif salario >= 4000.04 and salario <= 7786.02:
    aliquota = 14.0
else:
    valor = 908.85
    
if aliquota != 0:
    valor = salario * aliquota / 100

texto = f'''
O funcionario X tem o salario de R$ {salario:.2f}
Vai pagar de INSS R$ {valor:10.2f}
Vai receber R$ {(salario-valor):.2f}
'''
#print(texto)

'''
Base de cálculo ANUAL
Base de Cálculo (R$)	Alíquota (%)
De R$ 24.511,93 até R$ 33.919,80	7,5%
De R$ 33.919,81 até R$ 45.012,60	15,0%
De R$ 45.012,61 até R$ 55.976,16	22,5%
Acima de R$ 55.976,16	27,5%

A base de calculo é o salario já deduzido o INSS
'''
salario_anual = (salario-valor) * 12

if salario_anual >= 24511.93 and salario_anual <= 33919.80:
    aliquota_ir = 7.5
elif salario_anual >= 33919.81 and salario_anual <= 45012.60:
    aliquota_ir = 15
elif salario_anual >= 45012.61 and salario_anual <= 55976.16:
    aliquota_ir = 22.5
elif salario_anual >= 55976.17:
    aliquota_ir = 27.5
else:
    aliquota_ir = 0
    
base_ir = salario - valor
valor_ir = base_ir * aliquota_ir / 100

texto += f'''
Aliquota do IR {aliquota_ir}%
Valor deducao IR R$ {valor_ir}
Salario final a receber R$ {base_ir - valor_ir}
'''
print(texto)
