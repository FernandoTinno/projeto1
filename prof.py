#Professores: nome, código (A1234), data de nascimento, sexo, endereço, telefone,e-mail, disciplina.

import random
def cadastro_prof():
    nome = input(f'Qual o nome do professor(a):')
    data_dia = input(f'em que dia nasceu o professor(a):')
    data_mes = input(f'em que mes nasceu o professor(a):')
    data_ano = input(f'em que ano nasceu o professor(a):')
    sexo = input(f'sexo do professor(a):')
    endereco = input(f'endereço do professor(a):')
    tel =  input(f'telefone do professor(a): ')
    email = input(f'email do professor(a):')
    disciplina = input(f'o professor(a) ministra qual disciplina:')
    
    
    letras = 'ABCDE'
    embaralhar_letra = random.choice(letras)
    prof = random.randint(1000000,9999999)
    cod_prof = str(prof)
    cod_proffinal = cod_prof + embaralhar_letra
    
    
    ficha_prof = {'nome_p': nome, 'nascimento_p' : f'{data_dia}/{data_mes}/{data_ano}', 'sexo_p' : sexo, 'endereco_p' : endereco, 'telefone_p' : tel, 'email_p' : email, 'disciplina_p' : disciplina , 'codigo_p' : cod_proffinal}
    
    
    print(f'cadastro feito com sucesso:')
    
    mostrar = input(f'você gostaria de ver como ficou o cadastro?(digite S ou N)')
    veri_mostrar = mostrar.lower()
    
    if veri_mostrar == 's':
        print (f'{ficha_aluno}\n')
    elif veri_mostrar == 'n':
        print(f'Tudo bem!')
    else:
        return mostrar
        
    voltar= input(f'Ok, voce vai voltar para o menu principal(s ou n):')
    if voltar == 's':
        return True
    else:
        return print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n')





    