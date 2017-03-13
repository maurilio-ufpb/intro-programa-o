# Comando condicional - Lista 3

# 3. A viação Rapidinho cobra R$ 350 pelo aluguel de ônibus (capacidade: 42
# pessoas) e R$ 200 por van (capacidade 20 pessoas). Escreva um programa que
# receba como entrada a quantidade de pessoas de uma excursão e exiba a quantidade
# de ônibus e vans que deverão ser alugados e o valor a ser pago por cada pessoa
# da excursão, sabendo que:
# A escolha entre alugar ônibus e vans dependerá da quantidade de pessoas, mas a 
# preferência é que sejam preenchidos primeiro os ônibus, e depois as vans
# necessárias.  A despesa geral será dividida igualmente por todos os participantes,
# não importando quem irá de ônibus ou de van.

aluguelBus= 350
aluguelVan= 200
cpBus= 42
cpVan= 20

quantPessoas= int(input("Informe a quantidade de pessoas: "))
quantBus= quantPessoas//cpBus
sobraBus= quantPessoas%cpBus
quantVan= sobraBus//cpVan
sobraVan= sobraBus%cpVan

if sobraVan > 0:
    quantVan= quantVan + 1
    valorBus= quantBus*aluguelBus
    valorVan= quantVan*aluguelVan
    valorTotal= valorBus+valorVan
    valorPessoa= valorTotal/quantPessoas
print()
print("A quantidade de Onibus é: ", quantBus)
print("A quantidade de Van é: ", quantVan)
print("O valor total da excursão é: R$ %.2f"% valorTotal)
print("O valor por pessoa é: R$ %.2f"% valorPessoa)
