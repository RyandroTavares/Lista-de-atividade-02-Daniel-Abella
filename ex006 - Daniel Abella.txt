# 06 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi
raio = float(input('Digite o raio do círculo: '))
var = pi * raio ** 2
print()

print('Área do circulo = {:.2f}'.format(var))
