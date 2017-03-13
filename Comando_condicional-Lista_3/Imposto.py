# Comando condicional - Lista 3

# 1. Para cada problema a seguir, analise se a solução apresentada é a mais
# indicada. Caso não seja, explique porque e reescreva o código fazendo as
# mudanças necessárias.

# a. O programa deve receber como entrada a renda anual de uma pessoa e exibir
# o imposto total a ser pago. Quem ganha até 12000 fica isento, quem ganha mais
# de 60000 paga 7% desse valor, e os demais pagam 3% do valor total.

renda= float(input("Informe a renda anual: "))
if renda <= 12000:
    imposto= 0
elif renda > 60000:
    imposto= renda * 0.07
else:
    imposto= renda * 0.03
print("O imposto a pagar é: R$ %.2f"%
      imposto)
