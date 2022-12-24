import random
def inserir_txt():
    arquivo=open("atividade.txt","a")
    arquivo.write(tipo_veiculo)
    arquivo.write(' ')
    arquivo.write(km_rodados)
    arquivo.write('\n')
    arquivo.close()
total_gasolina=0
total_veiculos=0
cont=True
while cont:
    tipo_veiculo=random.randint(1,4)
    km_rodados=random.randint(0,500)
    if tipo_veiculo==1:
        gasolina_gasta=km_rodados/8
        print('O veiculo gastou',gasolina_gasta,'lt de gasolina')
        total_gasolina+=gasolina_gasta
        if km_rodados>0:
            total_veiculos+=1
    if tipo_veiculo==2:
        gasolina_gasta=km_rodados/10
        print('O veiculo gastou',gasolina_gasta,'lt de gasolina')
        total_gasolina+=gasolina_gasta
        if km_rodados>0:
            total_veiculos+=1
    if tipo_veiculo==3:
        gasolina_gasta=km_rodados/15
        print('O veiculo gastou',gasolina_gasta,'lt de gasolina')
        total_gasolina+=gasolina_gasta
        if km_rodados>0:
            total_veiculos+=1
    if tipo_veiculo==4:
        gasolina_gasta=km_rodados/18
        print('O veiculo gastou',gasolina_gasta,'lt de gasolina')
        total_gasolina+=gasolina_gasta
        if km_rodados>0:
            total_veiculos+=1
    print('Deseja continuar?\n1- SIM\nQUALQUER OUTRO VALOR - NÃO')
    escolha=int(input())
    tipo_veiculo=str(tipo_veiculo)
    km_rodados=str(km_rodados)
    inserir_txt()
    if escolha!=1:
        cont=False
        break
arquivo=open('atividade.txt','r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
print('Ao total foram gastos',total_gasolina,'litros de gasolina')
print('Foram locados',total_veiculos,'no total')


