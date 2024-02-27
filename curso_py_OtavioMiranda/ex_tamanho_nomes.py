"""
Peça ao usuario que informe o nome, se o nome tiver 4 letras ou menos escreva:
seu nome é curto; se tiver 5 ou 6 letras escrvea: seu nome é normal;
maior que 6 letras escreva; seu nome é muito grande.
"""

nome = input('Informe seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto!')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')
