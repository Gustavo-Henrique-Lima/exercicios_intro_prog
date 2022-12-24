#Declaração de váriaveis
#pe : int
#corridasdias : int
#final : int

#Início do programa
import random
qtotal=0
pe=random.randint(1,2)
print(pe)
if(pe==1):
    for  i in range(1,6):
     corrida=random.randint(1,29)
     print('No dia' ,i, 'Ligeirinho correu' ,corrida, 'vezes')
     queijo=random.randint(1,10)
     print('No dia' ,i, 'Ligeirinho pegou' ,queijo, 'pedaços de queijo')
     qtotal+=queijo
    print('Ao final dos cinco dias, Ligeirinho pegou' ,qtotal, 'pedaços de queijo')
if(pe==2):
    print('Ligeirinho começou com o pé esquerdo e não obteve velocidade suficiente para pegar nenhum pedaço de queijo.')
