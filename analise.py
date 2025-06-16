import pandas as pd
import matplotlib.pyplot as plt

df_labeled = df_total.copy()
df_labeled['sex'] = df_total['sex'].map({1: 'Homem', 0: 'Mulher'})
df_labeled['target'] = df_total['target'].map({1: 'Doente', 0: 'Não Doente'})
cp_labels = {0: 'Angina Típica', 1: 'Angina Atípica', 2: 'Dor Não Anginosa', 3: 'Assintomático'}
df_labeled['cp'] = df_total['cp'].map(cp_labels)

cross_tab_gender = pd.crosstab(df_labeled['sex'], df_labeled['target'])

cross_tab_gender.plot(kind='bar', figsize=(10, 7), color=['#3498db', '#e74c3c'])
plt.title('Contagem de Pacientes por Sexo e Condição Cardíaca', fontsize=16)
plt.xlabel('Sexo', fontsize=12)
plt.ylabel('Número de Pacientes', fontsize=12)
plt.xticks(rotation=0)
plt.legend(title='Condição')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafico_sexo_condicao.png')
plt.show()


cross_tab_cp = pd.crosstab(df_labeled['cp'], df_labeled['target'])

cross_tab_cp.plot(kind='bar', figsize=(12, 7), color=['#3498db', '#e74c3c'])
plt.title('Relação entre Tipo de Dor no Peito e Condição Cardíaca', fontsize=16)
plt.xlabel('Tipo de Dor no Peito (cp)', fontsize=12)
plt.ylabel('Número de Pacientes', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Condição')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafico_dor_peito.png')
plt.show()


plt.figure(figsize=(12, 7))


plt.hist(df_total[df_total['target'] == 0]['age'], bins=20, alpha=0.7, label='Não Doente', color='#3498db')
a
plt.hist(df_total[df_total['target'] == 1]['age'], bins=20, alpha=0.7, label='Doente', color='#e74c3c')

plt.title('Distribuição de Idade por Condição Cardíaca', fontsize=16)
plt.xlabel('Idade', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafico_distribuicao_idade.png')
plt.show()



plt.figure(figsize=(12, 8))


scatter = plt.scatter(df_total['age'], df_total['thalach'], c=df_total['target'], cmap='coolwarm', alpha=0.8)

plt.title('Frequência Cardíaca Máxima vs. Idade por Condição', fontsize=16)
plt.xlabel('Idade', fontsize=12)
plt.ylabel('Frequência Cardíaca Máxima (thalach)', fontsize=12)


handles, _ = scatter.legend_elements()
plt.legend(handles, ['Não Doente', 'Doente'], title="Condição")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('grafico_idade_thalach.png')
plt.show()