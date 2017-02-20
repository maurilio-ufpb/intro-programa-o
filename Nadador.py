
# 14. Elabore um algoritmo que dada a idade de um nadador classifica-o em uma
# das seguintes categorias:
# • infantil A = 5 - 7 anos
# • infantil B = 8-10 anos
# • juvenil A = 11-13 anos
# • juvenil B = 14-17 anos
# • adulto = maiores de 18 anos

idade= int(input("Informe a idade do nadador: "))
if idade >= 5 and idade < 7:
    print("Infantil A!")
if idade >= 8 and idade < 10:
    print("Infantil B!")
if idade >= 11 and idade < 13:
    print("Juvenil A!")
if idade >= 14 and idade < 17:
    print("Juvenil B!")
if idade >= 18:
    print("Adulto!")
