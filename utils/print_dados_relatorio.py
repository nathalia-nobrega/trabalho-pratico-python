"""
    Este arquivo serve para formatar a saída dos dados para o relatório final
"""
import main.estatisticas.estatisticas_global as glb
import main.estatisticas.estatisticas_turma as tur


def print_disciplina_dados(disciplinas, alunos):
    print('\t\t\t================================== ESTATÍSTICAS DE CADA TURMA ==================================')
    for key, values in disciplinas.items():
        nome = values[0]
        qtd_alunos = values[1]
        perc_aprovacao = f'{values[2]:.1f}%'
        media_turma = f'{values[3]:.1f}'
        medias_alunos = tur.getMediasAlunos(alunos, key)

        print(f"""
    {nome}, {key}

        # N° de estudantes: {qtd_alunos}
        # % de aprovados: {perc_aprovacao}
        # Média da turma: {media_turma}
        """)
        tur.calculate_above_average(float(media_turma), medias_alunos)
        tur.maior_menor_media(alunos, key)
        print('\n\t------------------------------------------------')


def print_global_dados(disciplinas, alunos):
    print('\n\t\t\t================================== ESTATÍSTICAS GLOBAIS ==================================\n')
    glb.get_media_global(disciplinas)
    glb.get_perc_aprovacao(disciplinas)
    glb.get_alunos_matriculados(alunos)
    glb.get_aprovados_todas_materias(alunos)
    glb.get_taxa_aprovacao(disciplinas)
