#No modelo morcego, ele tem que abastecer a cada 16km, são 295km então ele tem que abastecer no mínimo 19 vezes.
#Já no modelo vampior, ele tem que abastecer a cada 11km, são 295km então ele tem que abastecer no mínimo 27 vezes.


#Declaração de variável
#escolha : integer
#valortotal : float

#Início do programa
print("Olá Sr Wayne, o senhor dispõe de duas opções de carro.")
print("1- Modelo morcego, com motor 1.0, que consome um litro de gasolina a cada 16km e o aluguel é de 300$")
print("2- Modelo vampiro voador, com motor 2.0, que consome um litro de gasolina a cada 11km e o aluguel é de 500$")
escolha = int(input("Qual das opções o senhor deseja, 1 ou 2? "))
if escolha==1 :
    valortotal=300+(19*0.75)
    print("O senhor gastou, no total : " , valortotal)
else :
    valortotal=500+(27*0.75)
    print("O senhor gastou, no total : " , valortotal)
