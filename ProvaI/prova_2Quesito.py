import random
def sorteio():
    cont=0
    while cont<quantidade:
        n1 = random.randint(1,99)
        while n1%2==0:
            n1 = random.randint(1,99)
        n2 = random.randint(1,99)
        while n1 == n2:
           n2 = random.randint(1,99)
        n3 = random.randint(1,99)
        while (n3 == n1) or (n3 == n2):
            n3 = random.randint(1,99)
        n4 = random.randint(1,99)
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = random.randint(1,99)
        cont+=1
        print('Os números para o palpite',cont,'são:',n1, n2, n3, n4,'\n')
quantidade=int(input('Digite a quantidade de palpites que você deseja: '))
print('')
sorteio()
