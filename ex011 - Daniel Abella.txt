# 11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A • o produto do dobro do primeiro com metade do segundo .
# B • a soma do triplo do primeiro com o terceiro.
# C • o terceiro elevado ao cubo.

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
numero3 = float(input('Digite um número flutuante: '))
a = (numero1 * 2) * (numero2 / 2)
b = (numero1 * 3) + (numero3)
c = numero3 ** 3
print()

print('• O produto do dobro do primeiro com metade do segundo: {}.\n• A soma do triplo do primeiro com o terceiro: {}. \n• O terceiro elevado ao cubo: {}.'.format(a, b, c))