"""
    Este arquivo contém a função que disponibiliza a leitura dos arquivos
"""

def read_data(filename):
    file = open(f'data/{filename}')
    data = file.read()
    file.close()
    return data
