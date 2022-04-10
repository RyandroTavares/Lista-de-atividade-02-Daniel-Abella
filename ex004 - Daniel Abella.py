# 04 Faça um Programa que peça as 4 notas bimestrais e mostre a média

nota1 = float(input('Digite sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))
nota3 = float(input('Digite sua nota 3: '))
nota4 = float(input('Digite sua nota 4: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print()

print('Sua média é igual a {:.2f}!'.format(media))