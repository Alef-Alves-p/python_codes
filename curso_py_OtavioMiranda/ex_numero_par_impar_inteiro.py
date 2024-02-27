"""
faça um programa que peça ao usuario para digitar um numero inteiro
informe se o numero é par ou impar. Caso o usuario nao informe um numero
inteiro, informe que não é um numero inteiro.
"""

numero = input("Informe um numero inteiro: ")

if numero.isnumeric():
    intnum = int(numero)
    print(f'O numero informado foi {numero}, ele é um numero INTEIRO')

    if intnum % 2 == 0:
        print(f'E o numero {numero} é um numero PAR!')
    else:
        print(f'E o numero {numero} é um numero IMPAR!')
else:
    print(f'O numero {numero} informado não é um numero inteiro!')
