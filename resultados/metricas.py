# k-fold para 5k itereções
resultado_kfold_5k = {
    'ap_0': [0.9910, 0.9935, 0.9937, 0.9956, 0.9928],
    'ap_1': [0.9989, 0.9993, 0.9996, 0.9982, 0.9999],
    'ap_2': [0.9962, 0.9991, 0.9891, 0.9979, 0.9981],
    'ap_3': [1.0000, 0.9997, 0.9993, 0.9965, 1.0000],
    'ap_4': [0.9987, 0.9973, 0.9991, 0.9981, 0.9975],
    'map': [0.996951, 0.997787, 0.996174, 0.997264, 0.997653],
    'precision': [0.99, 0.99, 0.99, 0.99, 0.99],
    'recall': [1.00, 1.00, 0.99, 1.00, 1.00],
    'f1': [0.99, 0.99, 0.99, 0.99, 1.00],
    'IoU': [0.8752, 0.8726, 0.8692, 0.8761, 0.8745]
}

# k-fold para 10k itereções
resultado_kfold_10k = {
    'ap_0': [0.9977, 0.9978, 0.9977, 0.9987, 0.9978],
    'ap_1': [0.9986, 0.9996, 0.9993, 0.9983, 1.0000],
    'ap_2': [1.0000, 1.0000, 0.9993, 0.9997, 0.9997],
    'ap_3': [0.9996, 1.0000, 1.0000, 0.9993, 0.9992],
    'ap_4': [0.9990, 0.9982, 0.9993, 0.9984, 0.9984],
    'map': [0.999005, 0.999130, 0.999137, 0.998877, 0.999014],
    'precision': [1.00, 1.00, 1.00, 1.00, 1.00],
    'recall': [1.00, 1.00, 1.00, 1.00, 1.00],
    'f1': [1.00, 1.00, 1.00, 1.00, 1.00],
    'IoU': [0.8917, 0.8938, 0.8917, 0.8930, 0.8917]
}

# k-fold para 20k itereções
resultado_kfold_20k = {
    'ap_0': [0.9989, 0.9989, 1.0000, 0.9999, 0.9996],
    'ap_1': [0.9997, 1.0000, 1.0000, 1.0000, 1.0000],
    'ap_2': [1.0000, 1.0000, 0.9993, 1.0000, 1.0000],
    'ap_3': [1.0000, 1.0000, 1.0000, 1.0000, 0.9997],
    'ap_4': [0.9991, 0.9983, 0.9993, 0.9986, 0.9985],
    'map': [0.999545, 0.999446, 0.999696, 0.999698, 0.999562],
    'precision': [1.00, 1.00, 1.00, 1.00, 1.00],
    'recall': [1.00, 1.00, 1.00, 1.00, 1.00],
    'f1': [1.00, 1.00, 1.00, 1.00, 1.00],
    'IoU': [0.9048, 0.9056, 0.8778, 0.9062, 0.9052]
}

# n-folds
resultado_nfolds = {
    'ap_0': [0.9966, 0.9954, 0.9965, 0.9981, 0.9971],
    'ap_1': [0.9998, 0.9995, 0.9992, 0.9998, 1.0000],
    'ap_2': [0.9956, 0.9978, 0.9990, 0.9971, 0.9972],
    'ap_3': [0.9996, 0.9997, 0.9994, 0.9999, 0.9998],
    'ap_4': [1.0000, 1.0000, 1.0000, 1.0000, 1.0000],
    'map': [0.998312, 0.998486, 0.998821, 0.998957, 0.998826],
    'precision': [0.99, 0.99, 0.99, 0.98, 0.99],
    'recall': [0.99, 0.99, 1.00, 0.99, 1.00],
    'f1': [0.99, 0.99, 1.00, 0.99, 0.99],
    'IoU': [0.8662, 0.8664, 0.8691, 0.8292, 0.8689]
}

# final
resultado_final = {
    'ap_0': 1.0000,
    'ap_1': 1.0000,
    'ap_2': 0.9996,
    'ap_3': 0.9998,
    'ap_4': 1.0000,
    'map': 0.999867,
    'precision': 1.00,
    'recall': 1.00,
    'f1': 1.00,
    'IoU': 0.8972
}

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def calcular_media_desvio(dicionario):
    resultados = {}
    chaves_interesse = ['ap_0', 'ap_1', 'ap_2', 'ap_3', 'ap_4', 'map', 'IoU']
    
    for chave in chaves_interesse:
        valores = dicionario[chave]
        media = np.mean(valores)
        desvio_padrao = np.std(valores)
        resultados[chave] = {'media': media, 'desvio_padrao': desvio_padrao}
    
    return resultados

def gerar_tabela_latex_combinada(resultados_5k, resultados_10k, resultados_20k):
    tabela_latex = "\\begin{table}[H]\n\\centering\n\\caption{Resultados Combinados}\n\\begin{tabular}{|c|c|c|c|c|c|c|}\n\\hline\n"
    tabela_latex += "Métrica & Média 5k & Desvio 5k & Média 10k & Desvio 10k & Média 20k & Desvio 20k \\\\\n\\hline\n"
    
    chaves_interesse = ['ap_0', 'ap_1', 'ap_2', 'ap_3', 'ap_4', 'map', 'IoU']
    
    for chave in chaves_interesse:
        media_5k = resultados_5k[chave]['media']
        desvio_5k = resultados_5k[chave]['desvio_padrao']
        media_10k = resultados_10k[chave]['media']
        desvio_10k = resultados_10k[chave]['desvio_padrao']
        media_20k = resultados_20k[chave]['media']
        desvio_20k = resultados_20k[chave]['desvio_padrao']
        tabela_latex += f"{chave} & {media_5k:.6f} & {desvio_5k:.6f} & {media_10k:.6f} & {desvio_10k:.6f} & {media_20k:.6f} & {desvio_20k:.6f} \\\\\n\\hline\n"
    
    tabela_latex += "\\end{tabular}\n\\end{table}"
    return tabela_latex

def salvar_tabela_excel_combinada(resultados_5k, resultados_10k, resultados_20k, nome_arquivo):
    chaves_interesse = ['ap_0', 'ap_1', 'ap_2', 'ap_3', 'ap_4', 'map', 'IoU']
    
    dados = {
        'Métrica': [],
        'Média 5k': [],
        'Desvio 5k': [],
        'Média 10k': [],
        'Desvio 10k': [],
        'Média 20k': [],
        'Desvio 20k': []
    }
    
    for chave in chaves_interesse:
        dados['Métrica'].append(chave)
        dados['Média 5k'].append(resultados_5k[chave]['media'])
        dados['Desvio 5k'].append(resultados_5k[chave]['desvio_padrao'])
        dados['Média 10k'].append(resultados_10k[chave]['media'])
        dados['Desvio 10k'].append(resultados_10k[chave]['desvio_padrao'])
        dados['Média 20k'].append(resultados_20k[chave]['media'])
        dados['Desvio 20k'].append(resultados_20k[chave]['desvio_padrao'])
    
    df = pd.DataFrame(dados)
    df.to_excel(nome_arquivo, index=False)

def plot_media_epocas(resultados_5k, resultados_10k, resultados_20k):
    chaves_interesse = ['ap_0', 'ap_1', 'ap_2', 'ap_3', 'ap_4', 'map']
    num_epocas = [5, 10, 20]
    
    medias_5k = [resultados_5k[chave]['media'] for chave in chaves_interesse]
    medias_10k = [resultados_10k[chave]['media'] for chave in chaves_interesse]
    medias_20k = [resultados_20k[chave]['media'] for chave in chaves_interesse]
    
    fig, ax1 = plt.subplots(figsize=(12, 8))
    
    for i, chave in enumerate(chaves_interesse):
        ax1.plot(num_epocas, [medias_5k[i], medias_10k[i], medias_20k[i]], marker='o', label=chave)
    
    ax1.set_xlabel('Quantidade de Épocas (milhares)')
    ax1.set_ylabel('ap e mAP')
    ax1.set_title('Média das Métricas em Função da Quantidade de Épocas')
    ax1.grid(True)
    
    # Adicionar um segundo eixo y para o IoU
    ax2 = ax1.twinx()
    medias_iou = [resultados_5k['IoU']['media'], resultados_10k['IoU']['media'], resultados_20k['IoU']['media']]
    ax2.plot(num_epocas, medias_iou, marker='o', color='r', label='IoU')
    ax2.set_ylabel('IoU', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    
    # Combinar as legendas dos dois eixos
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='lower right')
    
    plt.show()

def plot_variacao_folds(resultado_nfolds):
    chaves_interesse = ['ap_0', 'ap_1', 'ap_2', 'ap_3', 'ap_4', 'map']
    num_folds = list(range(1, len(resultado_nfolds['ap_0']) + 1))
    
    fig, ax1 = plt.subplots(figsize=(12, 8))
    
    # Plotar as métricas principais no eixo y1
    for chave in chaves_interesse:
        ax1.plot(num_folds, resultado_nfolds[chave], marker='o', label=chave)
    
    ax1.set_xlabel('Número de Folds')
    ax1.set_ylabel('ap e mAP')
    ax1.set_title('Variação das Métricas em Função do Número de Folds')
    ax1.grid(True)
    
    # Adicionar um segundo eixo y para o IoU
    ax2 = ax1.twinx()
    ax2.plot(num_folds, resultado_nfolds['IoU'], marker='o', color='r', label='IoU')
    ax2.set_ylabel('IoU', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    
    # Combinar as legendas dos dois eixos
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='lower right')
    
    plt.show()

def gerar_tabela_latex_nfolds(resultados_nfolds):
    tabela_latex = "\\begin{table}[H]\n\\centering\n\\caption{Resultados n-folds}\n\\begin{tabular}{|c|c|c|c|c|c|}\n\\hline\n"
    tabela_latex += "Métrica & Fold 1 & Fold 2 & Fold 3 & Fold 4 & Fold 5 \\\\\n\\hline\n"
    
    for chave, valores in resultados_nfolds.items():
        tabela_latex += f"{chave} & {valores[0]:.6f} & {valores[1]:.6f} & {valores[2]:.6f} & {valores[3]:.6f} & {valores[4]:.6f} \\\\\n\\hline\n"
    
    tabela_latex += "\\end{tabular}\n\\end{table}"
    return tabela_latex

if __name__ == '__main__':
    # Calcular a média e desvio padrão dos resultados
    # resultados_5k = calcular_media_desvio(resultado_kfold_5k)
    # resultados_10k = calcular_media_desvio(resultado_kfold_10k)
    # resultados_20k = calcular_media_desvio(resultado_kfold_20k)
    # print(gerar_tabela_latex_combinada(resultados_5k, resultados_10k, resultados_20k))
    # salvar_tabela_excel_combinada(resultados_5k, resultados_10k, resultados_20k, 'resultados/kfold.xlsx')
    # plot_media_epocas(resultados_5k, resultados_10k, resultados_20k)

    # Plotar a variação das métricas em função do número de folds
    # plot_variacao_folds(resultado_nfolds)
    print(gerar_tabela_latex_nfolds(resultado_nfolds))

