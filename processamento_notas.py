"""
    Este arquivo é onde começa a execução do projeto
"""
import sys, os

from main.dicionarios.create_disciplina_dict import create_dict_disciplina
import utils.print_dados_relatorio as prt


def run(path):
    files = os.listdir(path)
    files.sort()
    dados_disciplina = create_dict_disciplina(files, path)

    est_turma = prt.write_disciplina_dados(dados_disciplina[0], dados_disciplina[1])
    est_global = prt.write_global_dados(dados_disciplina[0], dados_disciplina[1])
    est_ind = prt.write_individual_dados(dados_disciplina[0], dados_disciplina[1])

    file_path = f'{path}/resultado.txt'
    with open(file_path, 'w') as file:
        # Write content to the file
        file.write(est_turma)
        file.write(est_global)
        file.write(est_ind)
    print(f"O arquivo resultado.txt foi criado na pasta {file_path}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        print("Nenhum caminho foi informado!")
    # run('/home/nathalia/dev/projects/IPC-TP1-NathaliaNobregaSilva/data')
