"""
    Este arquivo é onde começa a execução do projeto
"""
import os

from main.dicionarios.create_disciplina_dict import create_dict_disciplina
import utils.print_dados_relatorio as prt


def run(path):
    files = os.listdir(path)
    files.sort()


    dados_disciplina = create_dict_disciplina(files, path)

    prt.print_disciplina_dados(dados_disciplina[0], dados_disciplina[1])
    prt.print_global_dados(dados_disciplina[0], dados_disciplina[1])
    prt.print_individual_dados(dados_disciplina[0], dados_disciplina[1])


if __name__ == "__main__":
    # if len(sys.argv) == 2:
    #     run(sys.argv[1])
    # else:
    #     print("Nenhum caminho foi informado!")
    run('/home/nathalia/dev/projects/IPC-TP1-NathaliaNobregaSilva/data')
