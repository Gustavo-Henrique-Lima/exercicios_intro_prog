#Declaração de váriaveis
#num1: int
#num2: int

#Início do programa
num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))
if(num1%2==0 and num2%2==0):
    print('A soma de' ,num1, '+',num2, 'é: ' ,num1+num2)
elif(num1%2!=0 and num2%2!=0):
    print('A subtração de' ,num1, 'por' ,num2, 'é : ' , num1-num2)
else:
    print('A multiplicação de ' ,num1, 'por' ,num2, 'é : ' ,num1*num2)




#Fim do programa
