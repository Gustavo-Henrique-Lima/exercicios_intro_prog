def ordem(nomes):
    tamanho = len(nomes)
    for i in range(tamanho):
        troca = False
        for j in range(1, tamanho - i):
            if nomes[j] > nomes[j - 1]:
                Temp = nomes[j]
                nomes[j] = nomes[j - 1]
                nomes[j - 1] = Temp
                troca = True
        if not troca:
            break
    return nomes
nomes=[]
nome_mais_velha=''
idade_mais_velha=-100
maior_nome=''
tamanho=-100
contador=0
continuar=True
while continuar:
    print('Digite o nome da pessoa: ')
    nome=input()
    if nome[0]=='A' or nome[0]=='a':
        contador+=1
    if (len(nome))> tamanho:
        maior_nome=nome
        tamanho=(len(nome))
    nomes=nomes+[nome]
    print('Digite a idade da pessoa: ')
    idade=int(input())
    if idade>idade_mais_velha:
        idade_mais_velha=idade
        nome_mais_velha=nome
        
    print('Deseja continuar?\n1-SIM 2-NÃO')
    cont=int(input())
    if cont==2:
        continuar=False
    if cont<1 or cont>2:
        print('Erro tente novamente')
ordem(nomes)
print('Lista de nomes ordenada de Z a A',nomes)  
print('Existem',contador,'pessoa que o nome começa com a letra A')
print('A pessoa mais velha é: ',nome_mais_velha)
print('O maior nome lido foi', maior_nome,'de tamanho',tamanho)
