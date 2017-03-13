# Lista 3 - Comando condicional

# 4. Luzia é fã do Cirque du Soleil e desde que soube que haverá apresentações
# no Brasil, tem mobilizado amigos e familiares para ir.
# Há três tipos de ingresso, dependendo do setor escolhido: platéia VIP
# (R$ 350), cadeira (R$ 200) e arquibancada (R$ 100). Estudantes têm direito
# a 50% de desconto (meia-entrada) em todos os setores, exceto na platéia VIP.
# Também é cobrada uma taxa de conveniência correspondente a 5% do valor do
# ingresso. Escreva um programa que receba como entrada o setor escolhido 
# e o tipo de ingresso (inteira ou meia) e exiba o valor total a ser pago.

plateiaVip= 350
cadeira= 200
arquibancada= 100

setor= str.upper(input("Qual o setor escolhido: "))
tipoIngresso= str.upper(input("Qual tipo de entrada: Inteira ou Meia? "))

if setor != "PLATEIA VIP" and setor != "CADEIRA" and setor != "ARQUIBANCADA":
    print("Opção inválida! Escolha outro setor!")
elif setor == "PLATEIA VIP" and tipoIngresso != "INTEIRA":
    print("Neste setor só Inteira!")
if setor == "PLATEIA VIP":
    taxaConveniencia= plateiaVip * 0.05
    valorIngresso= plateiaVip + taxaConveniencia
    print("O valor do ingresso é: R$ %.2f"% valorIngresso)
elif setor == "CADEIRA" and tipoIngresso == "INTEIRA":
    taxaConveniencia= cadeira * 0.05
    valorIngresso= cadeira + taxaConveniencia
    print("O valor do ingresso é: R$ %.2f"% valorIngresso)
elif setor == "CADEIRA" and tipoIngresso == "MEIA":
    taxaConveniencia= cadeira * 0.05
    valorIngresso= cadeira/2 + taxaConveniencia
    print("O valor do ingresso é: R$ %.2f"% valorIngresso)
elif setor == "ARQUIBANCADA" and tipoIngresso == "INTEIRA":
    taxaConveniencia= arquibancada * 0.05
    valorIngresso= arquibancada + taxaConveniencia
    print("O valor do ingresso é: R$ %.2f"% valorIngresso)
elif setor == "ARQUIBANCADA" and tipoIngresso == "MEIA":
    taxaConveniencia= arquibancada * 0.05
    valorIngresso= arquibancada/2 + taxaConveniencia   
    print("O valor do ingresso é: R$ %.2f"% valorIngresso)
