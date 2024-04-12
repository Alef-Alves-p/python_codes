#Calculadora com while
#Calculadora com while
print("Informe dois números e um operador ( +, -, *, / ) para realizar um calculo aritmético")
print()

while True:
    num1 = float(input("informe um numero: "))
    num2 = float(input("informe outro numero: "))

    operador = input("Informe um operador: ")

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("ERRO, operador inválido, informe um dos operadores permitidos ->(+ - / *)")
        continue
    if num1 == '' and num2 == '':
        print("ERRO, deve ser informado pelo menos um numero para o calculo!")
        continue
    elif operador == '':
        print("ERRO, operador não informado!")
        operador
        continue
    print("realizando o calculo, confira o resultado abaixo!")
    if operador == '+':
        print(f"O resultado da soma é: {num1} + {num2} = {num1+num2}")
    elif operador == '-':
        print(f"O resultado da subtração é: {num1} - {num2} = {num1-num2}")
    elif operador == '/':
        print(f"O resultado da divisão é: {num1} / {num2} = {num1/num2}")
    elif operador == '*':
        print(f"O resultado da multiplicação é: {num1} * {num2} = {num1*num2}")
    saida = input("Deseja encerrar ou realizar um novo calculo?\ndigite [s] para sair ou [n] para um novo calculo!: ")
    if saida == 's':
        print("Obrigado!")
        break
