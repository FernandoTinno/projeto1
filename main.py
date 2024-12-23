import aluno
import materia
import prof
import turma

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
print(f'\nbem-vindo ao G.A.M.P.T(Gerenciador de Alunos, Matérias, Professores e Turmas)\n')

print(f'quais serviços do GAMPT você deseja acessar?\n')

print(f'1-Cadastrar aluno')
print(f'2-Cadastrar Professor')
print(f'3-Cadastrar Materia')
print(f'4-Cadastrar Turma')
print(f'5-Atribuir aluno a uma turma')
print(f'6-Atribuir uma disciplina a um professor')
print(f'7-Atribuir uma disciplina a uma turma')
print(f'8-Filtrar professor por disciplina')
print(f'9-Consultar alunos matriculados em turmas especificas')
print(f'10-Consultar quais são as disciplinas regidas por um professor especifico')
print(f'11-Consultar quais disciplinas estão interligadas a cada turma')
print(f'12-Sair\n')

opcao = input(f'digite o número de acordo com a opção que você deseja:')



