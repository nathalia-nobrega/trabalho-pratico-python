"""
    Este módulo fornece funções básicas para o cálculo das estatísticas individuais .
"""
def is_approved(media_aluno, media_disciplina):
    return media_aluno >= media_disciplina

# Taxa de aprovação. Exemplo: Um aluno matriculado em 2 disciplinas
# e que foi aprovado apenas em uma teve 50% de taxa de aprovação

def get_taxa_aprovacao_aluno(matricula, aluno):
    qtd_disciplinas_cursadas = len(aluno['matriculado_em'])
    lista_disc_aprovado = aluno['aprovado']

    qtd_disciplinas_aprovado = 0

    for situacao in lista_disc_aprovado:
        if situacao ==  True:
            qtd_disciplinas_aprovado += 1

    taxa_aprovacao = f'{(qtd_disciplinas_aprovado / qtd_disciplinas_cursadas) * 100:.1f}%'
    format = f'\t# Aproveitamento de {taxa_aprovacao} em {qtd_disciplinas_cursadas} disciplinas'
    return format

def get_maior_media_aluno(aluno, disciplinas):
    medias_aluno = aluno['media']
    disciplinas_cursadas = aluno['matriculado_em']

    maior_media = max(medias_aluno)
    menor_media = min(medias_aluno)

    codigo_maior = disciplinas_cursadas[medias_aluno.index(maior_media)]
    codigo_menor =  disciplinas_cursadas[medias_aluno.index(menor_media)]

    nome_maior = ''
    nome_menor = ''

    for key, value in disciplinas.items():
        if key == codigo_maior:
            nome_maior = value[0]
        elif key == codigo_menor:
            nome_menor = value[0]

    melhor_media = f'\t# Disciplina na qual obteve melhor média: {nome_maior} -- {maior_media:.1f}'
    pior_media = f'\t# Disciplina na qual obteve menor média: {nome_menor} -- {menor_media:.1f}'

    return melhor_media, pior_media
