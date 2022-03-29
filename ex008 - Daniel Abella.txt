# 08 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# • Calcule e mostre o total do seu salário no referido mês

hora = float(input('Digite a quantidade ganho em horas: '))
mes = float(input('Digite a quantidade de horas trabalhadas por mês: '))
total = hora * mes
print()

print('Ganhando R$ {} por hora e trabalhando {} horas por mês\nE ganhando R$ {} por mês'.format(hora, mes, total))