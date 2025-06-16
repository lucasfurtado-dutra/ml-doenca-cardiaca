import pandas as pd
import statsmodels.api as sm

features_importantes = [
    'cp', 'ca', 'oldpeak', 'chol', 'thal', 'age', 
    'trestbps', 'thalach', 'sex', 'slope', 'exang', 
    'restecg', 'fbs'
]
X = df_total[features_importantes]
y = df_total['target']

X = sm.add_constant(X)

modelo_logistico = sm.Logit(y, X)

resultado = modelo_logistico.fit()

print(resultado.summary())