# Faça uma lista de compras usando listas do python
# O usuário deve ter a possibilidade de: inserir, apagar, e listar os valores da lista
# Não permita que o programa quebre com erros de indices inexistentes na lista.

import os


titulo_1 = ("Lista de compras, o que deseja fazer?. \n")
titulo_2 = "[i] - Inserir novo item.\n" "[a] - Apagar item existente.\n" "[l] - Mostrar lista completa.\n""[e] - encerrar programa."

lista_compras = []

while True:
    print(titulo_1)
    print(titulo_2)

    escolha = str(input("Informe sua opção.: "))

    if escolha == 'i':
        os.system('cls')
        novo_item = input("Informe o nome do novo item: ")
        lista_compras.append(novo_item)

        for indice, valor in enumerate(lista_compras):
            print(indice, valor)

        fim_1 = str(input("Item adicionado, deseja adicionar mais itens ou encerrar?: \n""[c] - continuar [f] finalizar: "))
        
        if fim_1 == 'c':
            continue
        else:
            print("lista finalizada!")
            break


    elif escolha == 'a':
        os.system('cls')
        print(lista_compras)

        apagar = input("Qual item deseja apagar da lista ?: ")

        indice = int(apagar)
        del lista_compras[indice]
        print(lista_compras)
                

    elif escolha == 'l':
        os.system('cls')
        if len(lista_compras) <= 0:
            print("lista vazia!")
            continue
        
        for indice, valor in enumerate(lista_compras):
            print(indice, valor)

        fim_3 = str(input("Deseja adicionar mais itens ou encerrar?: \n""[c] - continuar [f] finalizar: "))
        
        if fim_3 == 'c':
            continue
        else:
            print("Por favor, escolha [i], [a] ou [l]")
            continue
    elif escolha == 'e':
        print("Programa encerrado, obrigado!")
        break

    else:
        print("Por favor, escolha [i], [a] ou [l]")
        continue
    









