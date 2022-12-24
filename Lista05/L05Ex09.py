#Declaração de váriaveis
#i : int
#sinal :int
#s :int

#Begin
i=2
sinal=0
S=0
print('S={')
while i<101:
    if sinal==0:
        print(i, '-' , end= '')
        i+=2
        sinal= sinal+1
        S=S+i
    if sinal==1:
            print(i, '+' , end= '')
            i+=2
            sinal= sinal-1
            S=S-i
print('}')
print('')
print('S=',S)
#End
