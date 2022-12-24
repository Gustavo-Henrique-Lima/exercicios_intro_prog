#Declaração de váriaveis
#Lado1 : int
#Lado2 : int
#Lado3 : int

#Início do programa

lado1= int(input("Para continuarmos, digite o valor do lado A do seu triângulo: "))
lado2= int(input("Para continuarmos, digite o valor do lado B do seu triângulo: "))
lado3= int(input("E por fim, digite o valor do lado C do seu triângulo: "))
somalados1=lado2+lado3
somalados2=lado1+lado3
somalados3=lado2+lado1
if lado1>somalados1 or lado2>somalados2 or lado3>somalados3  :
    print("Suas medidas não formam um triângulo")
if  lado1==lado2 :
    print("O seu triângulo é um triângulo isóceles")
