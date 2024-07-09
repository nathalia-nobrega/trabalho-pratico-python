"""
    Este arquivo serve para formatar a saída dos dados para o relatório final
"""
from main.estatisticas.estatisticas_turma import getMediasAlunos, calculate_above_average, maior_menor_media


def print_disciplina_dados(disciplinas, alunos):
    print('\t\t\t================================== ESTATÍSTICAS DE CADA TURMA ==================================')
    for key, values in disciplinas.items():
        nome = values[0]
        qtd_alunos = values[1]
        perc_aprovacao = f'{values[2]:.1f}%'
        media_turma = f'{values[3]:.1f}'


        print(f'\n\tDisciplina - {nome}')
        print(f"\t\tCódigo: {key}\n\t\tN° de estudantes: {qtd_alunos}\n\t\t% de aprovados: {perc_aprovacao}\n\t\tMédia da turma: {media_turma}")

        medias_alunos = getMediasAlunos(alunos, key)
        calculate_above_average(float(media_turma), medias_alunos)
        maior_menor_media(alunos, key)
        print('\n\t------------------------------------------------')


    print('\n\t\t\t========================= FIM ESTATÍSTICAS DE CADA TURMA ==================================')
