#Turmas: nome, código (A1234), disciplinas, professor, alunos (lista-matricula).

import random
def cadastro_turma():
    
    
    while True: 
                letras = list('ABCDE')
                nome = input(f'Qual é a classe da turma? A,B,C,D ou E:')
                cod_nome = nome.upper()
                if cod_nome in letras:
                        break  
                else:
                        print(f'\nA letra que você digitou não se adequa as condições impostas, tente novamente\n')
    disciplina = input(f'qual é a disciplina que a turma {cod_nome} possui: ')
    turma_professor = input(f'qual professor está responsavel por essa turma: ')
    
    
    embaralhar_letra = random.choice(letras)
    turma = random.randint(1000000,9999999)
    cod_turma = str(turma)
    cod_turmafinal = cod_turma + embaralhar_letra
    
    
    lista_turma = []
    ficha_turma = {'turma' : cod_nome, 'disciplina' : disciplina, 'professor responsavel' : turma_professor, 'codigo da turma' : cod_turmafinal}
    nome_turma = ficha_turma['turma']
    lista_turma.append(nome_turma)
    
    
    print(f'cadastro feito com sucesso:')
    
    
    while True:
            
                mostrar = input(f'Você gostaria de ver como ficou o cadastro? (digite S ou N): ')
                veri_mostrar = mostrar.lower()
                if veri_mostrar == 's':
                    print(f'{ficha_turma}\n')
                    break      
                elif veri_mostrar == 'n':
                    print(f'Tudo bem!')
                    break
                else:
                    print(f'deu errado')
   
    while True:
            voltar= input(f'Ok, voce vai voltar para o menu principal(s ou n):').lower()
            
            if voltar == 's':
                return True
            
            elif voltar == 'n':
                return print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n') 
            else:
                print(f'Opção inválida. Por favor, digite S ou N.')

 

