"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

import os

palavra_sec = 'dialogo'
letras_acertadas = ''
numero_tentativas = 0

while True:    
    entrada = input("Digite uma letra: ")
    numero_tentativas += 1

    if len(entrada) > 1:
        print("Digite uma letra por vez!")
        continue

    if entrada in palavra_sec:
        letras_acertadas += entrada

    palavra_formada = ''
    for letra_sec in palavra_sec:
        if letra_sec in letras_acertadas:
            palavra_formada += letra_sec
        else:
            palavra_formada += "*"

    print("Palavra formada: ", palavra_formada)

    if palavra_formada == palavra_sec:
        os.system('cls')
        print("VOCÊ GANHOU, PARABÉNS!")
        print(" palavra secreta era: ", palavra_sec)
        print("Tentativas",  numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0