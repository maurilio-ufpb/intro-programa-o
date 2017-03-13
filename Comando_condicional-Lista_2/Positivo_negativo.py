# Comando condicional - Lista 2

# 1. Escreva um programa que receba como entrada um número e exiba uma mensagem
# informando se ele é positivo, negativo ou neutro.

num= int(input("Informe o número: "))
if num > 0:
    print("O número é Positivo!")
elif num < 0:
    print("O número é Negativo!")
else:
    print("O número é Neutro!")
