
# 15. Escrever um algoritmo que lê um valor em reais e calcula qual o menor
# número possível de notas de 100, 50, 10, 5 e 1 em que o valor lido pode ser
# decomposto. Escrever o valor lido e a relação de notas necessárias.

# cd = cédulas 

valor= int(input("Informe o valor e ser sacado: "))
print()
print("O valor solicitado foi: R$ %.2f"%valor)
print()
if valor != 100:
    cd100= valor//100
    resto= valor%100
    print(cd100, "Cédulas de 100")
if valor >= 50:
    cd50= resto//50
    resto= resto%50
    print(cd50, "Cédulas de 50")
if valor >= 20:
    cd20= resto//20
    resto= resto%20
    print(cd20, "Cédulas de 20")
if valor >= 10:
    cd10= resto//10
    resto= resto%10
    print(cd10, "Cédulas de 10")
if valor >= 5:
    cd5= resto//5
    resto= resto%5
    print(cd5, "Cédulas de 5")
if valor >= 1:
    cd1= resto//1
    resto= resto%1
    print(cd1, "Cédulas de 1")
    
   
