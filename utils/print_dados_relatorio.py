"""
    Este arquivo serve para formatar a saída dos dados para o relatório final
"""
import main.estatisticas.estatisticas_global as glb
import main.estatisticas.estatisticas_turma as tur
import main.estatisticas.estatisticas_aluno as ind


def write_disciplina_dados(disciplinas, alunos):
    fmt = """
        ================================== ESTATÍSTICAS DE CADA TURMA ==================================
    """
    for key, values in disciplinas.items():
        nome = values[0]
        qtd_alunos = values[1]
        perc_aprovacao = f'{values[2]:.1f}%'
        media_turma = f'{values[3]:.1f}'
        medias_alunos = tur.get_medias_alunos(alunos, key)
        above_avg = tur.calculate_above_average(float(media_turma), medias_alunos)
        maior, menor = tur.maior_menor_media(alunos, key)

        fmt += f"""
    {nome}, {key}

        # N° de estudantes: {qtd_alunos}
        # % de aprovados: {perc_aprovacao}
        # Média da turma: {media_turma}
        # {above_avg}
        # {maior}
        # {menor}
        
        ------------------------------------------------
        """

    return fmt


def write_global_dados(disciplinas, alunos):
    maior, menor = glb.get_taxa_aprovacao(disciplinas)
    format = f"""
        ================================== ESTATÍSTICAS GLOBAIS ==================================

        
        {glb.get_media_global(disciplinas)}
        {glb.get_perc_aprovacao(disciplinas)}
        {glb.get_alunos_matriculados(alunos)}
        {glb.get_aprovados_todas_materias(alunos)}
        {maior}
        {menor}
    """

    return format

def write_individual_dados(disciplinas, alunos):
    print('\n\t\t\t\n')
    fmt = f"""
    
        ================================== ESTATÍSTICAS INDIVIDUAIS ==================================
    """

    for matricula, aluno in alunos.items():
        taxa_aprovacao = ind.get_taxa_aprovacao_aluno(matricula, aluno)
        melhor_media, pior_media = ind.get_maior_media_aluno(aluno, disciplinas)

        fmt += f"""

    Estudante n° {matricula}

    {taxa_aprovacao}
    {melhor_media}
    {pior_media}

    ------------------------------------------------
        """

    return fmt

