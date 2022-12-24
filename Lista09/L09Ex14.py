for i in range(1,10):
    sexo=int(input('Digite 1- MULHER 2- HOMEM: '))
    if sexo==1:
        nome_mulher=input()
        arquivo=open('mulher.txt','a')
        arquivo.write(nome_mulher)
        arquivo.write('\n')
        arquivo.close()
    if sexo==2:
        nome_homem=input()
        arq=open('homem.txt','a')
        arq.write(nome_homem)
        arq.write('\n')
        arq.close()
    if sexo!=1 and sexo !=2:
        print('ERRO 404 NOT FOUND')
        print('O que você inseriu foi registrado, reinicie o programa para inserir mais')
        break
