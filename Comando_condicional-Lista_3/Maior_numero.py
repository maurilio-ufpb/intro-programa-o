# Comando condicional - Lista 3

# c. O programa deve receber como entrada três números inteiros e exibir qual
# o maior deles. (Dica: desconsidere a possibilidade de números iguais na
# entrada).

n1= int(input("Informe o número: "))
n2= int(input("Informe o número: "))
n3= int(input("Informe o número: "))
if n1 > n2 and n1 > n3:
    maior= n1
elif n2 > n1 and n2 > n3:
    maior= n2
else:
    maior= n3
print("O maior número é: ", maior)
        
