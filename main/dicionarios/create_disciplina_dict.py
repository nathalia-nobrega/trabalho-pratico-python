from main.dicionarios.create_alunos_dict import create_dict_alunos
from main.estatisticas.estatisticas_turma import extract_discipline_data, calculate_approved
from utils.read_file_data import read_data


def create_dict_disciplina(files, path):
    disciplina = {}

    # Aqui ficam somente os dados que vão ser enviados ao resultado.txt
    dados_relatorio = {}

    for file in files:
        data = read_data(file, path)

        # Extraíndo os dados da disciplina
        dados_disciplina = extract_discipline_data(data)
        codigo_turma = dados_disciplina[0]

        # Extraíndo a quantidade de alunos
        qtd_alunos = 0
        for line in data.split('\n')[2:]:
            if line:
                qtd_alunos += 1

        dados_dict = {
            'NOME': dados_disciplina[1],
            'PESOS': dados_disciplina[2][:3],
            'MEDIA_MINIMA': float(dados_disciplina[2][3]),
            'QUANTIDADE_ALUNOS': qtd_alunos,
        }
        disciplina[f'{codigo_turma}'] = dados_dict
        dict_alunos = create_dict_alunos(data, codigo_turma, disciplina[f'{codigo_turma}'])
        dados = calculate_approved(codigo_turma, dict_alunos, disciplina[f'{codigo_turma}']['PESOS'], disciplina[f'{codigo_turma}']['MEDIA_MINIMA'], disciplina[f'{codigo_turma}']['QUANTIDADE_ALUNOS'])

        dados_dict['% DE APROVADOS'] = dados[0]
        dados_dict['MEDIA_TURMA'] = dados[1]
        dados_dict['QTD_APROVADOS'] = dados[2]


        dados_relatorio[f'{codigo_turma}'] = [disciplina[f'{codigo_turma}']['NOME'],disciplina[f'{codigo_turma}']['QUANTIDADE_ALUNOS'], disciplina[f'{codigo_turma}']['% DE APROVADOS'], disciplina[f'{codigo_turma}']['MEDIA_TURMA'], disciplina[f'{codigo_turma}']['QTD_APROVADOS']]

    return dados_relatorio, dict_alunos