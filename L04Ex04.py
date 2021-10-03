#Declaração de variávies
#quantidade = int


#Início do programa
quantidade= int(input('Digite a quantidade de pessoas que você deseja cadastrar: '))
homemmaisnovo=100
cadastrohomem=False
cadastromulher=False
idademulher=0
idademulhervelha=1
nomemulhernova= ''
for i in range(quantidade):
        print('Tecle 1-Para homem\n2-Para mulher\nPara a pessoa', i+1)
        sexo=int(input())
        if(sexo==1):
            cadastrohomem=True
            print('Digite o nome da' ,i+1, 'pessoa que é um homem: ')
            nome=input()
            print('Digite a idade de', nome)
            idade=int(input())
            if(idade<homemmaisnovo):
                homemmaisnovo=idade
        if(sexo==2):
            cadastromulher=True
            print('Digite o nome da' ,i+1, 'pessoa que é uma mulher: ')
            nomemulher=input()
            print('Digite a idade da mulher da(e)', nomemulher)
            idademulher=int(input())
            if(idademulher>idademulhervelha):
              idademulhervelha=idademulher     
              nomemulhernova=nomemulher
        if(sexo<1 or sexo>2):
                print('Opção inválida')
if(cadastrohomem==True):
        print(homemmaisnovo, 'é a idade do homem mais novo')
elif(cadastrohomem==False):
        print('Nenhum homem cadastrado')
if(cadastromulher==True):
        print(nomemulhernova, ' é o nome da mulher mais velha')
elif(cadastromulher==False):
        print('Nenhuma mulher cadastrada')
