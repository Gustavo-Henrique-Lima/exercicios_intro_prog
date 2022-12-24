#Declaração de variáveis
#nota : float
#media :float
#Início do programa
media=0
cont=0
while cont<=19:
    media=float(input('Digite a média do aluno '))
    if(media>=7):
        print('Aluno aprovado')
    else:
        print('')
    cont+=1
