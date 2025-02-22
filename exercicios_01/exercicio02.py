"""Faça um programa que leia uma temperatura em graus Celsius e a converta para Fahrenheit.
A fórmula de conversão é: F = (C X 9/5) + 32"""

print("Informe para que você gostaria de converter: ")
converter_para = (input("Digite - (F) ou (C): "))

"""Erros possíveis"""
numero = len(converter_para)
if(converter_para != 'f' and converter_para != 'c' and numero != 'c'):
    print("Essa letra não é aceita!")

"""Fórmula"""
F = 0
C = 0

if(converter_para == 'c'):
    C = float(input("Informe o valor em C°: "))
    F = (C * 9/5) + 32
    print('O valor de {:.2f} C° em F° é: {:.2f}'.format(C, F))

if(converter_para == 'f'):
    F = float(input("Informe o valor em F°: "))
    C = (F - 32) * 5/9 
    print('O valor de {:.2f} F° em C° é: {:.2f}'.format(F,C))