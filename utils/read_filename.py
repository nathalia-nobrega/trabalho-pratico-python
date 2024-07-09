"""
    Este arquivo tem o código que extrai o nome dos arquivos (Turma 1, Turma 2)
"""

def extract_class_name(filename):
    split = filename.split('.csv')[0].split('_')
    return str.capitalize(split[0] + " " + split[1])