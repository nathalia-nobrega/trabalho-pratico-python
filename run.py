"""
    Este arquivo é onde começa a execução do projeto
"""
import sys, os
from main.dicionarios.create_disciplina_dict import create_dict_disciplina
from main.dicionarios.create_alunos_dict import create_dict_alunos
from utils.print_dados_relatorio import print_disciplina_dados


def run(path):
    files = os.listdir(path)
    files.sort()
    # a)
    dados_disciplina = create_dict_disciplina(files)
    print_disciplina_dados(dados_disciplina[0], dados_disciplina[1])



if __name__ == "__main__":
    # if len(sys.argv) == 2:
    #     run(sys.argv[1])
    # else:
    #     print("Nenhum caminho foi informado!")
    run('/home/nathalia/dev/projects/IPC-TP1-NathaliaNobregaSilva/data')


# main('/home/nathalia/dev/projects/IPC-TP1-NathaliaNobrega/data')