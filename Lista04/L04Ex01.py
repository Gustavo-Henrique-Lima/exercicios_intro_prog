#Declaração de variáveis
#Jesse Quick : int
#Barry Allen : int
#Wally West :int
#Dr.Wells : int
#Jay Garrick : int
#Max Mercury : int

#Início do programa
import random
for i in range(1,7):
    jessequick= random.randint(290000,300000)
    barryallen= random.randint(290000,300000)
    wallywest= random.randint(290000,300000)
    wells= random.randint(290000,300000)
    jay= random.randint(290000,300000)
    maxm= random.randint(290000,300000)
print('Jesse Quick correu a:', jessequick , ' Kms/s')
print('Barry Allen correu a:', barryallen , ' Kms/s')
print('Wally West correu a:', wallywest , ' Kms/s')
print('Dr.Wells correu a:', wells , ' Kms/s')
print('Jay Garrick correu a:', jay , ' Kms/s')
print('Max Mercury correu a:', maxm , ' Kms/s')
if(jessequick>barryallen) and (jessequick>wallywest) and (jessequick>wells) and(jessequick>jay) and(jessequick>maxm):
    print('Jesse Quick venceu a corrida!')
if(barryallen>jessequick) and (barryallen>wallywest) and (barryallen>wells) and (barryallen>jay) and(barryallen>maxm):
    print('Barry Allen venceu a corrida!')
if(wallywest>barryallen) and (wallywest>jessequick) and (wallywest>wells) and (wallywest>jay) and(wallywest>maxm):
    print('Wally West venceu a corrida!')
if(wells>jessequick) and (wells>barryallen) and (wells>wallywest) and (wells>jay) and(wells>maxm):
    print('Dr.Wells venceu a corrida!')
if(jay>jessequick) and (jay>barryallen) and (jay>wallywest) and (jay>wells) and(jay>maxm):
    print('Jay Garrick venceu a corrida!')
if(maxm>jessequick) and (maxm>barryallen) and (maxm>wallywest) and (maxm>wells) and(maxm>jay):
    print('Max Mercury venceu a corrida!')

#Fim do programa:)
