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

