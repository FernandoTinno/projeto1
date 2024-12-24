#Turmas: nome, código (A1234), disciplinas, professor, alunos (lista-matricula).

import random
def cadastro_turma():
    nome = input(f'Qual é a classe da turma? A,B,C,D ou E:')
    cod_nome = nome[0].upper()
    disciplina = input(f'qual é a disciplina que a turma {cod_nome} possui: ')
    turma_professor = input(f'qual professor está responsavel por essa turma: ')
    
    
    letras = 'ABCDE'
    embaralhar_letra = random.choice(letras)
    turma = random.randint(1000000,9999999)
    cod_turma = str(turma)
    cod_turmafinal = cod_turma + embaralhar_letra
    
    
    lista_turma = []
    ficha_turma = {'turma' : cod_nome, 'disciplina' : disciplina, 'professor responsavel' : turma_professor, 'codigo da turma' : cod_turmafinal}
    nome_turma = ficha_turma['turma']
    lista_turma.append(nome_turma)
    
    
    print(f'cadastro feito com sucesso:')
    
    
    mostrar = input(f'você gostaria de ver como ficou o cadastro?(digite S ou N)')
    veri_mostrar = mostrar.lower()
    
    if veri_mostrar == 's':
        print (f'{ficha_turma}\n')
    else:
        print(f'Tudo bem!')
        
    voltar= input(f'Ok, voce vai voltar para o menu principal(s ou n):')
    if voltar == 's':
        return True
    else:
        return print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n')

 

    