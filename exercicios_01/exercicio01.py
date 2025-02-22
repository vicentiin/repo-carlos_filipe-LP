"""Imprtações"""
import math

"""Primeiramente vamos obter o valor de Pi com (math.pi)"""
P = math.pi

"""Agora iremos obter a variaveL (raio)"""
raio = float(input("Informe o raio do círculo:"))

"""Fórmula"""
area = P * (raio**2)

"""Resposta"""
print('A área do círculo é igual a: {:.2f}'.format(area))
