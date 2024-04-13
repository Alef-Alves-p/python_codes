# Contando frequencia de uma letra em uma frase

frase = 'O Python é uma linguagem de programação'\
    'multiparadigma' \
    'Python foi criada po Guido Van Rossum'
contagem_letras = {}

i = 0
while i < len(frase):
    letra = frase[i]
    if letra.isalpha():
        if letra in contagem_letras:
            contagem_letras[letra] += 1
        else:
            contagem_letras[letra] = 1
    i += 1

if contagem_letras:  # Verifica se há letras na contagem
    letra_mais_comum = max(contagem_letras, key=contagem_letras.get)
    quantidade_mais_comum = contagem_letras[letra_mais_comum]

    print(f"A letra mais comum é '{letra_mais_comum}' com {quantidade_mais_comum} ocorrências.")
else:
    print("A frase não contém letras.")

"""