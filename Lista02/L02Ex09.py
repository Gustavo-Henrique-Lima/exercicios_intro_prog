#Declaração de váriaveis
#Temperatura : float

#Início do programa
print("Com esse programa voce digite a temperatura da água em CELSIUS e ele lhe responde em qual estado físico ela se encontra")
temperatura = float(input("Digite a temperatura da água em Celsius : "))
if temperatura<0 :
    print("A água se encontra no estado solido.")
if temperatura>=0 and temperatura <=100 :
    print("A água se encontra no estado líquido.")
if temperatura>100 :
    print("A água se encontra no estado gasoso.")
