#- Alunos: nome, matrícula (1238734), data de nascimento, sexo, endereço, telefone, e-mail.
import random
import main

def cadastro_aluno():
    nome = input(f'Qual o nome do aluno(a):')
    data_dia = input(f'em que dia nasceu o aluno(a):')
    data_mes = input(f'em que mes nasceu o aluno(a):')
    data_ano = input(f'em que ano nasceu o aluno(a):')
    sexo = input(f'sexo do aluno(a):')
    endereco = input(f'endereço do aluno(a):')
    tel =  input(f'telefone do aluno(a): ')
    email = input(f'email do aluno(a):')
    
    cod_nome = nome[0].upper()
    matricula = random.randint(1000000,9999999)
    cod_matricula = str(matricula)
    cod_matriculafinal = cod_matricula + cod_nome
    
    lista_aluno = []
    ficha_aluno = {'nome': nome, 'data de nascimento' : f'{data_dia}/{data_mes}/{data_ano}', 'sexo' : sexo, 'endereco' : endereco, 'telefone' : tel, 'email' : email, 'Numero da matricula' : cod_matriculafinal}
    nome_aluno = ficha_aluno['nome']
    lista_aluno.append(nome_aluno)
    
    print(f'cadastro feito com sucesso!\n')
   
    mostrar = input(f'você gostaria de ver como ficou o cadastro?(digite S ou N)')
    mostrar_maiusculo = mostrar[0].upper()
    if mostrar_maiusculo == 'S':
        print (ficha_aluno)
        
    else:
            escolha=input(f'Ok, voce deseja voltar para o inicio?')
            escolha_maiusculo = escolha[0].upper()
    if escolha_maiusculo == 'S':
                print(f'sefsef')
    else:
        print(f'você saiu do GAMPT')

    


    