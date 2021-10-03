import random
lucro = 0
moto = carro = onibus =0
for veiculo in range(1,401):
    opcao = random.randint(1,3)
    if opcao == 1:
        lucro = lucro + 4
        moto+=1
    elif opcao == 2:
        lucro = lucro + 8
        carro+=1
    elif opcao == 3:
        lucro = lucro + 20
        onibus+=1
    else:
        print('Erro na escolha da opção')
print('O lucro do estacionamento foi R$',lucro, 'e dos 400 veículos que passaram pelo estacionamento:')
print(moto,'foram motos')
print(carro ,'foram carros')
print(onibus, 'foram ônibus')
