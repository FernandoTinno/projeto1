#- Alunos: nome, matrícula (1238734), data de nascimento, sexo, endereço, telefone, e-mail.
import random



def cadastro_aluno():
    
    nome = input(f'Qual o nome do aluno(a):')
    data_dia = input(f'em que dia nasceu o aluno(a):')
    data_mes = input(f'em que mes nasceu o aluno(a):')
    data_ano = input(f'em que ano nasceu o aluno(a):')
    sexo = input(f'sexo do aluno(a):')
    endereco = input(f'endereço do aluno(a):')
    tel =  input(f'telefone do aluno(a): ')
    email = input(f'email do aluno(a):')
    
    
    letras = 'ABCDE'
    embaralhar_letra = random.choice(letras)
    matricula = random.randint(1000000,9999999)
    cod_matricula = str(matricula)
    cod_matriculafinal = cod_matricula + embaralhar_letra
    
    
    lista_aluno = []
    ficha_aluno = {'nome_a': nome, 'nascimento_a' : f'{data_dia}/{data_mes}/{data_ano}', 'sexo_a' : sexo, 'endereco_a' : endereco, 'telefone_a' : tel, 'email_a' : email, 'codigo_a' : cod_matriculafinal}
    nome_aluno = ficha_aluno['nome_a']
    lista_aluno.append(nome_aluno)
    
    
    print(f'cadastro feito com sucesso!\n')
   
   
    while True:
        mostrar = input(f'Você gostaria de ver como ficou o cadastro? (digite S ou N): ')
        veri_mostrar = mostrar.lower()

        if veri_mostrar == 's':
            print(f'{ficha_aluno}\n')
        
            voltar= input(f'Ok, voce vai voltar para o menu principal(s ou n):')
            if voltar == 's':
                return True
            else:
                return print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n')
            
            
        elif veri_mostrar == 'n':
            print(f'Tudo bem!')
            voltar= input(f'Ok, voce vai voltar para o menu principal(s ou n):')
            if voltar == 's':
                return True
            else:
                return print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n')
            
            
        else:
            print(f'Opção inválida. Por favor, digite S ou N.')
           
        
        
#cadastro_aluno()


    