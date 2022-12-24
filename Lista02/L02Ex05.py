#Declaração variávies
#votostotais : int
#votosnulo : int
#votosnaruto :int
#votossakura : int
#votosshin : int


#Início do programa

votosnaruto= int(input("Digite a quantidade de votos do candidato Naruto: "))
votossakura= int(input("Digite a quantidade de votos da candidata Sakura: "))
votosshin= int(input("Digite a quantidade de votos do candidato Shin: "))
votosnulos= int(input("Digite a quantidade de votos nulos: "))
votostotais= votosnaruto+votossakura+votosshin
if votostotais>votosnulos :
    print("A eleição foi válida")
    if votosnaruto>votossakura and votosnaruto>votosshin :
        print("E o vencedor é o candidato Naruto")
    if votossakura>votosnaruto and votossakura>votosshin :
        print("E o vencedor é a candidata Sakura")
    if votosshin>votosnaruto and votosshin>votossakura :
        print("E o vencedor é o candidato Shin")

else :
    print("A eleição foi inválida, pois a quantidade de votos nulos superou a quantidade de votos válidos.")
 
