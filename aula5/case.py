# case.py
opcao = 5

match opcao:
    case 1:
        print('digitou 1')
    case 2:
        print('digitou 2')
    case _:
        print('digitou qualquer coisa')
