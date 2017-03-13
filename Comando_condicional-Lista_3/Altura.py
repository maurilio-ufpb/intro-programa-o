# Comando condicional - Lista 3

# 1. Para cada problema a seguir, analise se a solução apresentada é a mais
# indicada. Caso não seja, explique porque e reescreva o código fazendo as
# mudanças necessárias.

# b. O programa deve receber como entrada a altura de uma pessoa e exibir uma
# mensagem informando se ela é de estatura baixa, mediana ou alta.


altura= float(input("Informe a altura: "))
if altura <= 1.40:
    print("Estatura Baixa")
elif altura < 1.65:
    print("Estatura Média")
else:
    print("Estatura Alta")
