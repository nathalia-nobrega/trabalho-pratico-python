"""
    Este arquivo contém a função que disponibiliza a leitura dos arquivos
"""

def read_data(filename, path):
    file = open(f'{path}/{filename}')
    data = file.read()
    file.close()
    return data
