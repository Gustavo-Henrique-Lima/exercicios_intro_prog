#Declaração de variáveis
#codigo_curso : int
#numeros_vagas : int
#maior_candidatos : int
#porcetagem_mulheres : int
#homens : int
#mulheres : int
#total_candidatos : int
#candidatos_vagas :int
#Início do programa
codigo_curso=1
total_candidatos= candidatos_vagas = valor_total=0
numeros_vagas = homens = mulheres= porcetagem_mulheres =0
maior_candidatos =0
nome_do_maior= ''
codigo_do_maior=0
while codigo_curso!=0:
    codigo_curso=int(input('Digite o código do curso: ')) #Lendo código de curso
    if codigo_curso>0:
        numeros_vagas=int(input('Digite a quantidade de vagas do curso: '))
        if numeros_vagas<1 :
            print('Erro no número de vagas, tente novamente')# Fim da leitura do código
        elif numeros_vagas>0:   #Tratamento da informação de cada curso individualmente
            homens=int(input('Digite a quantidade de homens inscritos: '))
            mulheres=int(input('Digite a quantidade de mulheres inscritas: '))
            valor_total+=homens+mulheres
            total_candidatos=homens+mulheres
            candidatos_vagas=total_candidatos/numeros_vagas
            porcetagem_mulheres=100*(mulheres/total_candidatos)
            print('No curso de número' ,codigo_curso, 'existem: {:.2f} candidatos por vaga'.format(candidatos_vagas))
            print('E {:.2f} % dos inscritos são mulheres'.format(porcetagem_mulheres))#Fim de dados de cursos individuais
            if candidatos_vagas>maior_candidatos: #Descobrindo maior
                maior_candidatos=candidatos_vagas
                codigo_do_maior=codigo_curso

print('O curso com o maior número de candidatos foi o curso' ,codigo_do_maior, 'que teve {:.2f} candidatos por vagas'.format(maior_candidatos))#Dados gerais
print('Ao todo foram :' ,valor_total, 'inscritos no vestibular')

#Fim do programa
