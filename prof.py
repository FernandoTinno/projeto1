#Professores: nome, código (A1234), data de nascimento, sexo, endereço, telefone,e-mail, disciplina.

import random
def cadastro_prof():
    nome = input(f'Qual o nome do professor(a):')
    while True:
            try:
                data_dia = int(input(f'em que dia nasceu o professor(a):'))
                data_mes = int(input(f'em que mes nasceu o professor(a):'))
                data_ano = int(input(f'em que ano nasceu o professor(a):'))
                break  
            except ValueError:
                print("\nnão foi possivel cadastrar a data de nascimento, digite números inteiros.\n")
    sexo = input(f'digite o sexo do professor(a):')
    endereco = input(f'endereço do professor(a):')
    tel =  input(f'telefone do professor(a): ')
    email = input(f'email do professor(a):')
    disciplina = input(f'o professor(a) ministra qual disciplina:')
    
    
    letras = 'ABCDE'
    embaralhar_letra = random.choice(letras)
    prof = random.randint(1000000,9999999)
    cod_prof = str(prof)
    cod_proffinal = cod_prof + embaralhar_letra
    
    
    
    ficha_prof = {'nome_professor': nome, 'nascimento_professor' : f'{data_dia}/{data_mes}/{data_ano}', 'sexo_professor' : sexo, 'endereco_professor' : endereco, 'telefone_professor' : tel, 'email_professor' : email, 'disciplina_professor' : disciplina , 'codigo_professor' : cod_proffinal}
    lista_prof = []
    nome_prof = ficha_prof['nome_professor']
    lista_prof.append(nome_prof)
    '''
    se eu precisar colocar mais de um valor em uma lista
    nome_prof = ficha_prof['nome_professor']
    idade_prof = ficha_prof['nascimento_professor']
    lista_prof.append(f'{nome_prof}, {idade_prof}')
    '''
    
    
    print(f'cadastro feito com sucesso:\n')
    
    
    while True:
            
                mostrar = input(f'Você gostaria de ver como ficou o cadastro? (digite S ou N): ')
                veri_mostrar = mostrar.lower()
                if veri_mostrar == 's':
                    print(f'{ficha_prof}\n')
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





