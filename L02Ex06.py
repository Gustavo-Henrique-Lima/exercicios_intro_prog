#Declaração de váriavéis
#Hipotenusa : int
#Cateto1 : int
#Cateto2 : int
#Novahipotenusa : int
#Novocateto1: int
#Novocateto2: int

#Início do programa
hipotenusa= int(input("Para descobrir se o seu triângulo é um triângulo rentâgulo informe a hipotenusa dele: "))
cateto1= int(input("Agora informe o valor do primeiro cateto: "))
cateto2= int(input("Agora informe o valor do segundo cateto: "))
novahipotenusa=hipotenusa*hipotenusa
novocateto1=cateto1*cateto1
novocateto2=cateto2*cateto2
somacateto=novocateto1+novocateto2
if novahipotenusa==somacateto :
    print("O seu triângulo é um triângulo retângulo")
else:
    print("O seu triângulo não é um triângulo retângulo")
