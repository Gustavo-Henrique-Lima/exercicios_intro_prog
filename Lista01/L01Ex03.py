produto = float(input("Digite o valor do produto:"))
print("Existem 3 possibilidades de parcelas, a primeira: 1 mês, a segunda 2 meses e a terceira 3 meses.")
qparcelas = int(input("Digite em quantas parcelas você deseja: "))
if qparcelas==1 :
    valorfinal = produto+produto*(2/100)
    juros= valorfinal-produto
    print("Você escolheu " , qparcelas , " parcelas e por isso o produto ficará por : " , valorfinal)
    print("Sendo " , produto , " o valor do produto e " , juros , " de juros ")
if qparcelas==2 :
    valorfinal = produto+produto*(4/100)
    juros= valorfinal-produto
    print("Você escolheu " , qparcelas , " parcelas e por isso o produto ficará por : " , valorfinal)
    print("Sendo " , produto , " o valor do produto e " , juros , " de juros ")
if qparcelas==3 :
    valorfinal = produto+produto*(6/100)
    juros= valorfinal-produto
    print("Você escolheu " , qparcelas , " parcelas e por isso o produto ficará por : " , valorfinal)
    print("Sendo " , produto , " o valor do produto e " , juros , " de juros ")
    
