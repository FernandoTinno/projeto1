#- Alunos: nome, matrícula (1238734), data de nascimento, sexo, endereço, telefone, e-mail.
import random



def cadastro_aluno():
    
    nome_1 = input(f'Qual o nome do aluno(a):')
    nome_1_certo = nome_1.lower()
    while True:
            try:
                data_dia_1 = int(input(f'em que dia nasceu o aluno(a):'))
                data_mes_1 = int(input(f'em que mes nasceu o aluno(a):'))
                data_ano_1 = int(input(f'em que ano nasceu o aluno(a):'))
                break  
            except ValueError:
                print("\nnão foi possivel cadastrar a data de nascimento, digite números inteiros.\n")
    sexo_1 = input(f'sexo do aluno(a):')
    endereco_1 = input(f'endereço do aluno(a):')
    tel_1 =  input(f'telefone do aluno(a): ')
    email_1 = input(f'email do aluno(a):')
    
    
    letras = 'ABCDE'
    embaralhar_letras_1 = random.choice(letras)
    matricula_1 = random.randint(1000000,9999999)
    cod_matricula_1 = str(matricula_1)
    cod_matriculafinal_1 = cod_matricula_1 + embaralhar_letras_1
    
    
    lista_aluno = []
    ficha_aluno = {'nome_a': nome_1_certo, 'nascimento_a' : f'{data_dia_1}/{data_mes_1}/{data_ano_1}', 'sexo_a' : sexo_1, 'endereco_a' : endereco_1, 'telefone_a' : tel_1, 'email_a' : email_1, 'codigo_a' : cod_matriculafinal_1}
    nome_aluno = ficha_aluno['nome_a']
    lista_aluno.append(nome_aluno)
    
    
    
    print(f'cadastro feito com sucesso!\n')
    
    
    while True:     
            mostrar = input(f'Você gostaria de ver como ficou o cadastro? (digite S ou N):')
            veri_mostrar = mostrar.lower()
            if veri_mostrar == 's':
                    print(f'{ficha_aluno}\n')
                    break      
            elif veri_mostrar == 'n':
                    print(f'Tudo bem!')
                    break
            else:
                    print(f'deu errado')
    
    
    while True:
            mais_1 = input(f'você gosaria de fazer mais uma matricula? Digite S ou N:')
            veri_mais_1 = mais_1.lower()
            if veri_mais_1 == 's':
                while True:
                    nome_2 = input(f'Qual o nome do aluno(a):')
                    nome_2_certo_2 = nome_2.lower()
                    if nome_2_certo_2 in lista_aluno:
                        print(f'esse aluno já foi cadastrado')
                    else:
                        break
                while True:
                    try:
                        data_dia_2 = int(input(f'em que dia nasceu o aluno(a):'))
                        data_mes_2 = int(input(f'em que mes nasceu o aluno(a):'))
                        data_ano_2 = int(input(f'em que ano nasceu o aluno(a):'))
                        break  
                    except ValueError:
                        print("\nnão foi possivel cadastrar a data de nascimento, digite números inteiros.\n")    
                sexo_2 = input(f'sexo do aluno(a):')
                endereco_2 = input(f'endereço do aluno(a):')
                tel_2 =  input(f'telefone do aluno(a): ')
                email_2 = input(f'email do aluno(a):')
                
                
                embaralhar_letras_2 = random.choice(letras)
                matricula_2 = random.randint(1000000,9999999)
                cod_matricula_2 = str(matricula_2)
                cod_matriculafinal_2 = cod_matricula_2 + embaralhar_letras_2
                
                ficha_aluno_2 = {'nome_a': nome_2, 'nascimento_a' : f'{data_dia_2}/{data_mes_2}/{data_ano_2}', 'sexo_a' : sexo_2, 'endereco_a' : endereco_2, 'telefone_a' : tel_2, 'email_a' : email_2, 'codigo_a' : cod_matriculafinal_2}
                nome_aluno_2 = ficha_aluno_2['nome_a']
                lista_aluno.append(nome_aluno_2)
                
                
              
                
                while True:     
                    mostrar_2 = input(f'Você gostaria de ver como ficou o cadastro? (digite S ou N): ')
                    veri_mostrar_2 = mostrar_2.lower()
                    if veri_mostrar_2 == 's':
                        print(f'{ficha_aluno_2}\n')
                        break     
                    elif veri_mostrar_2 == 'n':
                        print(f'Tudo bem!')
                        break
                    else:
                        print(f'deu errado')        
                
                return lista_aluno
            elif veri_mais_1 == 'n':
                print(f'Tudo bem!')
                break
            else:
                print(f'algo deu errado')
                
    while True:
            voltar= input(f'Ok, voce vai voltar para o menu principal(s ou n):').lower()
            
            if voltar == 's':
                return True
            
            elif voltar == 'n':
                return print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n') 
            else:
                print(f'Opção inválida. Por favor, digite S ou N.')
    
    
        


