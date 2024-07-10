# Média global
def get_media_global(disciplinas):
    soma_global = 0.0
    for disciplina in disciplinas.values():
        soma_global += disciplina[3]
    media_global = f'{soma_global / len(disciplinas):.1f}'
    print(f'\t\t# A média global das turmas do professor: {media_global}')

# Percentual de aprovação do professor
def get_perc_aprovacao(disciplinas):
    qtd_aprovados = 0
    qtd_alunos_turma = 0
    for disciplina in disciplinas:
        qtd_aprovados += disciplinas[disciplina][4]
        qtd_alunos_turma += disciplinas[disciplina][1]

    taxa_aprovacao = f'{(qtd_aprovados/qtd_alunos_turma) * 100:.1f}'
    print(f'\t\t# A % de aprovação do professor: {taxa_aprovacao}%')

# Quantidade de alunos matriculados em mais de 2 disciplinas do professor
def get_alunos_matriculados(alunos):
    qtd_matriculados = 0
    for aluno in alunos.values():
        lista_matriculas = aluno['matriculado_em']
        if len(lista_matriculas) > 2:
            qtd_matriculados += 1
    print(f'\t\t# A quantidade de alunos matriculados em mais de 2 disciplinas do professor: {qtd_matriculados}')

# Quantidade e percentual de alunos aprovados em TODAS as disciplinas que estavam matriculados
def get_aprovados_todas_materias(alunos):
    qtd_aprovados_todas = 0
    qtd_alunos = len(alunos)

    for matricula, aluno in alunos.items():
        aprovacao_lista = aluno['aprovado']
        if all(aprovacao_lista):
            qtd_aprovados_todas += 1
    perc_aprovados_todas = f'{(qtd_aprovados_todas / qtd_alunos) * 100:.1f}%'
    print(f'\t\t# A quantidade e o percentual de alunos aprovados em TODAS as disciplinas que estavam matriculados: {qtd_aprovados_todas} ({perc_aprovados_todas})')

# Disciplinas com a maior e a menor taxa de aprovação: Nome e taxa
def get_taxa_aprovacao(disciplinas):
    maior_taxa = 0.0
    nome_maior = ''

    menor_taxa = 0.0
    nome_menor = ''

    for cont in range(len(disciplinas)):
        for value in disciplinas.values():
            if cont == 0:
                maior_taxa = value[2]
                menor_taxa = value[2]

                nome_maior = value[0]
                nome_menor = value[0]
            else:
                if value[2] > maior_taxa:
                    maior_taxa = value[2]
                    nome_maior = value[0]
                elif value[2] < menor_taxa:
                    menor_taxa = value[2]
                    nome_menor = value[0]
    print(f'\t\t# A disciplina com maior taxa de aprovação é {nome_maior}, com {maior_taxa:.1f}% de aprovados')
    print(f'\t\t# A disciplina com menor taxa de aprovação é {nome_menor}, com {menor_taxa:.1f}% de aprovados')
