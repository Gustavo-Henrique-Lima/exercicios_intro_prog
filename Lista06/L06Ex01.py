#Declaração de variáveis
#nome : String
#idade : int
import random
from random import choice
parar=True
nome_padawan_maior15=[]
nome_padawan_menor15=[]
lista=[]
contador=0
media_idade=0
idade_maisvelho=-100
nome_maisnovo=''
idade_maisnovo=100
escolhido=''
#Inicío do programa para leitura com quantidade indefinida
while parar:
    nome=input('Digite o nome do padawan: ')
    idade=int(input('Digite a idade do padawan: '))
    if(idade<idade_maisnovo): #Procurando mais novo
        idade_maisnovo=idade
        nome_maisnovo=nome
    if(idade>idade_maisvelho):#Procurando mais velho
        idade_maisvelho=idade
        nome_maisvelho=nome
    contador+=1  #Contador para saber a quantidade de padawans cadastrados, que será usado para obter a média de idade
    media_idade+=idade #Somando idades para calcular média
    if idade>=15:  #Atribuindo maiores que 15 à lista
        nome_padawan_maior15=nome_padawan_maior15 + [nome]
    else:          #Atribuindo menores que 15 à lista
        nome_padawan_menor15=nome_padawan_menor15 + [nome]
    print('Deseja cadastar mais um padawan?')
    print('1-SIM |||||2- NÃO')
    sair=int(input())
    if sair<1 or sair>2:
          print('*' *5 ,'ERRO 404 NOT FOUND', '*' *5)
          break
    if sair==2:
        parar=False
print('Os padawan que precisão de mestre são :')
for i in range (len(nome_padawan_maior15)): #Retornando lista com os que precisão de mestre
    print(nome_padawan_maior15[i] ,' ', end= '')
print('')
print('Os padwan com idade menor que 15 são: ') #Retornando lista com os que tem idade <15
for i in range (len(nome_padawan_menor15)):
    print(nome_padawan_menor15[i] , ' ', end='')
print('')
print('A média de idade dos padawans é:{:.2f}'.format(media_idade/contador)) #Retornando média de idade
print('O padawan mais velho é: ' , nome_maisvelho)#Retornando mais velho
print('O padawan mais novo é: ' ,nome_maisnovo)#Retornando mais novo
print('')
#Gerando padawns para os mestres
for i in range (0,nome_padawan_maior15):
    Kenobi =  random.randint(0,len(nome_padawan_maior15))
print('O padawan do mestre Kenobi é ', nome_padawan_maior15[Kenobi])



