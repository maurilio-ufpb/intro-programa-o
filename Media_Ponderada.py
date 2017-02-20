
# 9. Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final
# deste aluno. Considerar que a média é ponderada e que o peso das notas é:
# 2, 3 e 5, respectivamente.


pn1= 2 # peso primeira nota
pn2= 3 # peso segunda nota
pn3= 5 # peso terceira nota

n1= float(input("Informe a primeira nota: "))
n2= float(input("Informe a segunda nota: "))
n3= float(input("Informe a terceira nota: "))

media= ((n1*pn1+(n2*pn2)+ n3*pn3))/(2+3+5)
print()
print("A média ponderada é: ", media)

