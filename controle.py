import random
aluno_lista = []
prof_lista = []
materia_lista = []
turma_lista = []
turma_completa_a = {}
turma_completa_b = {}
turma_completa_c = {}
turma_completa_d = {}
turma_completa_e = {}




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


def cadastro_aluno():
    global aluno_lista
    
    nome_1 = input(f'Qual o nome do aluno(a):')
    nome_1_certo = nome_1.lower()
    while True:
            try:
                data_dia_1 = int(input(f'em que dia nasceu o aluno(a):'))
                data_mes_1 = int(input(f'em que mes nasceu o aluno(a):'))
                data_ano_1 = int(input(f'em que ano nasceu o aluno(a):'))
                break  
            except ValueError:
                print("\nnão foi possivel cadastrar a data de nascimento, digite números inteiros e reescreva a data de nascimento completa do aluno(a).\n") 
    sexo_1 = input(f'sexo do aluno(a):')
    endereco_1 = input(f'endereço do aluno(a):')
    tel_1 =  input(f'telefone do aluno(a): ')
    email_1 = input(f'email do aluno(a):')
    
    
    letras = 'ABCDE'
    embaralhar_letras_1 = random.choice(letras)
    matricula_1 = random.randint(1000000,9999999)
    cod_matricula_1 = str(matricula_1)
    cod_matriculafinal_1 = cod_matricula_1 + embaralhar_letras_1
    
    
    
    ficha_aluno = {'nome_a': nome_1_certo, 'nascimento_a' : f'{data_dia_1}/{data_mes_1}/{data_ano_1}', 'sexo_a' : sexo_1, 'endereco_a' : endereco_1, 'telefone_a' : tel_1, 'email_a' : email_1, 'codigo_a' : cod_matriculafinal_1}
    aluno_lista.append(ficha_aluno['nome_a'])
    
    
    
    
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
                    print(f'digite S ou N')
    
    
    while True:
            mais_1 = input(f'você gosaria de fazer mais uma matricula? Digite S ou N:')
            veri_mais_1 = mais_1.lower()

            if veri_mais_1 == 's':
                while True:
                    nome_2 = input(f'Qual o nome do aluno(a):')
                    nome_2_certo_2 = nome_2.lower()
                    if nome_2_certo_2 in aluno_lista:
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
                        print("\nnão foi possivel cadastrar a data de nascimento, digite números inteiros e reescreva a data de nascimento completa do aluno(a).\n")    
                sexo_2 = input(f'sexo do aluno(a):')
                endereco_2 = input(f'endereço do aluno(a):')
                tel_2 =  input(f'telefone do aluno(a): ')
                email_2 = input(f'email do aluno(a):')
                
                
                embaralhar_letras_2 = random.choice(letras)
                matricula_2 = random.randint(1000000,9999999)
                cod_matricula_2 = str(matricula_2)
                cod_matriculafinal_2 = cod_matricula_2 + embaralhar_letras_2
                
                ficha_aluno_2 = {'nome_a': nome_2, 'nascimento_a' : f'{data_dia_2}/{data_mes_2}/{data_ano_2}', 'sexo_a' : sexo_2, 'endereco_a' : endereco_2, 'telefone_a' : tel_2, 'email_a' : email_2, 'codigo_a' : cod_matriculafinal_2}
                aluno_lista.append(ficha_aluno_2['nome_a'])
                
                
              
                
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
                        print(f'digite S ou N')        




                return aluno_lista   
            elif veri_mais_1 == 'n':
                print(f'Tudo bem!')
                return aluno_lista
            
            else:
                print(f'digite S ou N')
   
    

def cadastro_prof():
    global prof_lista


    nome = input(f'Qual o nome do professor(a):')
    while True:
            try:
                data_dia = int(input(f'em que dia nasceu o professor(a):'))
                data_mes = int(input(f'em que mes nasceu o professor(a):'))
                data_ano = int(input(f'em que ano nasceu o professor(a):'))
                break  
            except ValueError:
                print("\nnão foi possivel cadastrar a data de nascimento, digite números inteiros e reescreva a data de nascimento completa do professor(a).\n") 
    sexo = input(f'digite o sexo do professor(a):')
    endereco = input(f'endereço do professor(a):')
    tel =  input(f'telefone do professor(a): ')
    email = input(f'email do professor(a):')
    
    
    
    letras = 'ABCDE'
    embaralhar_letra = random.choice(letras)
    prof = random.randint(1000000,9999999)
    cod_prof = str(prof)
    cod_proffinal = cod_prof + embaralhar_letra
    
    
    ficha_prof = {'nome_professor': nome, 'nascimento_professor' : f'{data_dia}/{data_mes}/{data_ano}', 'sexo_professor' : sexo, 'endereco_professor' : endereco, 'telefone_professor' : tel, 'email_professor' : email,  'codigo_professor' : cod_proffinal}
    prof_lista.append(ficha_prof['nome_professor'])


    print(f'cadastro realizado com sucesso!')


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
                        print(f'digite S ou N')


    while True:
            mais_1 = input(f'você gosaria de fazer mais uma matricula? Digite S ou N:')
            veri_mais_1 = mais_1.lower()

            if veri_mais_1 == 's':
                while True:
                    nome_2 = input(f'Qual o nome do Professor(a):')
                    nome_2_certo_2 = nome_2.lower()
                    if nome_2_certo_2 in prof_lista:
                        print(f'esse Professor já foi cadastrado')
                    else:
                        break
                while True:
                    try:
                        data_dia_2 = int(input(f'em que dia nasceu o Professor(a):'))
                        data_mes_2 = int(input(f'em que mes nasceu o Professor(a):'))
                        data_ano_2 = int(input(f'em que ano nasceu o Professor(a):'))
                        break  
                    except ValueError:
                        print("\nnão foi possivel cadastrar a data de nascimento, digite números inteiros e reescreva a data de nascimento completa do aluno(a).\n")    
                sexo_2 = input(f'sexo do Professor(a):')
                endereco_2 = input(f'endereço do Professor(a):')
                tel_2 =  input(f'telefone do Professor(a): ')
                email_2 = input(f'email do Professor(a):')
                
                
                
                embaralhar_letras_2 = random.choice(letras)
                prof_2 = random.randint(1000000,9999999)
                cod_prof_2 = str(prof_2)
                cod_proffinal_2 = cod_prof_2 + embaralhar_letras_2
                
                ficha_prof_2 = {'nome_professor': nome_2, 'nascimento_professor' : f'{data_dia_2}/{data_mes_2}/{data_ano_2}', 'sexo_professor' : sexo_2, 'endereco_professor' : endereco_2, 'telefone_professor' : tel_2, 'email_professor' : email_2, 'codigo_professor' : cod_proffinal_2}
                prof_lista.append(ficha_prof_2['nome_professor'])
                
                
              
                
                while True:     
                    mostrar_2 = input(f'Você gostaria de ver como ficou o cadastro? (digite S ou N): ')
                    veri_mostrar_2 = mostrar_2.lower()

                    if veri_mostrar_2 == 's':
                        print(f'{ficha_prof_2}\n')
                        break
                    
                    elif veri_mostrar_2 == 'n':
                        print(f'Tudo bem!')
                        break
                    
                    else:
                        print(f'digite S ou N')        




                return prof_lista
            elif veri_mais_1 == 'n':
                print(f'Tudo bem!')
                return aluno_lista
            
            else:
                print(f'digite S ou N')
    



def cadastro_materia():
    global materia_lista
    
    nome = input(f'Qual o nome da materia:')
    while True:
            try:
                carga = int(input(f'digite o valor inteiro de carga horaria(semanal) relacionado a materia: '))
                break  
            except ValueError:
                print("\nnão foi possivel cadastrar as horas, digite um numero inteiro.\n")

    

    letras = 'ABCDE'
    embaralhar_letra = random.choice(letras)
    materia = random.randint(1000000,9999999)
    cod_materia = str(materia)
    cod_materiafinal = cod_materia + embaralhar_letra
   
   
    ficha_materia = {'nome_materia' : nome, 'carga_materia' : carga, 'codigo_materia' : cod_materiafinal}
    
    materia_lista.append(ficha_materia['nome_materia'])
    
    print(f'cadastro feito com sucesso:\n')
    
    
    while True:
            
            mostrar = input(f'Você gostaria de ver como ficou o cadastro? (digite S ou N): ')
            veri_mostrar = mostrar.lower()
            if veri_mostrar == 's':
                print(f'{ficha_materia}\n')
                break      
            elif veri_mostrar == 'n':
                print(f'Tudo bem!')
                break
            else:
                print(f'digite S ou N')


    while True:
            mais_1 = input(f'você gosaria de fazer mais uma matricula? Digite S ou N:')
            veri_mais_1 = mais_1.lower()

            if veri_mais_1 == 's':
                while True:
                    nome_2 = input(f'Qual o nome da materia:')
                    nome_2_certo_2 = nome_2.lower()
                    if nome_2_certo_2 in prof_lista:
                        print(f'esse Professor já foi cadastrado')
                    else:
                        break
                while True:
                        try:
                            carga_2 = int(input(f'digite o valor inteiro de carga horaria(semanal) relacionado a materia: '))
                            break  
                        except ValueError:
                            print("\nnão foi possivel cadastrar as horas, digite um numero inteiro.\n")
                
                

                letras = 'ABCDE'
                embaralhar_letra_2 = random.choice(letras)
                materia_2 = random.randint(1000000,9999999)
                cod_materia_2 = str(materia_2)
                cod_materiafinal_2 = cod_materia_2 + embaralhar_letra_2
            
            
                ficha_materia_2 = {'nome_materia' : nome_2, 'carga_materia' : carga_2, 'codigo_materia' : cod_materiafinal_2}
                
                materia_lista.append(ficha_materia_2['nome_materia'])
                
                print(f'cadastro feito com sucesso:\n')

                while True:
            
                    mostrar = input(f'Você gostaria de ver como ficou o cadastro? (digite S ou N): ')
                    veri_mostrar = mostrar.lower()
                    if veri_mostrar == 's':
                        print(f'{ficha_materia}\n')
                        break      
                    elif veri_mostrar == 'n':
                        print(f'Tudo bem!')
                        break
                    else:
                        print(f'digite S ou N')


                return materia_lista
            
            elif veri_mais_1 == 'n':
                print(f'Tudo bem!')
                return materia_lista
            
            else:
                print(f'digite S ou N')


    

def cadastro_turma():
    global turma_lista
    
    while True: 
                letras = list('ABCDE')
                nome = input(f'Qual é a classe da turma? A,B,C,D ou E:')
                cod_nome = nome.upper()
                if cod_nome in letras:
                    break  
                else:
                    print(f'\nA letra que você digitou não se adequa as condições impostas, tente novamente\n')

    #disciplina = input(f'qual é a disciplina que a turma {cod_nome} possui: ')
    #turma_professor = input(f'qual professor está responsavel por essa turma: ')
    
    
    embaralhar_letra = random.choice(letras)
    turma = random.randint(1000000,9999999)
    cod_turma = str(turma)
    cod_turmafinal = cod_turma + embaralhar_letra
    
    
    
    ficha_turma = {'turma' : cod_nome, 'codigo da turma' : cod_turmafinal}
    
    turma_lista.append(ficha_turma['turma'])
    
    
    print(f'cadastro feito com sucesso:')
    
    
    while True:
            
                mostrar = input(f'Você gostaria de ver como ficou o cadastro? (digite S ou N): ')
                veri_mostrar = mostrar.lower()
                if veri_mostrar == 's':
                    print(f'{ficha_turma}\n')
                    break      
                elif veri_mostrar == 'n':
                    print(f'Tudo bem!')
                    break
                else:
                    print(f'digite S ou N')

    while True:
            mais_1 = input(f'você gosaria de fazer mais uma matricula? Digite S ou N:')
            veri_mais_1 = mais_1.lower()

            if veri_mais_1 == 's':
                while True: 
                    nome_2 = input(f'Qual é a classe da turma? A,B,C,D ou E:')
                    cod_nome_2 = nome_2.upper()
                    if cod_nome_2 == cod_nome:
                        print(f'a turma {cod_nome} já foi cadastrada, cadastre outra turma')
                    elif cod_nome_2 in letras:
                        break
                    else:
                        print(f'\nA letra que você digitou não se adequa as condições impostas, tente novamente\n')

                embaralhar_letra_2 = random.choice(letras)
                turma_2 = random.randint(1000000,9999999)
                cod_turma_2 = str(turma_2)
                cod_turmafinal_2 = cod_turma_2 + embaralhar_letra_2

                ficha_turma_2 = {'turma' : cod_nome_2, 'codigo da turma' : cod_turmafinal_2}
    
                turma_lista.append(ficha_turma_2['turma'])
                
                
                print(f'cadastro feito com sucesso:')
                
                
                while True:
                        
                            mostrar_2 = input(f'Você gostaria de ver como ficou o cadastro? (digite S ou N): ')
                            veri_mostrar_2 = mostrar_2.lower()
                            if veri_mostrar_2 == 's':
                                print(f'{ficha_turma_2}\n')
                                return turma_lista     
                            elif veri_mostrar_2 == 'n':
                                print(f'Tudo bem!')
                                return turma_lista
                            else:
                                print(f'digite S ou N')

            elif veri_mais_1 == 'n':
                print(f'Tudo bem!')
                return turma_lista
            
            else:
                print(f'digite S ou N')

def mesclar_aluno_turma():
    global turma_lista
    global aluno_lista
    global turma_completa_a
    global turma_completa_b
    global turma_completa_c
    global turma_completa_d
    global turma_completa_e
    alunos_a = []
    alunos_b = []
    alunos_c = []
    alunos_d = []
    alunos_e = []
    while True:
        if not aluno_lista:
            print(f'Você não cadastrou um aluno(a)')
            break
        if not turma_lista:
            print(f'Você não cadastrou uma turma')
            break
        if aluno_lista and turma_lista:
            print(f'turmas cadastradas: {turma_lista}\nalunos matriculados: {aluno_lista}')
            escolhe_turma = input(f'qual turma você deseja alocar o aluno:')
            escolhe_turma_certo = escolhe_turma.upper()

            if escolhe_turma_certo in turma_lista:
                print(f'turma escolhida')        
            else:
                print(f'a turma escolhida não consta no sistema')
                break
                    
            escolhe_aluno = input(f'aloque um aluno para a turma {escolhe_turma_certo}: ')
            escolhe_aluno_certo = escolhe_aluno.lower()
            if escolhe_aluno_certo in aluno_lista:
                print(f'aluno escolhido')
            else:
                print(f'o aluno {escolhe_aluno} não está cadastrado no sistema')
                break

            if escolhe_turma_certo == 'A':
                alunos_a.append(escolhe_aluno_certo)
                turma_completa_a.update({'turma' : escolhe_turma_certo, 'alunos' : alunos_a})
                print(f'cadastro feito com sucesso, aqui está a turma A:\n')
                print(turma_completa_a)
                break

            if escolhe_turma_certo == 'B':
                alunos_a.append(escolhe_aluno_certo)
                turma_completa_b = {'nome da turma' : escolhe_turma_certo, 'alunos' : alunos_b}

            if escolhe_turma_certo == 'C':
                alunos_a.append(escolhe_aluno_certo)
                turma_completa_c = {'nome da turma' : escolhe_turma_certo, 'alunos' : alunos_c}

            if escolhe_turma_certo == 'D':
                alunos_a.append(escolhe_aluno_certo)
                turma_completa_d = {'nome da turma' : escolhe_turma_certo, 'alunos' : alunos_d}

            if escolhe_turma_certo == 'E':  
                alunos_a.append(escolhe_aluno_certo)
                turma_completa_e = {'nome da turma' : escolhe_turma_certo, 'alunos' : alunos_e}
        return turma_completa_a
            

        


            
            
                




def teste():
    global aluno_lista
    global prof_lista
    global materia_lista
    global turma_lista

    lista_teste = {'nome' : aluno_lista}
    print(aluno_lista)
    print(prof_lista)
    print(materia_lista)
    print(turma_lista)
    print(lista_teste)
    












def voltar_menu():
    while True:
                voltar= input(f'Ok, voce vai voltar para o menu principal(s ou n):').lower()
                        
                if voltar == 's':
                    return True
                        
                elif voltar == 'n':
                    print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n') 
                    return False
                else:
                    print(f'Opção inválida. Por favor, digite S ou N.')
    