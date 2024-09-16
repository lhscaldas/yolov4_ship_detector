import os
from collections import defaultdict, Counter

# Caminhos das pastas de destino
# pastas_destino = [f"fold_{i}" for i in range(1, 6)]
pastas_destino = ["train"]

# Inicializa um dicionário para contar as classes em cada pasta
contagem_classes = {pasta: defaultdict(int) for pasta in pastas_destino}

# Inicializa um dicionário para rastrear os arquivos txt e verificar duplicados
arquivos_rastreados = defaultdict(list)

# Contagem dos arquivos e classes em cada pasta
for pasta in pastas_destino:
    arquivos = os.listdir(pasta)
    arquivos_txt = [arq for arq in arquivos if arq.endswith('.txt')]

    for arq_txt in arquivos_txt:
        # Lê a classe (os dois primeiros caracteres)
        with open(os.path.join(pasta, arq_txt), 'r') as file:
            classe = file.read(2)
            contagem_classes[pasta][classe] += 1

        # Adiciona o arquivo ao rastreamento para verificar duplicados
        nome_base = arq_txt[:-4]  # Remove a extensão .txt
        arquivos_rastreados[nome_base].append(pasta)

# Exibir a contagem de classes em cada pasta
print("Contagem de arquivos por classe em cada pasta:")
for pasta, contagem in contagem_classes.items():
    print(f"\nPasta {pasta}:")
    for classe, quantidade in contagem.items():
        print(f"  Classe {classe}: {quantidade} arquivos")

# Verificar e exibir arquivos duplicados
arquivos_duplicados = {arquivo: pastas for arquivo, pastas in arquivos_rastreados.items() if len(pastas) > 1}

if arquivos_duplicados:
    print("\nArquivos duplicados encontrados em mais de uma pasta:")
    for arquivo, pastas in arquivos_duplicados.items():
        print(f"  Arquivo {arquivo}.txt duplicado nas pastas: {', '.join(pastas)}")
else:
    print("\nNenhum arquivo duplicado encontrado.")
