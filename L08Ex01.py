import random
Lista=[]
Lista_Par=[]
Lista_Impar=[]
for i in range(1,31):
    numero=random.randint(10,99)
    Lista=Lista+[numero]
    if numero%2==0:
        Lista_Par=Lista_Par+[numero]
    else:
        Lista_Impar=Lista_Impar+[numero]
print('Lista gerada: ' ,Lista)
print('*'*80)

tamanho=len(Lista)
for i in range(tamanho):
        troca = False
        for j in range(1, tamanho - i):
            if Lista[j] < Lista[j - 1]:
                Temp = Lista[j]
                Lista[j] = Lista[j - 1]
                Lista[j - 1] = Temp
                troca = True
        if not troca:
            break

print('Lista ordenada: ' ,Lista)
print('*'*80)
print('Lista dos número pares: ' ,Lista_Par)
print('*'*80)
tamanho1=len(Lista_Par)
for i in range(tamanho1):
        troca = False
        for j in range(1, tamanho1 - i):
            if Lista_Par[j] < Lista_Par[j - 1]:
                Temp = Lista_Par[j]
                Lista_Par[j] = Lista_Par[j - 1]
                Lista_Par[j - 1] = Temp
                troca = True
        if not troca:
            break
print('Lista dos números pares ordenados: ', Lista_Par)
print('*'*80)
print('Lista dos números ímpares: ', Lista_Impar)
tamanho2=len(Lista_Impar)
for i in range(tamanho1):
        troca = False
        for j in range(1, tamanho2 - i):
            if Lista_Impar[j] < Lista_Impar[j - 1]:
                Temp = Lista_Impar[j]
                Lista_Impar[j] = Lista_Impar[j - 1]
                Lista_Impar[j - 1] = Temp
                troca = True
        if not troca:
            break
print('*'*80)
print('Lista dos números ímpares ordenados:' ,Lista_Impar)
