#Disciplinas: nome, código (A1234), carga horária, professor.

import random
def cadastro_materia(nome,carga,materia_professor,cod_nome):
    
    cod_materia = random.randint(1000000,9999999)
    cod_materiastr = str(cod_materia)
    codfinal_materia = cod_materiastr + cod_nome
   
    ficha_materia = {'nome' : nome, 'carga horaria' : carga, 'professor responsavel pela materia' : materia_professor, 'codigo da materia' : codfinal_materia}
    
    print(f'cadastro feito com sucesso:')
    return ficha_materia

nome = input(f'Qual o nome da materia:')
carga = input(f'Carga horaria(em horas) da diciplina ao longo da semana: ')
materia_professor = input(f'qual professor está responsavel por essa materia: ')
cod_nome = nome[0].upper()

resultado = cadastro_materia(nome,carga,materia_professor,cod_nome)

print(resultado)
    