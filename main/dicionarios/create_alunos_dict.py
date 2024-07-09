from main.estatisticas.estatisticas_aluno import isApproved
from main.estatisticas.estatisticas_turma import calculate_notes
from utils.read_file_data import read_data

alunos_turmas = {}

def create_dict_alunos(alunos, disciplina_codigo, disciplina):

    for aluno in alunos.split('\n')[2:]:
        if aluno:
            dados_aluno = extract_student_data(aluno)

            matricula = dados_aluno[0]

            media_aluno = calculate_notes(dados_aluno[1], disciplina['PESOS'])
            aprovado = isApproved(media_aluno, disciplina['MEDIA_MINIMA'])
            codigo_turma = disciplina_codigo

            # Verificar se aluno já está matriculado em algum curso
            if matricula in alunos_turmas:
                turmas = alunos_turmas[matricula]['matriculado_em']

                alunos_turmas[matricula]['matriculado_em'].append(codigo_turma)
                alunos_turmas[matricula]['media'].append(media_aluno)
                alunos_turmas[matricula]['aprovado'].append(aprovado)
            else:
                dados_dict = {
                'matriculado_em': [codigo_turma],
                'media': [media_aluno],
                'aprovado': [aprovado]
            }

                alunos_turmas[f'{dados_aluno[0]}'] = dados_dict

    return alunos_turmas


def extract_student_data(line):
    matricula = line.split(',')[0]
    notas = []
    for nota in line.split(',')[1:4]:
        notas.append(float(nota))
    return matricula, notas

