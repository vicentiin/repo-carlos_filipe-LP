"""Recolhendo dados"""
horas = float(input("Informe o número de horás trabalhadas no mês: "))
valor = float(input("Informe o valor recebido por cada hóra: "))

"""Resultado"""
resultado = horas * valor

print('O salário que você ganhou no mês foi de {:.2f}'.format(resultado))