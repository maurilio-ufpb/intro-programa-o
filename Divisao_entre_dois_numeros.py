
# 1. Construa um algoritmo que compute o resultado e resto da divisão entre
# dois números.
        
num1= int(input("Informe o Dividendo: "))
num2= int(input("Informe o divisor: "))
if num2 == 0:
    print("ERRO! O divisor não pode ser zero! ")

else:
    resultado= num1//num2
    resto= num1%num2
    print("O resultado da divisão é: ""%.f"% resultado)
    print("O resto da divisão é: ""%.f"% resto)
