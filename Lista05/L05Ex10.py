#Declaração de váriaveis
#num1 : int
#num2 : int

#Início do programa
num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))
if(num2==0):
    print('Não existe divisão por 0')
else:
    div=num1/num2
    print('O valor da divisão de' ,num1, 'por' ,num2, 'é : {:.1f} '.format(div))
