#Declaração de váriaveis
#opcao1 : int
#opcao2 : int
#opcao3 : int
#qboneco :int
#valorboneco : int
#qtumulo : int
#valortumulo: int
#qmorcegos : int
#valormorcegos : int
#valortotal : int

#Início do programa
import random
qboneco=0
valorboneco=0
qtumulo=0
valortumulo=0
qmorcegos=0
valormorcegos=0
valortotal=0
for i in range(1,4):
    print('Digite 1 para boneco de machimelo\n2 para túmulo\n3 para morcegos')
    opcao=int(input())
    if(opcao==1):
        valortotal+=350
        qboneco+=1
        valorboneco+=350
    elif(opcao==2):
            valortotal+=120
            valortumulo+=120
            qtumulo+=1
    elif(opcao==3):
            valortotal+=50
            qmorcegos+=1
            valormorcegos+=50
    else:
        print('Rodada não válida')
print('O campus gastou em uma semana o valor total de' , valortotal, 'R$ sendo' ,valorboneco, 'por' ,qboneco,' bonecos de machimelos encontrados,' ,qtumulo, ' túmulos que deram um valor de' , valortumulo, 'e' ,qmorcegos, ' morcegos que foram encontrados, que custaram' ,valormorcegos)



#Fim do programa
