#Disciplinas: nome, código (A1234), carga horária, professor.

import random
def cadastro_materia():
    
    
    nome = input(f'Qual o nome da materia:')
    while True:
            try:
                carga = int(input(f'digite o valor inteiro de carga horaria(semanal) relacionado a materia: '))
                break  
            except ValueError:
                print("\nnão foi possivel cadastrar as horas, digite um numero inteiro.\n")
    materia_professor = input(f'qual professor está responsavel por essa materia: ')
    

    letras = 'ABCDE'
    embaralhar_letra = random.choice(letras)
    materia = random.randint(1000000,9999999)
    cod_materia = str(materia)
    cod_materiafinal = cod_materia + embaralhar_letra
   
   
    ficha_materia = {'nome_materia' : nome, 'carga_materia' : carga, 'professor_materia' : materia_professor, 'codigo_materia' : cod_materiafinal}
    lista_materia = []
    nome_materia = ficha_materia['nome_materia']
    lista_materia.append(nome_materia)
    
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
                    print(f'deu errado')
   
    while True:
            voltar= input(f'Ok, voce vai voltar para o menu principal(s ou n):').lower()
            
            if voltar == 's':
                return True
            
            elif voltar == 'n':
                return print(f'\nVocê saiu do GAMPT, obrigado e volte sempre!\n') 
            else:
                print(f'Opção inválida. Por favor, digite S ou N.')

    



