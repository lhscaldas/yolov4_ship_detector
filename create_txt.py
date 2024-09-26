import os

def create_txt(output_filename, fold_numbers):
    # Verificar se todos os números de folds são válidos
    if not all(1 <= num <= 5 for num in fold_numbers):
        raise ValueError("All fold numbers must be between 1 and 5.")
    
    # Definindo o caminho base
    base_path = "data"
    
    # Nome do arquivo de saída
    output_file_path = os.path.join(base_path, output_filename)

    # Abrir arquivo de saída para escrita
    with open(output_file_path, 'w') as output_file:
        # Iterar sobre cada número de fold fornecido
        for num in fold_numbers:
            # Montar o nome do diretório do fold
            fold_path = os.path.join(base_path, f"fold_{num}")
            
            # Verificar se o diretório existe
            if os.path.exists(fold_path):
                # Listar todos os arquivos no diretório do fold
                for filename in os.listdir(fold_path):
                    if filename.endswith(".png"):  # Assumindo que são imagens jpg
                        output_file.write(f'data/fold_{num}/'+ filename + '\n')
            else:
                print(f"Directory {fold_path} does not exist.")

if __name__ == "__main__":
    total_folds = 6
    all_folds = list(range(1, total_folds + 1))

    # for i in range(1, total_folds + 1):
    #     valid_fold = [i]  # fold usado para validação
    #     train_folds = [j for j in all_folds if j != i]  # outros folds usados para treinamento

    #     # Criar arquivos de validação e treinamento para cada fold
    #     create_txt(f"valid_kfold_{i}.txt", valid_fold)
    #     create_txt(f"train_kfold_{i}.txt", train_folds)

    for i in range(1, total_folds):
        train_folds = list(range(1, i + 1))  # folds from 1 to i
        create_txt(f"train_{i}fold.txt", train_folds)
