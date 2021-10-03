print('Os 30 termos da sequência 1/2 são:')
razaonumerador=1
razaodenominador=2
termo1=1
termo2=2
cont=1
while cont<=30:
    print(termo1,'/',termo2)
    termo1+=razaonumerador
    termo2+=razaodenominador
    cont+=1
