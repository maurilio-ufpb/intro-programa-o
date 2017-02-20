
# 10. Faça um algoritmo que leia o tempo de duração de um evento em uma
# fábrica expressa em segundos e mostre-o expresso em horas, minutos e segundos.


quantSegundos= int(input("Informe a quantidade de segundos: "))
horas= quantSegundos//3600
minutos= quantSegundos%3600 // 60
segundos= (quantSegundos - horas*3600 - minutos*60)
print()
print("O tempo é: ",horas,"hora(s)",minutos,"minuto(s)",segundos,"segundo(s)" )
