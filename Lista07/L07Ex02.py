import random
#Definindo funçao para cacular fatorial
def fatorial(n):
    fatorial=1
    for c in range(n ,0,-1):
        fatorial*=c
    return fatorial
#Programa principal
for i in range(1,11):
    num=random.randint(1,30)
    print('O fatorial de' ,num, 'é:',fatorial(num))
