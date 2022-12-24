import random
comissao=0
salario=0
salario_liquido=0
desconto_inss=0
for i in range(1,21):
    salario=random.randint(40000,150000)
    cor=random.randint(1,2)
    if cor==1:
        quantidade=random.randint(1,30)
        if quantidade<10:
            comissao=quantidade*5000
            desconto_inss=salario*(8/100)
            salario_liquido=comissao+salario-desconto_inss
            if salario_liquido>=300000:
                desconto=salario_liquido*(5/100)
                salario_liquido=comissao+salario-desconto_inss-desconto
        if quantidade>10:
            comissao=quantidade*10000
            desconto_inss=salario*(8/100)
            salario_liquido=comissao+salario-desconto_inss
        if salario_liquido>=300000:
                desconto=salario_liquido*(5/100)
                salario_liquido=comissao+salario-desconto_inss-desconto
    if cor==2:
        quantidade=random.randint(1,30)
        if quantidade<20:
            comissao=quantidade*2000
            desconto_inss=salario*(8/100)
            salario_liquido=comissao+salario-desconto_inss
        if salario_liquido>=300000:
                desconto=salario_liquido*(5/100)
                salario_liquido=comissao+salario-desconto_inss-desconto
        if quantidade>20:
            comissao=quantidade*4000
            desconto_inss=salario*(8/100)
            salario_liquido=comissao+salario-desconto_inss
        if salario_liquido>=300000:
                desconto=salario_liquido*(5/100)
                salario_liquido=comissao+salario-desconto_inss-desconto
    print('O salário do funcionário de inscrição',i,'é:',salario,'ele tem salario líquido de',salario_liquido)
