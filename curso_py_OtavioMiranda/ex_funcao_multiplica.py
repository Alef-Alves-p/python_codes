# Crie uma função que multiplica todos os argumentos
# nao nomeados recebidos
# Retorne o total para uma variável e mostre
# o Valor da variável

def multiplica(*args):
    for n in args:
        return f'O total multiplicado é: {n}'

print(multiplica(5*50*70))


# Crie função que fala se o numero é par ou impar
# Retorne se o numero e par ou impar

def par_impar(n):
    if n % 2 == 0:
        return f'O numero {n} é Par'
    return f'O numero {n} é Impar'

print(par_impar(3))
