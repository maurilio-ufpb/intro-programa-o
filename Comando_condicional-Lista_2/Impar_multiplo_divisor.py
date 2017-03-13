# # Comando condicional - Lista 2

# 4. Escreva um programa que receba como entrada um número e exiba mensagens
# informando:
# - Se ele é ímpar
# - Se ele é múltiplo de 3
# - Se ele é divisor de 102
# Lembrete: Um número é múltiplo de três se o resto de sua divisão por três for
# zero. Um número é divisor de 102 caso a divisão de 102 por esse número tenha
# resto zero.

num= int(input("Informe o número: "))
if num%2 != 0:
    print("O número é Impar!")
else:
    print("O número não é Impar!")
if num%3 == 0:
    print("O número é multiplo de 3!")
else:
    print("O número não é múltiplo de 3!")
if 102%num == 0:
    print("O número é divisor de 102!")
else:
    print("O número não é divisor de 102!")
