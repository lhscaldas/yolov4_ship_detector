import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def verify_classes(csv_file):
    df = pd.read_csv(csv_file)
    unique_classes = df['class_code'].unique()
    print(f"Classes únicas em {csv_file}: {unique_classes}")

def plot_confusion_matrix(true_csv, predict_csv, title, output_csv):
    # Ler os arquivos CSV
    true_labels = pd.read_csv(true_csv)['class_code']
    predict_labels = pd.read_csv(predict_csv)['class_code']
    
    # Calcular a matriz de confusão
    cm = confusion_matrix(true_labels, predict_labels, labels=[0, 1, 2, 3, 4])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1, 2, 3, 4])
    
    # Plotar a matriz de confusão com o cmap azul
    fig, ax = plt.subplots(figsize=(6, 6))
    disp.plot(ax=ax, cmap='Blues')
    ax.set_title(title)
    
    plt.show()
    
    # Salvar a matriz de confusão em um arquivo CSV
    cm_df = pd.DataFrame(cm, index=[0, 1, 2, 3, 4], columns=[0, 1, 2, 3, 4])
    cm_df.to_csv(output_csv)

if __name__ == '__main__':
    # Verificar os arquivos CSV
    # verify_classes('resultados/test_true.csv')
    # verify_classes('resultados/predict_1fold.csv')
    # verify_classes('resultados/predict_5fold.csv')

    # Plotar as Matrizes
    plot_confusion_matrix('navios/resultados/test_true.csv', 'navios/resultados/predict_1fold.csv', 'cm_1_fold', 'Confusion Matrix - 1 Fold')
    plot_confusion_matrix('navios/resultados/test_true.csv', 'navios/resultados/predict_total.csv', 'cm_5_fold', 'Confusion Matrix - 5 Folds')