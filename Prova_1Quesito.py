arq=open('nomes.txt','a')
print('*'*30,'Atenção','*'*30)
print('Lembre-se de digitar a palavra ou frase de um mesmo modo, o python não distingue maiúsculo de minúscula')
print('*'*10,'por isso se você começou uma palavra ou frase em MAIÚSCULO FAÇA TODA ELA EM MAIÚSCULA, O MESMO PARA MINÚSCULA','*'*10)
for i in range(1,3):
    frase=input('Digite o nome ou a frase:')
    frase_final=''
    tamanho=(len(frase))
    for i in range(tamanho):
        if frase[i] != ' ':
            frase_final = frase_final + frase[i]
    print(frase_final)
    if frase_final[0]==frase_final[-1:]:
        arq.write(frase_final)
        arq.write('\n')
arq.close()
