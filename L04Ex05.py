#Declaração de variáveis
#cont : int
#valorfinal: int
#moto : int
#carro : int
#onibus : int
#escolha : int

#Início do programa
cont=1
valorfinal=0
moto=0
carro=0
onibus=0
while cont<=400:
    escolha=int(input('Tecle 1 para moto\nTecle 2 para carro\nTecle 3 para ônibus: '))
    if(escolha==1):
        valorfinal+=4
        moto+=1
    if(escolha==2):
        valorfinal+=8
        carro+=1
    if(escolha==3):
        valorfinal+=20
        onibus+=1
    if(escolha<1 or escolha>3):
        print('Opção inválida')
    cont+=1
print('Ao final do dia passaram pelo estacionamento' ,moto, 'motos' ,carro, 'carros' , onibus, 'ônibus')
print('No final do dia o estabelecimento teve lucro de : ', valorfinal)
#Fim do programa:)
