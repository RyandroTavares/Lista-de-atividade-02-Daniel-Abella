# 15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# • salário bruto.
# • quanto pagou ao INSS.
# • quanto pagou ao sindicato.
# • o salário líquido.
# • calcule os descontos e o salário líquido, conforme a tabela à direita.

hora = float(input('Digite quanto ganha por hora: R$ '))
mes = float(input('Digite quantas horas trabalha por mês: '))
total = hora * mes
ir = total * 0.11
inss = total * 0.8
sindicato = total * 0.5
print()

print('Salário bruto: R$ ', total)
print('Quanto pagou ao imposto de renda IR: R$ ', ir)
print('Quanto pagou ao INSS: R$ ', inss)
print('Quanto pagou ao sindicato: R$ ', sindicato)
print('O salário líquido: R$ ', total)