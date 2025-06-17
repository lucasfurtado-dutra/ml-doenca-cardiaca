# ML pra predição de doenças cardiovasculares

**Link DataBricks do projeto:** https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/1827107733663528/1795717227451338/6228417783277165/latest.html

**Link para o Roteiro de extensão via Overleaf:** https://pt.overleaf.com/read/zdfpdgwkpzmh#e4d31c

## 📝 Sobre o Projeto

Este projeto desenvolve um modelo de Machine Learning em Python para a predição de doenças cardíacas, visando a identificação precoce de pacientes em risco.
Utilizando as bibliotecas Pandas e Numpy para a manipulação de dados e Scikit-learn para o treinamento dos algoritmos, o modelo analisa padrões em dados clínicos. A visualização dos resultados é feita com Matplotlib. Para garantir o processamento eficiente e escalável de grandes volumes de dados, toda a solução é implementada na plataforma Databricks, potencializada pelo poder do Apache Spark, criando uma ferramenta robusta de apoio à decisão médica.

## 🚀 Tecnologias Utilizadas
* `Python (Libs: "pandas", "numpy", "scikit-learn", "matplotlib", "statsmodels")`
* `Databricks`
* `Apache spark`

## ⚙️ Pré-requisitos
* `Scala 12.2`
* `Spark 3.3.2`
* `Python versão >= 3.9`

## 💻 Instalação e Execução
1.  **Instalação das Bibliotecas:**
   
   `Para executar a ML, entre no seu Databricks (https://login.databricks.com)`
   
   `Crie um notebook, em seguida anexe um cluster para ele. (Recomendado que seja adicionado 4 celulas de códigos)`

   `Nas células de códigos adicionar respectivamente na ordem abaixo:`
* `main.py`
* `priority.py`
* `logit.py`
* `analise.py`

  `Libs:`
  
* `pip install pandas`
* `pip install numpy`
* `pip install matplotlib`
* `pip install scikit-learn`
* `pip install statsmodels`
   

## ✨ Funcionalidades
Destaque as principais características ou funcionalidades do seu projeto. Use bullet points para facilitar a leitura.

* `Geração de Predições de Risco: Habilidade de, dado um novo conjunto de dados de paciente, prever a probabilidade ou o risco de desenvolver doenças cardiovasculares.`
* `Treinamento e Otimização do Modelo de ML: Desenvolvimento e treinamento de algoritmos de Machine Learning (via scikit-learn) para identificar padrões em dados clínicos e otimizar sua performance.`
* `Engenharia de Características (Feature Engineering): Processo de criação ou seleção de variáveis relevantes a partir dos dados brutos para otimizar o desempenho do modelo de predição.`
