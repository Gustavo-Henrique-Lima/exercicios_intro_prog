#Declaração de váriaveis
#num1 : int
#num2 : int
#num3 : int
#melodia1 : int
#melodia2 : int
#melodia3 : int

#public static void mais (String[]args) {
import random

igual= False
contador=0
melodia1=random.randint(1,10)
melodia2=random.randint(1,10)
melodia3=random.randint(1,10)
num1=random.randint(1,10)
num2=random.randint(1,10)
num3=random.randint(1,10)
while igual==False:
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    num3=random.randint(1,10)
    contador+=1
    if num1==melodia1 and num2== melodia2 and num3==melodia3:
        igual=True
print('*' *10)
print('O flautista tentou ' ,contador,'vezes')
print('Melodia : ' ,num1,num2,num3)

#}
