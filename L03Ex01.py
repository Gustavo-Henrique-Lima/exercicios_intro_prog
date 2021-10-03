#Declarações de variáveis
#notaport : float
#notamat : float
#notapower : int
#tipodepoder : int
#mediafinal : float
#Início do programa
aprovadoportugues = False
aprovadomatematica = False
notaport = float(input('Insira a nota do candidato no teste de português: ')) #Lendo nota em português do aluno
if (notaport >= 8):
        aprovadoportugues = True
        notamatemat = float(input('Insira a nota do candidato em matemática: '))
        if(notamatemat >7) :                #Lendo nota em matemática do aluno
            aprovadomatematica = True
            print('Agora vamos para a avaliação do poder')   
            tipodepoder = int(input('Tecle 1-Para telepata\nTecle 2- Para outros\n ')) #Lendo tipo de poder
            if(tipodepoder ==1): #Conferindo se ele é telepata
                notapower= int(input('Digite a nota da avalição do poder do candidato '))
                if(notapower==10) :
                    print('Omêga')  #Se nota de poder =10 retorno de omêga
                else :
                    mediafinal = (notaport+notamatemat+(notapower*2))/3 #Se nota de poder <10, mas candidato telepata, então nota de poder recebe peso 2
                    print('A média final do candidato é : {:.2f}'.format(mediafinal)) #Imprimindo média final
            if(tipodepoder==2) : #Se candidato não for telepata
                notapower= int(input('Digite a nota da avalição do poder do candidato '))
                if(notapower==10) :
                    print('Omêga') #Se nota de poder =10 retorno de omêga
                else : #Nota de poder <10
                    mediafinal = (notaport+notamatemat+notapower)/3 #Imprimindo média final
                    print('A média final do candidato é : {:.2f}'.format(mediafinal))
            elif(tipodepoder != 1) and (tipodepoder!=2): #tratamento de erro para opção de poder digitada errada
                  print('Opção inválida, tente novamente')
        if not aprovadomatematica:
            print('O candidato não obteve média suficiente em matemática para avançar no processo.')
if not aprovadoportugues:                               #Se o aluno não tiver nota >=8 em português, que é a necessária para avançar para a proxima fase ele é excluido do processo e informado o porquê
    print('O candidato não obteve média suficiente em português para passar avançar no processo.') #Se o aluno não tiver nota >7 em matemática, que é a necessária para avançar para proxima fase ele é excluido do processo e informado o porquê


#Fim do programa
