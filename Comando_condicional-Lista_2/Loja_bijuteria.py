# Comando condicional - Lista 2

# 5. Natália abriu uma loja de bijuterias recentemente e as vendas vão muito
# bem. Pensando em atrair uma clientela ainda maior, ela deseja oferecer um
# desconto de 10% para os clientes que gastarem R$ 100 ou mais e pagarem em
# dinheiro. Escreva um programa que receba como entrada o valor do produto
# comprado e a forma de pagamento escolhida (dinheiro ou cheque), calcule o
# desconto devido (caso necessário), e exiba o valor final a ser pago.

valorProd= float(input("Qual o valor: "))
formaPag= str.upper(input("Qual forma de pagamento: Dinheiro ou Cheque? "))
if formaPag != "DINHEIRO" and formaPag != "CHEQUE":
    print("Opção inválida!")
else:
    if formaPag == "DINHEIRO" and valorProd >= 100:
        valorProd= valorProd * 0.9
    print("O valor a pagar é: R$ %.2f"% valorProd)
