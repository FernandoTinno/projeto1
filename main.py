import controle
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
    while voltar:
        controle.menu()
        opcao = input("Digite a opção: ")
        if opcao == '1':
            voltar = controle.cadastro_aluno(), controle.voltar_menu()
            
        elif opcao == '2':
            voltar = controle.cadastro_prof(),controle.voltar_menu()
            
        elif opcao == '3':
            voltar = controle.cadastro_materia(),controle.voltar_menu()
            
        elif opcao == '4':
            voltar = controle.cadastro_turma(),controle.voltar_menu()
        
        elif opcao == '5':
            voltar = controle.teste(),controle.voltar_menu()

        elif opcao == '12':
            voltar = False
            print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n')
        


main()


'''
amanha pensar na hierarquia dos processos de matricula. exp: nn pode cadastrar a turma se não houver aluno,professor e disciplina e assim em diante
e pensar como armazenar os cadastros.
'''