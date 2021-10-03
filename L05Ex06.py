#Declaração de váriaveis
#cont : int
#pessoas :int
#quantidade: int
#idademenor= -1

#public static main void (Args[]string){
cont=1
nome_novo= ''
idade_velha=0
while cont ==1:
    nome=input('Digite o nome da pessoa: ')
    print('Digite a idade de ', nome , end=' ')
    idade=int(input())
    if(idade%2!=0):
        print('')
    elif(idade%2==0):
        if idade>idade_velha:
            idade_velha=idade
            nome_novo=nome
    print('Digite 1 para cadastrar mais pessoas')
    cont=int(input('2-para terminar\n'))
print(nome_novo, 'é a mais velha')






#}
