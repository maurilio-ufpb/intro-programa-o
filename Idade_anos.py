
# 8. Faça um algoritmo que leia a idade de uma pessoa expressa em dias e
# mostre-a expressa em anos, meses e dias.


quantDias= int(input("Informe a quantidade de dias: "))
idadeAnos= quantDias//365
idadeMes= quantDias%365 // 30
idadeDias= (quantDias - idadeAnos*365- idadeMes*30)
print()
print("A idade é: ",idadeAnos,"ano(s)",idadeMes,"mes(es)",idadeDias,"dia(s)" )
