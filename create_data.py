import os

def create_data_files():
    # Template para o conteúdo do arquivo .data
    # data_content_template = """
    #     classes = 5
    #     train = data/train_kfold_{fold_number}.txt
    #     valid = data/valid_kfold_{fold_number}.txt
    #     names = data/train.names
    #     backup = /mydrive/navios/backup_kfold_{fold_number}
    # """

    data_content_template = """
        classes = 5
        train = data/train_{fold_number}fold.txt
        valid = data/test.txt
        names = data/train.names
        backup = /mydrive/navios/backup_{fold_number}fold
    """

    # Criação de arquivos .data para os folds de 2 a 5
    # for fold_number in range(2, 6):
    for fold_number in range(1, 5):
        # file_name = f"train_kfold_{fold_number}.data"
        file_name = f"train_{fold_number}fold.data"
        file_path = os.path.join("", file_name)
        
        # Preenchendo o template com informações específicas do fold
        data_content = data_content_template.format(fold_number=fold_number)
        
        # Escrevendo o conteúdo no arquivo
        with open(file_path, 'w') as file:
            file.write(data_content.strip())

        print(f"Created {file_name}")

if __name__ == "__main__":
    create_data_files()
