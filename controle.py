import aluno
import prof
import materia
import turma
def menu():
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


def chamar_funcao_aluno():
    return aluno.cadastro_aluno()


def chamar_funcao_prof():
    return prof.cadastro_prof()


def chamar_funcao_materia():
    return materia.cadastro_materia()

def chamar_funcao_turma():
    return turma.cadastro_turma()

    