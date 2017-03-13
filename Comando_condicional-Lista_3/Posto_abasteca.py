# Comando condicional - Lista 3

# 2. Pensando no grande número de motoristas que viajam no feriado, o posto de
# combustíveis Abasteça Já resolveu fazer uma super promoção, oferecendo preços
# abaixo do mercado: Além disso, todos os clientes que abastecerem seus veículos
# com mais de 30 litros de etanol serão premiados com uma troca de óleo. Escreva
# um programa para esse posto de modo que ele receba como entrada o combustível
# escolhido e o valor em dinheiro que se deseja gastar, e informe o total de
# combustível abastecido e uma mensagem indicando se o cliente ganhou ou não a
# troca de óleo.


gasolina= 2.53
etanol= 2.09
diesel= 1.92

combustivel= str.upper(input("Qual combustível deseja abastecer: "))
valor= float(input("Qual o valor: "))
if combustivel == "GASOLINA":
    quantLitros= valor/gasolina
    print("A quantidade abastecida foi: %.2f"% litros,"litros")
elif combustivel == "DIESEL":
    litros= valor/diesel
    print("A quantidade abastecida foi: %.2f"% litros,"litros")
elif combustivel == "ETANOL":
    quantLitros= valor/etanol
    print("A quantidade abastecida foi: %.2f"% quantLitros,"litros")
    if quantLitros > 30:
        print("Voce ganhou uma troca de oleo!")
    else:
        print("Voce não ganhou a troca de oleo!")
