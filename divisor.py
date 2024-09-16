import os
import shutil
from collections import defaultdict
from sklearn.model_selection import StratifiedKFold

# Caminho da pasta original
pasta_original = "train"

# Caminhos das pastas de destino
pastas_destino = [f"fold_{i}" for i in range(1, 6)]

# Criar as pastas de destino se não existirem
for pasta in pastas_destino:
    os.makedirs(pasta, exist_ok=True)

# Listar os arquivos na pasta original
arquivos = os.listdir(pasta_original)

# Filtrar apenas os arquivos txt
arquivos_txt = [arq for arq in arquivos if arq.endswith('.txt')]

# Obter as classes a partir dos arquivos txt
classes = []
for arq_txt in arquivos_txt:
    with open(os.path.join(pasta_original, arq_txt), 'r') as file:
        classes.append(file.read(2))

# Agrupar arquivos por classe
arquivos_por_classe = defaultdict(list)
for arq_txt, classe in zip(arquivos_txt, classes):
    nome_base = arq_txt[:-4]  # Remove a extensão .txt
    arquivos_por_classe[classe].append(nome_base)

# Preparar os dados para o StratifiedKFold
dados = []
labels = []
for classe, arquivos in arquivos_por_classe.items():
    for arquivo in arquivos:
        dados.append(arquivo)
        labels.append(classe)

# StratifiedKFold para manter a proporção das classes
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Inicializa um contador de progresso
total_arquivos = len(dados)
arquivos_processados = 0

# Distribuir os arquivos nas pastas de destino
for i, (treino_idx, teste_idx) in enumerate(skf.split(dados, labels)):
    print(f"Distribuindo arquivos para a pasta fold_{i+1}...")

    for idx in teste_idx:
        arquivo_base = dados[idx]
        
        # Copiar arquivo de imagem
        caminho_img_origem = os.path.join(pasta_original, arquivo_base + '.png')
        caminho_img_destino = os.path.join(pastas_destino[i], arquivo_base + '.png')
        shutil.copy2(caminho_img_origem, caminho_img_destino)
        
        # Copiar arquivo de texto
        caminho_txt_origem = os.path.join(pasta_original, arquivo_base + '.txt')
        caminho_txt_destino = os.path.join(pastas_destino[i], arquivo_base + '.txt')
        shutil.copy2(caminho_txt_origem, caminho_txt_destino)
        
        # Atualiza e printa o progresso
        arquivos_processados += 1
        if arquivos_processados % 1000 == 0 or arquivos_processados == total_arquivos:
            print(f"Progresso: {arquivos_processados}/{total_arquivos} arquivos processados.")

print("Distribuição concluída!")
