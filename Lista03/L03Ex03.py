#Declaração de variáveis
#escolha : int
#montante : float
#caminho: int
#valor1 : int
#valorfinal : int

#Inicio do programa
print('Escolha sua profissão')
print('1-Médico\n2-Jornalista\n3-Advogado\n4-Professor\n5-Físico\n6-Comerciante\n7-Estudante')
escolha=int(input())
if(escolha==1) or (escolha==3):  #Início da escolha para médico ou advogado
    print('Agora escolha qual caminho seguir, no caminho A você receberá o pagamento 30 vezes, mas dos 30 dez serão pagos pela metade. Já o caminho B receberá o pagamento 25 vezes, mas dos 25 cinco serão pagos pela metade.')
    caminho=int(input('Tecle 1- Para caminho A, ou 2 para caminho B: '))
    if(caminho==1) :
        valor1=50 * 20
        valorfinal=(50*10)/2
        print('O seu montante final é de: {:.2f}'.format(valor1+valorfinal))
    elif(caminho==2) :
        valor1=50*20
        valorfinal=(50*5)/2
        print('O seu montante final é de: {:.2f}'.format(valor1+valorfinal))
    else :
        print('Escolha inválida, tente novamente') #Fim da escolha para médico ou advogado
if(escolha==2) or (escolha==4): #Início da escolha para jornalista ou professor
    print('Agora escolha qual caminho seguir, no caminho A você receberá o pagamento 30 vezes, mas dos 30 dez serão pagos pela metade. Já o caminho B receberá o pagamento 25 vezes, mas dos 25 cinco serão pagos pela metade.')
    caminho=int(input('Tecle 1- Para caminho A, ou 2 para caminho B: '))
    if(caminho==1) :
        valor1=24 * 20
        valorfinal=(24*10)/2
        print('O seu montante final é de: {:.2f}'.format(valor1+valorfinal))
    elif(caminho==2) :
        valor1=24*20
        valorfinal=(24*5)/2
        print('O seu montante final é de: {:.2f}'.format(valor1+valorfinal))
    else :
        print('Escolha inválida, tente novamente') #Fim da escolha para jornalista ou professor
if(escolha==5): #Início da escolha físico
    print('Agora escolha qual caminho seguir, no caminho A você receberá o pagamento 30 vezes, mas dos 30 dez serão pagos pela metade. Já o caminho B receberá o pagamento 25 vezes, mas dos 25 cinco serão pagos pela metade.')
    caminho=int(input('Tecle 1- Para caminho A, ou 2 para caminho B: '))
    if(caminho==1):
        valor1=30 * 20
        valorfinal=(30*10)/2
        print('O seu montante final é de: {:.2f}'.format(valor1+valorfinal))
    elif(caminho==2) :
        valor1=30*20
        valorfinal=(30*5)/2
        print('O seu montante final é de: {:.2f}'.format(valor1+valorfinal))
    else :
        print('Escolha inválida, tente novamente')#Fim da escolha para físico
if(escolha==6):  #Início da escolha para comerciante
    print('Agora escolha qual caminho seguir, no caminho A você receberá o pagamento 30 vezes, mas dos 30 dez serão pagos pela metade. Já o caminho B receberá o pagamento 25 vezes, mas dos 25 cinco serão pagos pela metade.')
    caminho=int(input('Tecle 1- Para caminho A, ou 2 para caminho B: '))
    if(caminho==1) :
        valor1=12 * 20
        valorfinal=(12*10)/2
        print('O seu montante final é de: {:.2f}'.format(valor1+valorfinal))
    elif(caminho==2) :
        valor1=12*20
        valorfinal=(12*5)/2
        print('O seu montante final é de: {:.2f}'.format(valor1+valorfinal))
    else :
        print('Escolha inválida, tente novamente') #Fim da escolha para comerciante
if(escolha==7):#Início da escolha para estudante
    print('Agora escolha qual caminho seguir, no caminho A você receberá o pagamento 30 vezes, mas dos 30 dez serão pagos pela metade. Já o caminho B receberá o pagamento 25 vezes, mas dos 25 cinco serão pagos pela metade.')
    caminho=int(input('Tecle 1- Para caminho A, ou 2 para caminho B: '))
    if(caminho==1) :
        valor1=16 * 20
        valorfinal=(16*10)/2
        print('O seu montante final é de: {:.2f}'.format(valor1+valorfinal))
    elif(caminho==2) :
        valor1=16*20
        valorfinal=(16*5)/2
        print('O seu montante final é de: {:.2f}'.format(valor1+valorfinal))
    else :
        print('Escolha inválida, tente novamente') #Fim da escolha para estudante
elif(escolha<1) or (escolha>7): #Tratamento de escolha de profissão inválida
    print('Escolha inválida, tente novamente.')
#Fim do programa :)       
     
