vitoria=0
desafio1=False
desafio2=False
desafio3=False
desafio4=False
forcaloki=0
forcahogun=0
par=0
parval=0
loki1=0
valquiria=0
pontostotalloki=0
pontostotalfrandal=0
import random
print('PRIMEIRO DESAFIO, QUEM COME MAIS?')
for i in range(1,3):
    loki=random.randint(1,100)
    volstagg=random.randint(1,100)
if(loki>volstagg):
    vitoria+=1
    desafio1=True
if(desafio1==True):
    print('Loki comeu ' ,loki, 'kg de comida equanto Volstagg comeu' ,volstagg, ' Loki venceu o primeiro desafio!')
else:
    print('Loki comeu ' ,loki, 'kg de comida equanto Volstagg comeu' ,volstagg, ' Loki perdeu o primeiro desafio!')
print('Loki tem ' , vitoria , ' vitória')
print('*' *15)
print('SEGUNDO DESAFIO, LOKI E FRANDAL TEM 10 FLECHAS PARA ATIRAR NO ALVO, NO ALVO')
for i in range(1,11):
    loki=random.randint(1,60)
    if(loki>50):
        print('Loki errou o alvo :o')
    else:
        pontostotalloki+=loki
for i in range(1,11):
    frandal=random.randint(1,60)
    if(frandal>50):
        print('Frandal errou o alvo :o')
    else:
        pontostotalfrandal+=frandal
if(pontostotalloki>pontostotalfrandal):
    vitoria+=1
    desafio2=True
if(desafio2==True):
    print('Loki obteve' ,pontostotalloki, 'enquanto Frandal obteve' ,pontostotalfrandal, ' por isso Loki venceu o segundo desafio!')
else:
    print('Loki obteve' ,pontostotalloki, 'enquanto Frandal obteve' ,pontostotalfrandal, ' por isso Loki perdeu o segundo desafio!')
print('Loki tem' ,vitoria, ' vitória')
print('*' * 15)
print('TERCEIRO DESAFIO')
for i in range(1,2):
    forcaloki=random.randint(1,10)
    forcahogun=random.randint(1,10)
if(forcaloki>forcahogun):
        vitoria+=1
        desafio3=True
if(desafio3==True):
    print('Loki derrotou Hogu em uma batalha de polegar pois exerceu' ,forcaloki, ' pontos de força enquanto Hogu exerceu' ,forcahogun, 'pontos de força')
else:
    print('Loki perdeu para Hogu em uma batalha de polegar pois exerceu' ,forcaloki, ' pontos de força enquanto Hogu exerceu' ,forcahogun, 'pontos de força')
print('Loki tem' ,vitoria, ' vitória(s)')
print('*' *15)
if(vitoria==3):
    print('Loki obteve 3 vitórias e já esta apto a defender Asgard!')
    print('*' * 15)
else:
    print('QUARTO DESAFIO, DUELO DE SORTE, QUEM CONSEGUIRÁ TIRAR UM DUPLO POR')
    for i in range(1,100):
        loki1=random.randint(1,100)
        if(loki1%2==0):
            par=loki1
        valquiria=random.randint(1,100)
        if(valquiria%2==0):
            par=valquiria
        loki1=random.randint(1,100)
        if(loki1==par):
            desafio4=True
            break
        valquiria=random.randint(1,100)
        if(valquiria==par):
            desafio4=False
            break
    if(desafio4==True):
        print('Loki ganhou pois tirou 2 ' ,par)
        vitoria+=1
    else:
        print('Valquiria ganhou pois tirou 2' , parval)
    print('Loki tem' ,vitoria, ' vitórias')
    if(vitoria==3):
        print('Loki obteve 3 vitórias e já esta apto a defender Asgard!')
    else:
        print('*' *15)
        print('QUINTO DESAFIO')
        print('Loki usou seus poderes e trapaceou, ganhando assim de Lady Sif')
        vitoria+=1
        print('Com o fim do último desafio Loki obteve um total de : ' ,vitoria, ' vitórias')
        if(vitoria==3):
            print('Loki venceu 3 desafios, e está apto a defender Asgard!')
        else:
            print('Loki não venceu a quantidade suficiente de desafio e por isso não está apto a defender Asgard!')
