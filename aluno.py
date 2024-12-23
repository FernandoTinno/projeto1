#- Alunos: nome, matrícula (1238734), data de nascimento, sexo, endereço, telefone, e-mail.
import random
def cadastro_aluno(nome,data_dia,data_mes,data_ano,sexo,endereco,tel,email):
    matricula = random.randint(1000000,9999999)
    ficha_aluno = {'nome': nome, 'data de nascimento' : f'{data_dia}/{data_mes}/{data_ano}', 'sexo' : sexo, 'endereco' : endereco, 'telefone' : tel, 'email' : email, 'Numero da matricula' : matricula}
    
    print(f'cadastro feito com sucesso:')
    return ficha_aluno
nome = input(f'Qual o nome do aluno(a):')
data_dia = input(f'em que dia nasceu o aluno(a):')
data_mes = input(f'em que mes nasceu o aluno(a):')
data_ano = input(f'em que ano nasceu o aluno(a):')
sexo = input(f'sexo do aluno(a):')
endereco = input(f'endereço do aluno(a):')
tel =  input(f'telefone do aluno(a): ')
email = input(f'email do aluno(a):')

resultado = cadastro_aluno(nome,data_dia,data_mes,data_ano,sexo,endereco,tel,email)

print(resultado)
    