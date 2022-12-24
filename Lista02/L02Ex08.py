#Declaração de varíaves
#Escolha : int
#Area : float
#Altura : float
#Base : float
#Raio : float

#Início do programa

print('Olá, voce pode descobrir a área de 3 formas \n Tecle 1 para retângulo \n Tecle 2 para triângulo \n Tecle 3 para círculo.')

escolha= int(input("Digite sua escolha: "))
if escolha==1 :
    base=  float(input("Digite  o valor da base do retângulo "))
    altura= float(input("Digite o valor da altura do retângulo "))
    area=base*altura
    print("A área do retângulo é : " , area)
if escolha==2 :
    base = float(input("Digite o valor da base do triângulo "))
    altura= float(input("Digite o valor da altura do triângulo "))
    area=base*altura/2
    print("A área do triângulo é : " , area)
if escolha==3 :
    raio = float(input("Digite o valor do raio do círculo "))
    area=3.14*(raio*raio)
    print("A área do círculo é : " , area)
