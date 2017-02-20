# 7. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses
# e dias e mostre-a expressa apenas em dias.


ano= 365
mes= 30

idadeAnos= int(input("Entre com sua idade somente em anos: "))
idadeMes= int(input("Entre com sua idade somente em mes: "))
idadeDias= int(input("Entre com sua idade somente em dias: "))
d= idadeAnos * ano +(idadeMes * mes) + idadeDias
print()
print("Sua idade é:", d,"Dias")


