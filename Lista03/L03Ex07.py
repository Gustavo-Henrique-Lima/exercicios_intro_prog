#Declaraçao de variável
#num : int
#fat : int

#Início do programa
num=int(input('Digite o número para calcular o seu fatorial: '))
c = num
fat = 1
while c > 0:
    print('{} '.format(c))
    fat*=c
    c-=1
print('O fatorial de ' , num , ' é: {}'. format(fat))
#Fim do programa :)
    
