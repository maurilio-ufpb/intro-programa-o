# Comando condicional - Lista 2

# 3. Escreva um programa que receba como entrada três números e exiba uma
# mensagem informando qual é o maior deles. (Dica: desconsidere a entrada de
# números iguais)

n1= int(input("Informe o número: "))
n2= int(input("Informe o número: "))
n3= int(input("Informe o número: "))
if n1 > n2 and n1 > n3:
    maior= n1
elif n2 > n1 and n2 > n3:
    maior= n2
else:
    maior= n3
print("O maior número é:",maior)
        
