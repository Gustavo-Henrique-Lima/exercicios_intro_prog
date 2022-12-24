#Declaração de variável
#Forçadosenhor : float
#Forçadohomemcorcunda : float
#Forçadohomemdeumbraço : float
#Forçasenhora : float
#Forçaamigo : float

#Início do programa
forcasenhor=float(input('Insira a força do senhor esquelético: ')) #Obtendo força do senhor 1
if(forcasenhor>120): #Limite de força
    print('Valor da força do homem esquelético não condiz com a pessoa, tente novamente.')
else:
    forcahomemcorcunda=float(input('Insira a força do senhor concurda: ')) #Obtendo força do senhor 2
    if(forcahomemcorcunda>120): #Limite de força
         print('Valor da força do homem corcunda não condiz com a pessoa, tente novamente')
    else:
        forcahomemumbraco=float(input('Insira a força do homem com um braço: ')) #Obtendo força do senhor 3
        if(forcahomemumbraco>120): #Limite de força
             print('Valor da força do homem de um braço não condiz com a pessoa, tente novamente')
        else:
            forcasenhora=float(input('Insira a força da senhora: ')) #Obtendo força da senhora
            if(forcasenhora>120): #Limite de força
                print('Valor da força da senhora não condiz com a pessoa, tente novamente')
            else:
                forcaamigo=float(input('Insira a força do amigo da senhora: ')) #Obtendo força do amigo
                if(forcaamigo>50): #Limite de força
                    print('Valor da força do amigo da senhora não condiz com a pessoa, tente novamente')
                else:
                    forcagrupo1=forcahomemcorcunda+forcahomemumbraco+forcasenhor #Somando forças 
                    forcagrupo2=forcasenhora+forcaamigo #Somando forças 
                    if(forcagrupo1>120) or (forcagrupo2>120):#Comparação se foi gerada força suficiente para mover a porta
                        if(forcagrupo1>forcagrupo2): #Se a força foi suficiente, quem a gerou
                            print('O grupo 1 conseguiu abrir a porta pois exerceu força de: ' , forcagrupo1 , ' que superou a força do grupo 2, que foi de : ' , forcagrupo2)
                        else:
                            print('O grupo 2 conseguiu abir a porta pois exerceu forã de: ' , forcagrupo2 , ' que superou a forã do grupo 1, que foi de : ' , forcagrupo1)
                    else: #Possibilidade de empate
                        print('Ambos os grupos não estão exercendo força suficente para mover a porta, está empate :o')
        
#Fim do programa :)
