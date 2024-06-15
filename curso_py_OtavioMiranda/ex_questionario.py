# crie um sistema de perguntas e respostas com python

perguntas = [

    {
        'Pergunta': 'Quanto é 4 * 5 ? ',
        'Opções': ['16', '24', '35', '20'],
        'Resposta': '20',
    },
    {
        'Pergunta': 'Quanto é 12 / 3 ? ',
        'Opções': ['6', '4', '3', '0'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 40 - 15 ? ',
        'Opções': ['25', '24', '15', '30'],
        'Resposta': '25',


    },
]

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    qtd_opcoes = pergunta['Opções']
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)
        print()

    escolha = input('Escolha uma opção: ')
    if escolha == enumerate(pergunta['Opções']):
        print('Acertou!')
