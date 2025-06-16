import pandas as pd
import joblib
import matplotlib.pyplot as plt

pipeline_path = '/dbfs/FileStore/pipeline_modelo_ia.pkl'

colunas_esperadas = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                     'restecg', 'thalach', 'exang', 'oldpeak', 'slope',
                     'ca', 'thal']

pipeline = joblib.load(pipeline_path)
model_in_pipeline = pipeline.named_steps['classifier']

if hasattr(model_in_pipeline, 'feature_importances_'):
    importancias = model_in_pipeline.feature_importances_
    importancias = importancias * 100
    
    df_importancias = pd.DataFrame({
        'Feature': colunas_esperadas,
        'Importância': importancias
    }).sort_values(by='Importância', ascending=False)
    
    print("Ranking das colunas por importância para a IA:\n")
    print(df_importancias.to_string(index=False))
    
    plt.figure(figsize=(10, 6))
    plt.bar(df_importancias['Feature'], df_importancias['Importância'], color='royalblue')
    plt.xlabel("Feature")
    plt.ylabel("Importância (%)")
    plt.title("Importância das Variáveis na Decisão do Modelo")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("O modelo carregado não suporta análise de importância de features.")