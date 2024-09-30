import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('navios/resultados/test_true.csv')

# Contar o número de ocorrências de cada classe
contagem_classes = df['class_code'].value_counts().sort_index()

# Exibir o resultado
print(contagem_classes)