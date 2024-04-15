# Contando frequencia de uma letra em uma frase

frase = 'O Python é uma linguagem de programação'\
    'multiparadigma' \
    'Python foi criada po Guido Van Rossum'
contagem_letra = {}

i = 0
while i < len(frase):
    letra = frase[i]
    if letra.isalpha():
        if letra in contagem_letra:
            contagem_letra[letra] += 1
        else:
            contagem_letra[letra] = 1

    i += 1

if contagem_letra:  # Verifica se há letras na contagem
    letra_mais_comum = max(contagem_letra, key=contagem_letra.get)
    quantidade_mais_comum = contagem_letra[letra_mais_comum]

    print(f"A letra mais comum é '{letra_mais_comum}' com {quantidade_mais_comum} ocorrências.")
else:
    print("A frase não contém letras.")
