
# 5. Escreva um algoritmo que leia 3 números inteiros e mostre o maior deles.

n1= int(input("Digite o primeiro número: "))
n2= int(input("Digite o segundo número: "))
n3= int(input("Digite o terceiro número: "))

def maior():
    if n1 > n2 and n1 > n3:
        print(n1,"É o maior número!!")
    elif n2 > n1 and n2 > n3:
        print(n2,"É o maior número!!")
    elif n3 > n1 and n3 > n2:
        print(n3,"É o maior número!!")
    elif n1 == n2 and n3:
        print("todos os números são iguais!!")
    elif n1 == 0 and n2 == 0 and n3 == 0:
        print("O número é neutro!!")

maior()

