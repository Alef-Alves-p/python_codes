import os


"""lista = [10, 20, 30, 40, 50]

lista.append('oi')
lista.pop()
lista.append(1235468)
del lista[-1]
#lista.clear()
lista.insert(0, 5)
#print(len(lista))
print(lista)
"""
"""
lista_a = [1,2,3,4]
lista_b = lista_a.copy()

lista_a[0] = "coisa"

print(lista_a)
print(lista_b)"""

"""
os.system('cls')

lista = ['Maria', 'bob', 'Bento', 'ana']

for nome in lista:
    print(nome, type(nome))
"""

# Desempacotamento e tuplas 
"""os.system('cls')


lista = ['Maria', 'bob', 'Bento', 'ana']

nome1 = lista[0]
nome2 = lista[1]
nome3 = lista[2]
nome4 = lista[3]

print(f"{nome1}, {nome1},{nome1},{nome1},")
print(nome2)
print(nome3)
print(nome4)

"""

#enumerate para enumerar valores de iteráveis
"""os.system('cls')

lista = ['Maria', 'bob', 'Bento', 'ana']"""

"""lista_enumerada = enumerate(lista)
print(next(lista_enumerada))

for i in lista_enumerada:
    print(i)
"""

""" para conseguir executar mais do que um for com enumerate, não devemos
armazena-lo em uma variável e sim passa-lo diretamente no for


"""

# for i in enumerate(lista):
#     print(i)
# conversion type enumerate

"""lista_enumerada = list(enumerate(lista))
print(lista_enumerada)"""


# split e join com list e str
# split - divide uma string
# join - une uma string

"""frase =  "essa frase e, para teste!"
os.system('cls')

lista_frase = frase.split(' ')

for i, frase in enumerate(lista_frase):
    lista_frase[i].strip()


print(lista_frase)


# join
frases_unidas = ''.join(lista_frase)
print(frases_unidas)"""

#lista dentro de listas

"""salas = [
    ['Maria', 'Helena', ],
    ['Elaine', ],
    ['Luiz', 'João', 'Eduarda', ],

]
# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])
os.system('cls')

for sala in salas:
    print(f"a sala é {sala}")
    for aluno in sala:
        print(aluno)"""
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)

#def soma(*args):
#    print(args, type(args))
#
#soma(1,2,3,4,5,6)

#Dicionario

# Métodos uteis dos dicionários em python
# len - quantas chaves
# key - iterável com as chaves
# values - iteráveis com valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe 
# copy - retorna uma cópia rasa ( shallow copy)
# get - obtém a chave 
# pop - apaga um item com a chave especificada (del)
# popitem -  apaga o ultimo item da adicionado
# update - atualiza um dicionario com outro

pessoa = {
    'nome': 'Paulo',
    'sobrenome': 'Gustavo'
}

print(pessoa.setdefault('idade', '29'))
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())


