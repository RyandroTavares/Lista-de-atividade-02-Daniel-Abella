# 07 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

altura = float(input('Digite a altura do quadrado: '))
largura = float(input('Digite a largura do quadrado: '))
area = altura * largura
dobro = area * 2
print()

print('A área do quadrado é {:.2f}! e o dobro {:.2f}'.format(area, dobro))