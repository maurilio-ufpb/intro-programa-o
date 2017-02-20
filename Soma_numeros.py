
# 4. Construa um algoritmo que compute a soma dos números inteiros de 1 até N.

soma= 0
num= int(input("Informe o numero: "))

for i in range(1,num):
    soma= soma + i
    print(soma)
