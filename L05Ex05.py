#Declaração de váriaveis
#numeros : int
#qacertos: int

#Begin
import random
qacertos=0
for i in range(1,196):
    numeros=random.randint(11,300)
    if numeros%11==0:
        qacertos+=1
print('*' *10)
print('Cérebro acertou' ,qacertos, 'países com sua arma')



#End
