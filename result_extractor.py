import csv
import re

# Mapeamento das classes
class_mapping = {
    "Aviso": 0,
    "Catamara": 1,
    "Conteineiro": 2,
    "Fragata": 3,
    "Passageiro": 4
}

# Modificando a função para salvar apenas a coluna class_code no CSV

def extract_results(txt_file_path, output_csv_path):
    # Padrão para detectar a classe e o caminho da imagem
    class_pattern = re.compile(r"(Aviso|Catamara|Conteineiro|Fragata|Passageiro):")
    image_pattern = re.compile(r"data/test/\d+\.png")
    
    # Lista para armazenar os resultados
    results = []
    current_image = None  # Armazena a última imagem encontrada
    
    with open(txt_file_path, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            # Verifica se a linha contém o caminho da imagem
            image_match = image_pattern.search(line)
            if image_match:
                # Se já houver uma imagem carregada, isso significa que ela não teve uma classe associada
                if current_image is not None:
                    # Salvamos como sem classe detectada (-1)
                    results.append([-1])
                current_image = image_match.group()  # Captura o nome da imagem
            
            # Verifica se a linha contém uma classe
            class_match = class_pattern.search(line)
            if class_match and current_image:
                detected_class = class_match.group(1)
                class_code = class_mapping[detected_class]
                results.append([class_code])
                current_image = None  # Reset para próxima imagem
    
    # Salvando os resultados em um arquivo CSV
    with open(output_csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['class_code'])  # Cabeçalho
        writer.writerows(results)


if __name__ == '__main__':
    # Caminhos para o arquivo de texto e o CSV de saída
    txt_file_path = 'resultados/resultados_5fold.txt'
    output_csv_path = 'resultados/predict_5fold.csv'

    # Chamando a função para gerar o CSV
    extract_results(txt_file_path, output_csv_path)