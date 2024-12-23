#Turmas: nome, código (A1234), disciplinas, professor, alunos (lista-matricula).

import random
def cadastro_turma(nome,disciplina,turma_professor,cod_nome):
    
    cod_turma = random.randint(1000000,9999999)
    cod_turmastr = str(cod_turma)
    codfinal_turma = cod_turmastr + cod_nome
   
    ficha_materia = {'turma' : cod_nome, 'disciplina' : disciplina, 'professor responsavel' : turma_professor, 'codigo da turma' : codfinal_turma}
    
    print(f'cadastro feito com sucesso:')
    return ficha_materia

nome = input(f'Qual é a classe da turma? A,B,C,D ou E:')
cod_nome = nome[0].upper()
disciplina = input(f'qual é a disciplina que a turma {cod_nome} possui: ')
turma_professor = input(f'qual professor está responsavel por essa turma: ')

resultado = cadastro_turma(nome,disciplina,turma_professor,cod_nome)

print(resultado)
    