import zipfile
import pdfplumber
import pandas as pd
import os

# Caminho para o pasta zip contendo os anexos
anexos_zip = "anexos.zip"

# Pasta onde os arquivos extraídos serão armazenados
extract_folder = "anexos_extraidos"

# Nome do arquivo CSV gerado
csv_filename = "Rol_de_Procedimentos.csv"

# Nome da pasta ZIP final
final_zip_filename = "Teste_Alexandre.zip"

# Dicionário de substituições para as abreviações
substituicoes = {
    "OD": "Ocupação Odontológica",
    "AMB": "Ambulatorial"
}

# Criação da pasta de extração
if not os.path.exists(extract_folder):
    os.makedirs(extract_folder)

# Extração do arquivo ZIP
with zipfile.ZipFile(anexos_zip, "r") as zip_ref:
    zip_ref.extractall(extract_folder)

# Caminho para o PDF extraído
pdf_path = os.path.join(extract_folder, "Anexo_1.pdf")

# Lista para armazenar os dados extraídos
data = []

# Leitura do PDF e extração das tabelas
with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages):
        print(f"Processando página {page_num + 1}...")
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                data.append(row)

if data:
    # Criando um DataFrame a partir dos dados extraídos
    df = pd.DataFrame(data)

    # Ajustando o cabeçalho
    df.columns = df.iloc[0]
    df = df[1:]

    # Substituindo as abreviações de acordo com o dicionário
    df.replace(substituicoes, inplace=True)

    # Salvando o DataFrame em um arquivo CSV
    df.to_csv(csv_filename, index=False, sep=';', encoding="utf-8-sig")
    print(f"Arquivo CSV '{csv_filename}' gerado com sucesso!")

    # Compactando o arquivo CSV em um arquivo ZIP
    with zipfile.ZipFile(final_zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename)
    print(f"Arquivo ZIP '{final_zip_filename}' gerado com sucesso!")

    os.remove(csv_filename)
    print(f"Arquivo CSV '{csv_filename}' removido após compactação")
else:
    print("Nenhum dado foi extraído do PDF. Verifique o arquivo PDF")

print(f"Processo concluído! Arquivo ZIP final salvo como {final_zip_filename}")
