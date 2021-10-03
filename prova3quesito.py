#Declaração de variáveis
#altura_homem: float
#homem_alto :float
#homem_baixo : float
#altura_mulher : float
#mulher_baixo : float
#mulher_alto : float

#Início do programa
import random
print('*' *5 , 'A ALTURA SERÁ DADA EM CM' , '*' *5)
homem_alto = home_baixo = altura_homem= 0
homem_alto = 0
homem_baixo=100
mulher_alta = mulher_baixa = altura_mulher =0
mulher_alta=0
mulher_baixa=100
for i in range(1,201):
    altura_homem=random.randint(1,200)
    if altura_homem>homem_alto:
        homem_alto=altura_homem
    if altura_homem<homem_baixo:
        homem_baixo= altura_homem
for j in range(1,301):
    altura_mulher=random.randint(1,200)
    if altura_mulher>mulher_alta:
        mulher_alta=altura_mulher
    if altura_mulher<mulher_baixa:
        mulher_baixa= altura_mulher
print('O homem mais alto tem : {:.1f} cm de altura'.format(homem_alto))
print('O homem mais baixo tem : {:.1f} cm de altura'.format(homem_baixo))
print('O mulher mais alta tem : {:.1f} cm de altura'.format(mulher_alta))
print('O mulher mais baixa tem : {:.1f} cm de altura'.format(mulher_baixa))

#Fim do programah
