# Exercicio 3)
alunos = {}
alunos['nome'] = str(input('Escreva o nome do aluno.'))
alunos['media'] = float(input('Escreva a media do aluno.'))
if alunos['media'] >= 50:
    print('Aprovado')
    alunos['situacao'] = 'AP'
if alunos['media'] < 50:
    print('Reprovado')
    alunos['situacao'] = 'RP'
    
print(alunos)