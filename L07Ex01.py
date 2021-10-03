#Criando função para calcular potência
def calcular_potencia(base,expoente):
    potencia=1
    for i in range(expoente):
        potencia*=base
    print('O resultado da sua potência é :' ,potencia)
#Criando programa principal
continuar=1
while continuar==1:
    base=int(input('Digite o valor da base: '))
    expoente=int(input('Digite o valor do expoente: '))
    calcular_potencia(base,expoente)
    print('')
    print('Deseja continuar?\n1- SIM 2 - NÃO ')
    continuar=int(input())
    
   

