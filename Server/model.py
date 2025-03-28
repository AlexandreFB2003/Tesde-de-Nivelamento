import csv
from config import Config

def load_company():
    operadoras = []
    with open(Config.CSV_FILE_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            operadora = {
                'Registro_ANS': row['Registro_ANS'],
                'CNPJ': row['CNPJ'],
                'Razao_Social': row['Razao_Social'],
                'Nome_Fantasia': row['Nome_Fantasia'],
                'Modalidade': row['Modalidade']
            }
            operadoras.append(operadora)
    return operadoras

def search_company(query):
    operadoras = load_company()
    query = query.lower()
    results = [
        op for op in operadoras
        if query in op['Razao_Social'].lower() or query in op['Nome_Fantasia'].lower()
    ]
    return results
