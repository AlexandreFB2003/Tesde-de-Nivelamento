import os
import shutil
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import zipfile

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Pasta onde os PDFs serão salvos
download_dir = "downloads"
os.makedirs(download_dir, exist_ok=True)

# Função para realizar o download dos PDFs
def download_pdf(pdf_url, filename):
    response = requests.get(pdf_url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Função para compactar os PDFs em um arquivo ZIP
def create_zip_file(file_names, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in file_names:
            zipf.write(file, os.path.basename(file))

# Acessar o site
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar os links dos PDFs
pdf_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    if "Anexo I" in link.text or "Anexo II" in link.text:
        pdf_url = urljoin(url, href)
        pdf_links.append(pdf_url)

# Baixar os PDFs
downloaded_files = []
for i, pdf_url in enumerate(pdf_links):
    filename = os.path.join(download_dir, f"anexo_{i + 1}.pdf")
    download_pdf(pdf_url, filename)
    downloaded_files.append(filename)

# Compactar os arquivos baixados em um arquivo ZIP
zip_filename = "Anexos.zip"
create_zip_file(downloaded_files, zip_filename)

for file in downloaded_files:
    os.remove(file)

shutil.rmtree(download_dir)

print(f"Os arquivos foram baixados e compactados em: {zip_filename}")
