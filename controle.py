import random
import time
aluno_lista = []
prof_lista = []
materia_lista = []
turma_lista = []
turma_completa_a = {}
turma_completa_b = {}
turma_completa_c = {}
turma_completa_d = {}
turma_completa_e = {}
prof_materia = {}
prof_materia_2 = {}
materia_repetida = []




def menu():
    

    print(f'\nbem-vindo ao G.A.M.P.T(Gerenciador de Alunos, Matérias, Professores e Turmas)\n')
    time.sleep(1)
    print(f'quais serviços do GAMPT você deseja acessar?\n')
    time.sleep(1)

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
    
    
    while True:
        nome_1 = input(f'Qual o nome do aluno(a):')
        nome_1_certo = nome_1.lower()
        if nome_1_certo in aluno_lista:
            print(f'o aluno {nome_1} já está cadastrado no sistema, realize o cadastro de outro aluno(a)')
        else:
            break
    
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
    
    
    
    ficha_aluno = {'nome do aluno': nome_1_certo, 'nascimento' : f'{data_dia_1}/{data_mes_1}/{data_ano_1}', 'sexo' : sexo_1, 'endereco' : endereco_1, 'telefone' : tel_1, 'email' : email_1, 'codigo' : cod_matriculafinal_1}
    aluno_lista.append(ficha_aluno['nome do aluno'])
    
    
    
    
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
                    nome_2_certo = nome_2.lower()
                    if nome_2_certo in aluno_lista:
                        print(f'o aluno {nome_2} já está cadastrado no sistema, realize o cadastro de outro aluno(a)')  
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

    while True:
        nome = input(f'Qual o nome do professor(a):')
        nome_1_certo = nome.lower()
        if nome_1_certo in prof_lista:
            print(f'o professor {nome} já está cadastrado no sistema, realize o cadastro de outro aluno(a)')
        else:
            break
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
                    nome_2 = input(f'Qual o nome do professor(a):')
                    nome_2_certo = nome_2.lower()
                    if nome_2_certo in prof_lista:
                        print(f'o professor {nome_2} já está cadastrado no sistema, realize o cadastro de outro professor(a)')
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
                return prof_lista
            
            else:
                print(f'digite S ou N')
    



def cadastro_materia():
    global materia_lista
    
    
    while True:
        nome = input(f'Qual o nome da materia:')
        nome_1_certo = nome.lower()
        if nome_1_certo in materia_lista:
            print(f'a materia {nome} já está cadastrado no sistema, realize o cadastro de outra materia:')
        else:
            break
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
                    nome_2_certo = nome_2.lower()
                    if nome_2_certo in materia_lista:
                        print(f'a materia {nome_2} já está cadastrado no sistema, realize o cadastro de outra materia')
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
                        print(f'{ficha_materia_2}\n')
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
            while True:
                escolha = input(f'voce quer voltar para o menu (S ou N):')
                veri_escolha = escolha.lower()
                if veri_escolha == 's':
                    return True
                elif veri_escolha == 'n':
                    return False
                else:
                    print(f'tente novamente, digite S ou N')
            
            
        elif not turma_lista:
            print(f'Você não cadastrou uma turma')
            while True:
                escolha = input(f'voce quer voltar para o menu (S ou N):')
                veri_escolha = escolha.lower()
                if veri_escolha == 's':
                    return True
                elif veri_escolha == 'n':
                    return False
                else:
                    print(f'tente novamente, digite S ou N')
            
            
        else:
            print(f'turmas cadastradas: {turma_lista}\nalunos matriculados: {aluno_lista}')
            escolhe_turma = input(f'qual turma você deseja alocar o aluno:')
            escolhe_turma_certo = escolhe_turma.upper()

            
            if escolhe_turma_certo in turma_lista:
                print(f'turma escolhida')        
            else:
                print(f'a turma escolhida não consta no sistema, volte para o menu e realize um cadastro de acordo com o esperado')
                time.sleep(1)
                return True
                  
                    
            escolhe_aluno = input(f'aloque um aluno para a turma {escolhe_turma_certo}: ')
            escolhe_aluno_certo = escolhe_aluno.lower()
            if escolhe_aluno_certo in aluno_lista:
                print(f'aluno escolhido')
            else:
                print(f'o aluno {escolhe_aluno} não está cadastrado no sistema,volte para o menu e realize o cadastro do mesmo')
                time.sleep(1)
                return True


            if escolhe_turma_certo == 'A':
                alunos_a.append(escolhe_aluno_certo)
                turma_completa_a.update({'nome da turma' : escolhe_turma_certo, 'alunos' : alunos_a})
                print(f'cadastro feito com sucesso, aqui está a turma A:\n')
                print(turma_completa_a)
                

            if escolhe_turma_certo == 'B':
                alunos_b.append(escolhe_aluno_certo)
                turma_completa_b = {'nome da turma' : escolhe_turma_certo, 'alunos' : alunos_b}
                print(f'cadastro feito com sucesso, aqui está a turma B:\n')
                print(turma_completa_b)


            if escolhe_turma_certo == 'C':
                alunos_c.append(escolhe_aluno_certo)
                turma_completa_c = {'nome da turma' : escolhe_turma_certo, 'alunos' : alunos_c}
                print(f'cadastro feito com sucesso, aqui está a turma C:\n')
                print(turma_completa_c)


            if escolhe_turma_certo == 'D':
                alunos_d.append(escolhe_aluno_certo)
                turma_completa_d = {'nome da turma' : escolhe_turma_certo, 'alunos' : alunos_d}
                print(f'cadastro feito com sucesso, aqui está a turma D:\n')
                print(turma_completa_d)


            if escolhe_turma_certo == 'E':  
                alunos_e.append(escolhe_aluno_certo)
                turma_completa_e = {'nome da turma' : escolhe_turma_certo, 'alunos' : alunos_e}
                print(f'cadastro feito com sucesso, aqui está a turma D:\n')
                print(turma_completa_e)
            
            
            while True:
                mais_1 = input(f'você gosaria de fazer mais uma matricula? Digite S ou N:')
                veri_mais_1 = mais_1.lower()

                if veri_mais_1 == 's': 
                    
                    print(f'turmas cadastradas: {turma_lista}\nalunos matriculados: {aluno_lista}')
                    escolhe_turma_2 = input(f'qual turma você deseja alocar o aluno:')
                    escolhe_turma_certo_2 = escolhe_turma_2.upper()

                    if escolhe_turma_certo_2 in turma_lista:
                        print(f'turma escolhida')        
                    else:
                        print(f'a turma escolhida não consta no sistema, volte para o menu e realize um cadastro de acordo com o esperado')
                        time.sleep(1)
                        return True
                        
                            
                     
                    while True:
                        escolhe_aluno_2 = input(f'aloque um aluno para a turma {escolhe_turma_certo_2}: ')
                        escolhe_aluno_certo_2 = escolhe_aluno_2.lower()
                        if escolhe_aluno_certo_2 == escolhe_aluno_certo:
                            
                            print(f'esse aluno já está cadastrado, tente outro aluno')
                            
                        elif escolhe_aluno_certo_2 in aluno_lista:
                            print(f'aluno escolhido')
                            break
                        else:
                            print(f'o aluno {escolhe_aluno_2} não está cadastrado no sistema,volte para o menu e realize o cadastro do mesmo')
                            time.sleep(1)
                            return True
                    
                    if escolhe_turma_certo_2 == 'A':
                        alunos_a.append(escolhe_aluno_certo_2)
                        turma_completa_a.update({'nome da turma' : escolhe_turma_certo_2, 'alunos' : alunos_a})
                        print(f'cadastro feito com sucesso, aqui está a turma A:\n')
                        print(turma_completa_a)
                        return turma_completa_a
                        
                    

                    if escolhe_turma_certo_2 == 'B':
                        alunos_b.append(escolhe_aluno_certo_2)
                        turma_completa_b = {'nome da turma' : escolhe_turma_certo_2, 'alunos' : alunos_b}
                        print(f'cadastro feito com sucesso, aqui está a turma B:\n')
                        print(turma_completa_b)
                        return turma_completa_b

                    if escolhe_turma_certo_2 == 'C':
                        alunos_c.append(escolhe_aluno_certo_2)
                        turma_completa_c = {'nome da turma' : escolhe_turma_certo_2, 'alunos' : alunos_c}
                        print(f'cadastro feito com sucesso, aqui está a turma C:\n')
                        print(turma_completa_c)
                        return turma_completa_c

                    if escolhe_turma_certo_2 == 'D':
                        alunos_d.append(escolhe_aluno_certo_2)
                        turma_completa_d = {'nome da turma' : escolhe_turma_certo_2, 'alunos' : alunos_d}
                        print(f'cadastro feito com sucesso, aqui está a turma D:\n')
                        print(turma_completa_d)
                        return turma_completa_d

                    if escolhe_turma_certo_2 == 'E':  
                        alunos_e.append(escolhe_aluno_certo_2)
                        turma_completa_e = {'nome da turma' : escolhe_turma_certo_2, 'alunos' : alunos_e}
                        print(f'cadastro feito com sucesso, aqui está a turma e:\n')
                        print(turma_completa_e)
                        return turma_completa_e
                    
                
                elif veri_mais_1 == 'n':
                    print(f'Tudo bem!')
        
                    if escolhe_turma_certo == 'A':
                        return turma_completa_a
                    
                    elif escolhe_turma_certo == 'B':
                        return turma_completa_b
                    
                    elif escolhe_turma_certo == 'C':
                        return turma_completa_c
                    
                    elif escolhe_turma_certo == 'D':
                        return turma_completa_d
                    
                    elif escolhe_turma_certo == 'E':
                        return turma_completa_e
                    
                    
                else:
                    print(f'digite S ou N')

        
def mesclar_disciplina_prof():
    global materia_lista
    global prof_lista
    global prof_materia
    global prof_materia_2
    global materia_repetida
    
    
    while True:
        if not materia_lista:
            print(f'Você não cadastrou nenhuma materia')
            
            while True:
                escolha = input(f'voce quer voltar para o menu (S ou N):')
                veri_escolha = escolha.lower()
                if veri_escolha == 's':
                    return True
                elif veri_escolha == 'n':
                    return False
                else:
                    print(f'tente novamente, digite S ou N')
            
            
        elif not prof_lista:
            print(f'Você não cadastrou nenhum professor(a)')
            
            while True:
                escolha = input(f'voce quer voltar para o menu (S ou N):')
                veri_escolha = escolha.lower()
                if veri_escolha == 's':
                    return True
                elif veri_escolha == 'n':
                    return False
                else:
                    print(f'tente novamente, digite S ou N')
                    
        else:
            
            
            while True:
                    print(f'materias cadastradas: {materia_lista}\nprofessores efetivados: {prof_lista}\n')
                    escolhe_materia = input(f'qual materia você deseja alocar o professor:')
                    escolhe_materia_certo = escolhe_materia.lower()
                        
                    if escolhe_materia_certo in materia_repetida :
                        print(f'essa materia já possui um professor\n')
                            
                    elif escolhe_materia_certo in materia_lista:
                        print(f'materia escolhida')
                        break
                    else:
                        print(f'a materia {escolhe_materia} não está cadastrada no sistema,volte para o menu e realize o cadastro do mesmo')
                        time.sleep(1)
                        return True
            
            
            escolhe_prof = input(f'aloque um professor para a materia {escolhe_materia}: ')
            escolhe_prof_certo = escolhe_prof.lower()
            if escolhe_prof_certo in prof_lista:            
                print(f'professor escolhido com sucesso!')
                            
            else:
                print(f'o professor(a) {escolhe_prof} não está cadastrado no sistema,volte para o menu e realize o cadastro do mesmo')
                time.sleep(1)
                return True
            
            prof_materia = {'nome do professor' : escolhe_prof, 'disciplina do professor' : escolhe_materia}
            print(f'Você atribuiu uma materia a um professor, aqui está o cadastro:\n')
            materia_repetida.append(escolhe_materia_certo)
            print(prof_materia)
            
            while True:
                mais_1 = input(f'você gosaria de fazer mais uma matricula? Digite S ou N:')
                veri_mais_1 = mais_1.lower()

                if veri_mais_1 == 's':        
                    
                    while True:
                        print(f'materias cadastradas: {materia_lista}\nprofessores efetivados: {prof_lista}')
                        escolhe_materia_2 = input(f'qual materia você deseja alocar o professor:')
                        escolhe_materia_certo_2 = escolhe_materia_2.lower()
                        
                        if escolhe_materia_certo_2 == prof_materia['disciplina do professor']:
                            print(f'essa materia já possui um professor')
                        
                        elif escolhe_materia_certo_2 in materia_repetida:
                            print(f'essa materia já possui um professor')
                            
                        elif escolhe_materia_certo_2 in materia_lista:
                            print(f'materia escolhida')
                            break
                        else:
                            print(f'a materia {escolhe_materia_2} não está cadastrada no sistema,volte para o menu e realize o cadastro do mesmo')
                            time.sleep(1)
                            return True
                    
                    escolhe_prof_2 = input(f'aloque um professor para a materia {escolhe_materia_2}: ')
                    escolhe_prof_certo_2 = escolhe_prof_2.lower()
                    if escolhe_prof_certo_2 in prof_lista:            
                        print(f'professor escolhido com sucesso!')
                      
                        prof_materia_2 = {'nome do professor' : escolhe_prof_2, 'disciplina do professor' : escolhe_materia_2}
                        print(f'Você atribuiu uma materia a um professor, aqui está o cadastro:\n')
                        materia_repetida.append(escolhe_materia_certo_2)
                        print(prof_materia_2)
                        return prof_materia_2
                      
                                    
                    else:
                        print(f'o professor(a) {escolhe_prof_2} não está cadastrado no sistema,volte para o menu e realize o cadastro do mesmo')
                        time.sleep(1)
                        return True
                    
                    
                elif veri_mais_1 == 'n':
                    print(f'Tudo bem!')
                    return prof_materia
                    
                else:
                    print(f'digite S ou N')

            

def mesclar_disciplina_turma():
    
    global materia_lista
    global turma_lista
    global turma_completa_a
    
    #print(f'7-Atribuir uma disciplina a uma turma')
    
    while True:
        if not materia_lista:
            print(f'para realizar esse procedimento, cadastre um aluno,materia,turma e por fim cadastre o aluno em uma turma')     
            
            while True:
                escolha = input(f'voce quer voltar para o menu (S ou N):')
                veri_escolha = escolha.lower()
                if veri_escolha == 's':
                    return True
                elif veri_escolha == 'n':
                    return False
                else:
                    print(f'tente novamente, digite S ou N')
            
            
        elif not turma_lista:
            print(f'para realizar esse procedimento, cadastre um aluno,materia,turma e por fim cadastre o aluno em uma turma')     
            
            while True:
                escolha = input(f'voce quer voltar para o menu (S ou N):')
                veri_escolha = escolha.lower()
                if veri_escolha == 's':
                    return True
                elif veri_escolha == 'n':
                    return False
                else:
                    print(f'tente novamente, digite S ou N')
                    
                    
        elif not aluno_lista:
            print(f'para realizar esse procedimento, cadastre um aluno,materia,turma e por fim cadastre o aluno em uma turma')   
            
            while True:
                escolha = input(f'voce quer voltar para o menu (S ou N):')
                veri_escolha = escolha.lower()
                if veri_escolha == 's':
                    return True
                elif veri_escolha == 'n':
                    return False
                else:
                    print(f'tente novamente, digite S ou N')       
                     
        else:
            print(f'aqui estão as Turmas\n{turma_lista}\n e materias {materia_lista}')
            
            escolha_turma = input(f'qual das turmas você deseja atribuir uma materia: ')
            escolha_turma_certa = escolha_turma.upper()
            
            if escolha_turma_certa in turma_lista:
                print(f'Turma escolhida!')
                
            else: 
                print(f'a turma {escolha_turma_certa} não está cadastrada, volte para o menu e realize o cadastro do mesmo')
                time.sleep(1)
                return True
            
            escolha_materia = input(f'qual a materia que sera atribuida para a turma {escolha_turma_certa}: ')
            escolha_materia_certa = escolha_materia.lower()
            
            if escolha_materia_certa in materia_lista:
                print(f'materia escolhida!')
                
            else:
                print(f'a materia {escolha_materia_certa} não está cadastrada, volte para o menu e realize o cadastro do mesmo')
                time.sleep(1)
                return True
            
            if escolha_turma_certa == 'A':
                novo_turma_completa_a = turma_completa_a.copy()
                novo_turma_completa_a.update({'materia da classe' : escolha_materia})
                print(novo_turma_completa_a)
                return novo_turma_completa_a
            
            if escolha_turma_certa == 'B':
                novo_turma_completa_b = turma_completa_b.copy()
                novo_turma_completa_b.update({'materia da classe' : escolha_materia})
                print(novo_turma_completa_b)
                return novo_turma_completa_b
            
            if escolha_turma_certa == 'C':
                novo_turma_completa_c = turma_completa_c.copy()
                novo_turma_completa_c.update({'materia da classe' : escolha_materia})
                print(novo_turma_completa_c)
                return novo_turma_completa_c
            
            if escolha_turma_certa == 'D':
                novo_turma_completa_d = turma_completa_d.copy()
                novo_turma_completa_d.update({'materia da classe' : escolha_materia})
                print(novo_turma_completa_d)
                return novo_turma_completa_d
            
            if escolha_turma_certa == 'E':
                novo_turma_completa_e = turma_completa_e.copy()
                novo_turma_completa_e.update({'materia da classe' : escolha_materia})
                print(novo_turma_completa_e)
                return novo_turma_completa_e
            
            
            while True:
                mais_1 = input(f'você gosaria de fazer mais uma matricula? Digite S ou N:')
                veri_mais_1 = mais_1.lower()

                if veri_mais_1 == 's':  
                    
                    
                    
                    
                    print(f'aqui estão as Turmas\n{turma_lista}e disciplinas{materia_lista}')
            
                    escolha_turma_2 = input(f'qual das turmas você deseja atribuir uma materia: ')
                    escolha_turma_certa_2 = escolha_turma_2.upper()
                    
                    if escolha_turma_certa_2 in turma_lista:
                        print(f'Turma escolhida!')
                        
                    else: 
                        print(f'a turma {escolha_turma_certa_2} não está cadastrada, volte para o menu e realize o cadastro do mesmo')
                        time.sleep(1)
                        return True
                    
                    escolha_materia_2 = input(f'qual a materia que sera atribuida para a turma {escolha_turma_certa_2}: ')
                    escolha_materia_certa_2 = escolha_materia_2.lower()
                    
                    if escolha_materia_certa_2 in materia_lista:
                        print(f'materia escolhida!')
                        
                    else:
                        print(f'a materia {escolha_materia_certa_2} não está cadastrada, volte para o menu e realize o cadastro do mesmo')
                        time.sleep(1)
                        return True
                    
                    if escolha_turma_certa == 'A':
                        novo_turma_completa_a = turma_completa_a.copy()
                        novo_turma_completa_a.update({'materia da classe' : escolha_materia})
                        print(novo_turma_completa_a)
                        return novo_turma_completa_a
                    
                    if escolha_turma_certa == 'B':
                        novo_turma_completa_b = turma_completa_b.copy()
                        novo_turma_completa_b.update({'materia da classe' : escolha_materia})
                        print(novo_turma_completa_b)
                        return novo_turma_completa_b
                    
                    if escolha_turma_certa == 'C':
                        novo_turma_completa_c = turma_completa_c.copy()
                        novo_turma_completa_c.update({'materia da classe' : escolha_materia})
                        print(novo_turma_completa_c)
                        return novo_turma_completa_c
                    
                    if escolha_turma_certa == 'D':
                        novo_turma_completa_d = turma_completa_d.copy()
                        novo_turma_completa_d.update({'materia da classe' : escolha_materia})
                        print(novo_turma_completa_d)
                        return novo_turma_completa_d
                    
                    if escolha_turma_certa == 'E':
                        novo_turma_completa_e = turma_completa_e.copy()
                        novo_turma_completa_e.update({'materia da classe' : escolha_materia})
                        print(novo_turma_completa_e)
                        return novo_turma_completa_e
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
   
                    
                    
                    
                elif veri_mais_1 == 'n':
                    print(f'Tudo bem!')
        
                    if escolha_turma_certa == 'A':
                        return novo_turma_completa_a
                    
                    elif escolha_turma_certa == 'B':
                        return novo_turma_completa_b
                    
                    elif escolha_turma_certa == 'C':
                        return novo_turma_completa_c
                    
                    elif escolha_turma_certa == 'D':
                        return novo_turma_completa_d
                    
                    elif escolha_turma_certa == 'E':
                        return novo_turma_completa_e
                    
            
                else:
                    print(f'digite S ou N')











def voltar_menu():
    while True:
                voltar= input(f'Ok, voce vai voltar para o menu principal(s ou n):')
                veri_voltar = voltar.lower()
                        
                if veri_voltar == 's':
                    return True
                        
                elif veri_voltar == 'n':
                    print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n') 
                    return False
                else:
                    print(f'Opção inválida. Por favor, digite S ou N.')
    