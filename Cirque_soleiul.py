# 4. Luzia é fã do Cirque du Soleil e desde que soube que haverá apresentações
# no Brasil, tem mobilizado amigos e familiares para ir. Ela já pesquisou
# informações sobre transporte e ingressos, e agora precisa organizar o
# orçamento da viagem.
# Há três tipos de ingresso, dependendo do setor escolhido: platéia VIP (R$ 350),
# cadeira (R$ 200) e arquibancada (R$ 100). Estudantes têm direito a 50% de
# desconto (meia-entrada) em todos os setores, exceto na platéia VIP. Também é
# cobrada uma taxa de conveniência correspondente a 5% do valor do ingresso.

# Escreva um programa que receba como entrada o setor escolhido e o tipo de
# ingresso (inteira ou meia) e exiba o valor total a ser pago.


plateiaVip= 350
cadeira= 200
arquibancada= 100

setor= str.upper(input("Informe o setor: "))
ingresso= str.upper(input("Qual o tipo de ingresso: INTEIRA ou MEIA? "))

if setor == "CAMAROTE":
    print("opção inválida! Escolha outro setor: ")
elif setor == "PLATEIA VIP" and ingresso == "MEIA":
    print("Neste setor a entrada é só INTEIRA! ")
elif setor == "PLATEIA VIP":
    taxaConveniencia= plateiaVip * 5/100
    valorIngresso= plateiaVip + taxaConveniencia
    print("O valor do ingresso é: R$ %.2f "% valorIngresso)
elif setor == "CADEIRA" and ingresso == "INTEIRA":
    taxaConveniencia= cadeira * 5/100
    valorIngresso= cadeira + taxaConveniencia
    print("O valor do ingresso é: R$ %.2f "% valorIngresso)
elif setor == "CADEIRA" and ingresso == "MEIA":
    taxaConveniencia= cadeira * 5/100
    valorIngresso= cadeira/2 + taxaConveniencia
    print("O valor do ingresso é: R$ %.2f "% valorIngresso)
elif setor == "ARQUIBANCADA" and ingresso == "INTEIRA":
    taxaConveniencia= arquibancada * 5/100
    valorIngresso= arquibancada + taxaConveniencia
    print("O valor do ingresso é: R$ %.2f "% valorIngresso)
elif setor == "ARQUIBANCADA" and ingresso == "MEIA":
    taxaConveniencia= arquibancada * 5/100
    valorIngresso= arquibancada/2 + taxaConveniencia
    print("O valor do ingresso é: R$ %.2f "% valorIngresso)
