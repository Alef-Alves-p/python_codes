# pedir ao usuario para informar seu nome
# pedir ao usuario para informar sua idade
# se idade e nomne preenchidos
# mostre nome
# nome invertido
# se o nome contem espaços
# numero de letras no nome
# primeira letra do nome
# ultima letra do nome
# caso nada sej aexibido mostre:
# desculpe, você deixou campos vazios!


nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}!')
    print(f'Seu nome invertido fica {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome TEM espaços!')
    else:
        print('Seu nome NÂO tem espaços!')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios!')