#Definindo função para descobrir se é triângulo
def triangulo(a,b,c):
    triangulo = True
    equilatero = False
    escaleno = False
    if((a > (b + c)) or (b > (c + a)) or (c > (b + a))):
        triangulo=False
        print('Não é um triângulo')
    if triangulo and (a == b) and (b == c):
        equilatero=True
        print('Os lados da figura formam um triângulo equilátero')
    if triangulo and (a != b) and (b != c) and (a != c):
        escaleno=True
        print('Os lados da figura formam um triângulo escaleno')
    if triangulo:
        if equilatero or escaleno:
            print('')
        else:
            print('Os lados da figura formam um triângulo isósceles')
#Programa principal
for i in range(1,6):
    print('Digite os valores da' ,i, 'figura')
    a=int(input('Digite o primeiro lado da figura: '))
    b=int(input('Digite o segundo lado da figura: '))
    c=int(input('Digite o terceiro lado da figura: '))
    triangulo(a,b,c)
    print('')



