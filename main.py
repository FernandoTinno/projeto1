import controle
import time
'''
- Crie um sistema escolar que permita cadastrar alunos, professores, disciplinas e turmas.
- Alunos: nome, matrícula (1238734), data de nascimento, sexo, endereço, telefone, e-mail.
- Professores: nome, código (A1234), data de nascimento, sexo, endereço, telefone,e-mail, disciplina.
- Disciplinas: nome, código (A1234), carga horária, professor.
- Turmas: nome, código (A1234), disciplinas, professor, alunos (lista-matricula).

- O sistema deve permitir a matrícula de alunos em turmas.
- O sistema deve permitir a alocação de professores em disciplinas.
- O sistema deve permitir a alocação de disciplinas em turmas.

- O sistema deve permitir a filtragem de professores por disciplina.
- O sistema deve permitir a consulta de alunos matriculados em turmas.
- O sistema deve permitir a consulta de professores alocados em disciplinas.
- O sistema deve permitir a consulta de disciplinas alocadas em turmas.

'''

def main():
    voltar = True
    voltar_1 = True
    
    while voltar and voltar_1:
        controle.menu()
        opcao = input("Digite a opção: ")
        if opcao == '1':
            voltar = controle.cadastro_aluno()
            voltar_1 = controle.voltar_menu()
            if voltar_1 == False:
                break
            
        elif opcao == '2':
            voltar = controle.cadastro_prof()
            voltar_1 = controle.voltar_menu()
            if voltar_1 == False:
                break
            
        elif opcao == '3':
            voltar = controle.cadastro_materia()
            voltar_1 = controle.voltar_menu()
            if voltar_1 == False:
                break
            
        elif opcao == '4':
            voltar = controle.cadastro_turma()
            voltar_1 = controle.voltar_menu()
            if voltar_1 == False:
                break
       
        
        
        elif opcao == '5':
            voltar = controle.mesclar_aluno_turma()
            
            if voltar == False:
                print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n')    
                break
            elif voltar == True:
                voltar_1 = main()
            elif voltar != True or False:
                voltar_1 = controle.voltar_menu()    
            
            
        elif opcao == '6':
            voltar = controle.mesclar_disciplina_prof()
            
            if voltar == False:
                print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n')    
                break
            elif voltar == True:
                voltar_1 = main()
            elif voltar != True or False:
                voltar_1 = controle.voltar_menu()
                
        elif opcao == '7':
            voltar = controle.mesclar_disciplina_turma()
            
            if voltar == False:
                print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n')    
                break
            elif voltar == True:
                voltar_1 = main()
            elif voltar != True or False:
                voltar_1 = controle.voltar_menu()

        elif opcao == '12':
            voltar = False
            voltar_1 = False
            print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n')
        
        else:
            print(f'opção invalida, reiniciando sistema:')
            time.sleep(2)


main()


'''
amanha pensar na hierarquia dos processos de matricula. exp: nn pode cadastrar a turma se não houver aluno,professor e disciplina e assim em diante
e pensar como armazenar os cadastross.
'''