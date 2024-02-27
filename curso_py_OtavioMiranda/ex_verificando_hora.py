"""
Faça um programa que pergunte as horas ao usuario, baseando-se no horario informado
exiba a saudação de acordo com a hora: ex.
Bom dia 0-11, boa tarde 12-17, boa noite 18-23
"""

horario = int(input("Informe as horas: "))

if horario >= 0 and horario <= 11:
    print('Bom dia...!')
elif horario >= 12 and horario <= 17:
    print('Boa tarde...!')
elif horario >= 17 and horario <= 23:
    print('Boa noite...!')
else:
    print('Horario desconhecido!')