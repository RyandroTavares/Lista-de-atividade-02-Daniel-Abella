# 09 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# • C = 5 * ((F-32) / 9).

F = float(input('Digite a temperatura em Fahrenheit: '))
C = 5 * ((F-32) / 9)
print()

print('Temperatura em {}°F convertido para °C {:.2f}'.format(F, C))