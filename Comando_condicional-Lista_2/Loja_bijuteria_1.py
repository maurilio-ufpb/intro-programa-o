# Comando condicional - Lista 2

# 6. Passados seis meses, a loja de Natália teve um crescimento surpreendente e
# agora ela vai aceitar pagamentos também com cartão. O cliente poderá escolher
# entre as funções débito e crédito do cartão, e ainda parcelar sua compra em
# até 3 vezes na opção crédito. Modifique o programa anterior para que as novas
# formas de pagamento sejam consideradas e, além do valor final a ser pago, seja
# exibido o valor de cada parcela nas compras com cartão de crédito.

valorProd= float(input("Qual valor do produto: "))
formaPag= str.upper(input("Qual forma de pagamento! DINHEIRO, CHEQUE ou CARTÃO? "))
desconto= valorProd * 10/100
if valorProd >= 100 and formaPag =="DINHEIRO":
    valorApagar= valorProd - desconto
    print("O valor a pagar é: R$ %.2f"% valorApagar)
elif valorProd < 100 and formaPag == "DINHEIRO" or formaPag == "CHEQUE":
    valorApagar= valorProd
    print("O valor a pagar é: R$ %.2f"% valorApagar)
elif formaPag == "CARTÃO":
    formaParcelamento= str.upper(input("Como vai pagar: CRÉDITO ou DÉBITO? "))
    if formaParcelamento == "DÉBITO":
        valorApagar= valorProd
        print("O valor a pagar é: R$ %.2f"% valorApagar)
elif formaPag == "CARTÃO":
    formaParcelamento= str.upper(input("Como vai pagar: CRÉDITO ou DÉBITO? "))
    if formaParcelamento == "CRÉDITO":
        quantParcelas= int(input("Em quantas vezes quer parcelar? "))
        if quantParcelas <= 3:
            valorParcela= valorProd/quantParcelas
            valorApagar= valorProd      
            print("O valor a pagar é: R$ %.2f"% valorApagar)
            print("O valor de cada parcela é: R$ %.2f"% valorParcela)
        else:
            print("Quantidade de parcelas inválidas!")
    

        
