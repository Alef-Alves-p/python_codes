
    if entrada in palavra_sec:
        letras_acertadas += entrada

    palavra_formada = ''
    for letra_sec in palavra_sec:
        if letra_sec in letras_acertadas:
            palavra_formada += letra_sec
        else:
            palavra_formada += "*"

    print(" a palavra secreta era: ", palavra_formada)

    if palavra_formada == palavra_sec:
        print("Você acertou, parabéns!")
        print(" a palavra secreta era: ", palavra_formada)
        print("Tentativas", tentativas)

