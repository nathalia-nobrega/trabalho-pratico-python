"""
    Este arquivo é onde começa a execução do projeto
"""
import sys, os
from main.dicionarios.create_disciplina_dict import create_dict_disciplina
from main.dicionarios.create_alunos_dict import create_dict_alunos
from main.estatisticas.estatisticas_global import get_media_global, get_perc_aprovacao, get_alunos_matriculados, \
    get_aprovados_todas_materias, get_taxa_aprovacao
from utils.print_dados_relatorio import print_disciplina_dados, print_global_dados


def run(path):
    files = os.listdir(path)
    files.sort()

    dados_disciplina = create_dict_disciplina(files)

    # Saída
    print_disciplina_dados(dados_disciplina[0], dados_disciplina[1])
    print_global_dados(dados_disciplina[0], dados_disciplina[1])

    # get_media_global(dados_disciplina[0])
    # get_perc_aprovacao(dados_disciplina[0])
    # get_alunos_matriculados(dados_disciplina[1])
    # get_aprovados_todas_materias(dados_disciplina[1])
    # get_taxa_aprovacao(dados_disciplina[0])

if __name__ == "__main__":
    # if len(sys.argv) == 2:
    #     run(sys.argv[1])
    # else:
    #     print("Nenhum caminho foi informado!")
    run('/home/nathalia/dev/projects/IPC-TP1-NathaliaNobregaSilva/data')


# main('/home/nathalia/dev/projects/IPC-TP1-NathaliaNobrega/data')