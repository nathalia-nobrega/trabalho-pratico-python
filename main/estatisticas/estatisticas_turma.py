# Extrai dados da disciplina
def extract_discipline_data(file):
    first_line = file.split('\n')[0].split(',')
    second_line = file.split('\n')[1]

    codigo = first_line[0]
    nome = first_line[1]

    media_minima = second_line.split(',')[0]
    peso_um = float(second_line.split(',')[1])
    peso_dois = float(second_line.split(',')[2])
    peso_tres = float(second_line.split(',')[3])
    pesos = [peso_um, peso_dois, peso_tres, media_minima]

    return codigo, nome, pesos


# Calcula o percentual de alunos aprovados na turma, a média da turma e a quantidade de alunos com nota acima da média
def calculate_approved(cod, alunos, pesos, media, qtd_alunos):
    qtd_aprovados = 0
    soma_turma = 0
    medias = get_medias_alunos(alunos, cod)
    for media_aluno in medias:
        soma_turma += media_aluno
        if media_aluno >= media:
            qtd_aprovados += 1

    percentual = (qtd_aprovados / qtd_alunos) * 100
    media_turma = soma_turma / qtd_alunos

    return percentual, media_turma, qtd_aprovados


def calculate_notes(notas, pesos):
    numerador = (notas[0] * pesos[0]) + (notas[1] * pesos[1]) + (notas[2] * pesos[2])
    denominador = pesos[0] + pesos[1] + pesos[2]
    media_aluno = numerador / denominador
    return media_aluno


def calculate_above_average(media_turma, medias_alunos):
    qtd_acima_media = 0
    for media_aluno in medias_alunos:
        if media_aluno > media_turma:
            qtd_acima_media += 1
    format = f'Quantidade de alunos acima da média da turma: {qtd_acima_media}'
    return format


# Pega as médias dos alunos de uma determinada matéria
def get_medias_alunos(alunos, codigo_turma):
    medias = []
    for values in alunos.values():
        if codigo_turma in values['matriculado_em']:
            index = values['matriculado_em'].index(codigo_turma)
            media_aluno = values['media'][index]
            medias.append(media_aluno)
    return medias


def maior_menor_media(alunos, codigo_turma):
    maior_media = 0.0
    maior_media_aluno = ''

    menor_media = 0.0
    menor_media_aluno = ''
    for cont in range(len(alunos)):
        for key, val in alunos.items():
            if codigo_turma in val['matriculado_em']:
                index = val['matriculado_em'].index(codigo_turma)
                media_aluno = val['media'][index]

                if cont == 0:
                    maior_media = media_aluno
                    maior_media_aluno = key

                    menor_media = media_aluno
                    menor_media_aluno = key
                else:
                    if media_aluno > maior_media:
                        maior_media = media_aluno
                        maior_media_aluno = key
                    elif media_aluno < menor_media:
                        menor_media = media_aluno
                        menor_media_aluno = key

    format_maior = f'A maior média da turma: {maior_media:.1f} -- do aluno de matrícula {maior_media_aluno}'
    format_menor = f'A menor média da turma: {menor_media:.1f} -- do aluno de matrícula {menor_media_aluno}'
    return format_maior, format_menor
