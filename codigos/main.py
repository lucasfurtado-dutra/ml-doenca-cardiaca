import pandas as pd
import numpy as np
import difflib
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

def mapear_colunas(colunas_dataset, colunas_esperadas, threshold=0.6):
    mapeamento = {}
    for col_esp in colunas_esperadas:
        similares = difflib.get_close_matches(col_esp, colunas_dataset, n=1, cutoff=threshold)
        if similares:
            mapeamento[col_esp] = similares[0]
        else:
            mapeamento[col_esp] = None
    return mapeamento

def carregar_e_formatar_dataset(caminho_csv, colunas_esperadas):
    df_spark = spark.read.format("csv") \
        .option("inferSchema", "true") \
        .option("header", "true") \
        .option("sep", ",") \
        .load(caminho_csv)
    
    df_raw = df_spark.toPandas()
    mapeamento = mapear_colunas(df_raw.columns.tolist(), colunas_esperadas)
    
    df = pd.DataFrame()
    for col in colunas_esperadas:
        col_real = mapeamento[col]
        if col_real:
            df[col] = df_raw[col_real]
        else:
            print(f" Coluna '{col}' ausente em {caminho_csv}. Preenchida com NaN.")
            df[col] = np.nan
    return df

arquivos_csv = [
    "/FileStore/tables/heart.csv",
    "/FileStore/tables/Heart_Disease_Dataset__1_.csv"
]

colunas_esperadas = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                     'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

dataframes = [carregar_e_formatar_dataset(arquivo, colunas_esperadas) for arquivo in arquivos_csv]
df_total = pd.concat(dataframes, ignore_index=True)

print("DataFrame com a junção dos arquivos CSV:")
print(df_total.head(10).to_string(index=False))

X = df_total.drop('target', axis=1)
y = df_total['target']

pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42))
])

pipeline.fit(X, y)

os.makedirs('/dbfs/FileStore/', exist_ok=True)
joblib.dump(pipeline, '/dbfs/FileStore/pipeline_modelo_ia.pkl')

print("\nModelo treinado com múltiplos arquivos e salvo com sucesso.")