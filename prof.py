#Professores: nome, código (A1234), data de nascimento, sexo, endereço, telefone,e-mail, disciplina.

import random
def cadastro_prof(nome,data_dia,data_mes,data_ano,sexo,endereco,tel,email,disciplina,cod_nome):
    #fazer com que a letra do codigo do professor seja a primeira letra do nome
    cod_prof = random.randint(1000000,9999999)
    cod_profstr = str(cod_prof)
    codfinal_prof = cod_profstr + cod_nome
    #queria colocar / na data de nascimento mas não sabia fazer, então improvisei 
    ficha_prof = {'nome': nome, 'data de nascimento' : f'{data_dia}/{data_mes}/{data_ano}', 'sexo' : sexo, 'endereco' : endereco, 'telefone' : tel, 'email' : email, 'disciplina' : disciplina , 'Codigo do professor' : codfinal_prof}
    
    print(f'cadastro feito com sucesso:')
    return ficha_prof
nome = input(f'Qual o nome do professor(a):')
data_dia = input(f'em que dia nasceu o professor(a):')
data_mes = input(f'em que mes nasceu o professor(a):')
data_ano = input(f'em que ano nasceu o professor(a):')
sexo = input(f'sexo do professor(a):')
endereco = input(f'endereço do professor(a):')
tel =  input(f'telefone do professor(a): ')
email = input(f'email do professor(a):')
disciplina = input(f'o professor(a) ministra qual disciplina:')
cod_nome = nome[0].upper()

resultado = cadastro_prof(nome,data_dia,data_mes,data_ano,sexo,endereco,tel,email,disciplina,cod_nome)

print(resultado)
    