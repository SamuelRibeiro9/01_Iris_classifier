from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / 'dados'

# Caminho para os arquivos de dados do projeto
DADOS_ORIGINAIS = PASTA_DADOS / 'iris.csv'
DADOS_TRATADOS = PASTA_DADOS / 'iris_limpo.parquet'

# Caminho para os arquivos de modelos do projeto
PASTA_MODELOS = PASTA_PROJETO / 'modelos'

# Caminhos auxiliares
PASTA_RELATORIOS = PASTA_PROJETO / 'relatorios'
PASTA_IMAGENS = PASTA_RELATORIOS / 'imagens'
