import random
array=[]
array_par=[]
media_par=0
par=0
for i in range(1,21):
    numero=random.randint(1,200)
    array=array+[numero]
    if numero%2==0:
        array_par=array_par+[numero]
        par+=numero
media_par=par/(len(array_par))
print('A média dos número pares é {:.2f}'.format(media_par))
tamanho=len(array)
for i in range (tamanho):
    troca = False
    for j in range(1, tamanho- i):
        if array[j] < array[j-1]:
            Temp=array[j]
            array[j]= array[j-1]
            array[j-1]= Temp
            troca = True
        if not troca:
            break
print('O array ordenado: ',array)
