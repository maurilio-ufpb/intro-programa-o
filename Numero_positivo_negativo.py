
# 6. Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando
# se este número é par ou ímpar, e se é positivo ou negativo.

num= int(input("Informe o número: "))
if num%2 == 0:
    print("O número é par! ")
else:
    print("O número é impar! ")
if num >= 0:
    print("O número é positivo! ")
else:
    print("O número é negativo! ")
