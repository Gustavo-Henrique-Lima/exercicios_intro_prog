#Declaração de variáveis
#nota1,nota2,nota3,media,media_turma,nota_turma : float
#matricula,reprovados : int
#frequencia,reprovados_frequencia : int
#menor,maior : float
#nome_maior, nome_menor : string
#Início do programa
menor=100
maior=1
reprovados= reprovados_frequencia= media_turma = porcetagem_reprovados=0
nome_maior= ''
nome_menor= ''
print('*' *5 ,'LEMBRE-SE DE INSERIR NOTAS ENTRE 0-100' , '*' *5)
for i in range(1,101):
    matricula=input('Por favor, digite a matricula do aluno: ') # Início do primeiro bloco, lendo notas e frequências
    nota1=float(input('Digite a primeira nota do aluno: '))
    nota2=float(input('Digite a segunda nota do aluno: '))
    nota3=float(input('Digite a terceira nota do aluno: '))
    frequencia=int(input('Digite a frequência do aluno: '))
    media=(nota1+nota2+nota3)/3
    media_turma+=media
    print('*' *10) #Fim do primeiro bloco após leitura de notas e frequência e retorbi da nota final do aluno
    if media>=60 and frequencia>=40: #Segundo  bloco, aluno aprovado
        print('Matricula:',matricula, 'Frequência:' ,frequencia, 'Média :{:.2f} Parecer : aluno aprovado'.format(media))
    else:
        print('Matricula:',matricula, 'Frequência:' ,frequencia, 'Média :{:.2f} Parecer : aluno reprovado'.format(media))
        reprovados+=1
        if frequencia<40:
            reprovados_frequencia+=1
            porcetagem_reprovados=100*(reprovados_frequencia/100)# Descobrindo porcetagem de reprovados
    if media>maior:#Sexto bloco, maior média da turma
        maior=media
        nome_maior=matricula
    if media<menor:#Sétimo bloco, menor média da turma
        menor=media
        nome_menor=matricula
    print('*' *10)
print('')
print('A média final da turma é: {:.2f} '.format(media_turma/100))
print('A maior nota da turma foi {:.2f} do aluno cuja matrícula é {}'.format(maior,nome_maior))
print('A menor nota da turma foi {:.2f} do aluno cuja matrícula é {}'.format(menor,nome_menor))
if reprovados>0:
    print(reprovados , 'alunos foram reprovados')
    print('Desses, {:.2f} % foram reprovados devido a baixa frequência'.format(porcetagem_reprovados))
elif reprovados<1:
    print('Nenhum aluno foi reprovado')



#Fim do programa
