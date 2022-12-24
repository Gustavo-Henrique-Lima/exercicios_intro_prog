#Declaração de váriaveis
#magoNegro : int
#sereletrico : int
#dragao : int
#genio : int
#Yami : int
#kaiba : int

#Início do programa
import random
farao=0
vizir=0
empate=0
magonegro= random.randint(1000,4000)
print('O mago negro do faraó tem poder' ,magonegro)
genio= random.randint(1000,4000)
print('O gênio do vizir tem poder' ,genio)
sereletrico= random.randint(1000,4000)
print('O ser elétrico do faraó tem poder' ,sereletrico)
dragao= random.randint(1000,4000)
print('O dragão do vizir tem poder' ,dragao)
if(magonegro>genio):
    farao+=1
elif(genio>magonegro):
    vizir+=1
else:
    empate+=1
if(sereletrico>dragao):
    farao+=1
elif(dragao>sereletrico):
    vizir+=14
else:
    empate+=1
if(farao>vizir and farao>empate):
    print('O faraó Yami venceu o duelo')
elif(vizir>farao and vizir>empate):
    print('O vizir Kaiba venceu o duelo')
else:
    print('Houve um empate')






#Fim do programa
