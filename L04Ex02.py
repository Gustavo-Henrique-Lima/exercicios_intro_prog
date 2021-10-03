#Declaração de variáveis
#base : int
#expoente : int
#pontencia : int

#Início do programa
potencia=1
base= int(input('Por favor, digite o valor da base da potência: '))
expoente= int(input('Por favor, digite o valor do expoente da potência: '))
for i in range(expoente):
    potencia*=base
print(base , ' elevado a ' , expoente, ' é igual a ' , potencia)

#Fim do programa:)
