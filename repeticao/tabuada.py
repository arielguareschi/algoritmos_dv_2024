#tabuada.py
# agora faça a tabuada do 
# 1 até a do 95, indo cada uma do
# 1 ao 10, com no maximo mais 1 linha
# de código

for tabuada in range(1, 180):
    if tabuada % 2 == 0:
        continue
    if tabuada == 3:
        break
    print(f"=;= TABUADA DO {tabuada} =;=")
    for mult in range(1, 11):
        if mult % 2 == 0:
            continue
        print(f'{mult} x {tabuada} = {mult * tabuada}')
    print("=====================")
    
print("ACABOUUUUU")