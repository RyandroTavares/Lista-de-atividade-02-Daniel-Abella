# 13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# • Para homens: (72.7*h) –58
# • Para mulheres: (62.1*h) -44.7

altura = float(input('Digite sua altura para saber o peso ideal: '))
PH = (72.7 * altura) - 58
PM = (62.1 * altura) - 44.7
print()

print('O seu peso ideal caso seja Homen {:.3f}!\nO seu peso ideal caso seja Mulher {:.3f}!'.format(PH, PM))