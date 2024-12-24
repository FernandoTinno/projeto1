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
            voltar = controle.chamar_funcao_aluno()
        elif opcao == '12':
            voltar = False
        else:
            print(f'Você saiu do GAMPT')

main()
