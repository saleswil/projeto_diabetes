from pathlib import Path

PASTA_PROJETO = Path().resolve().parent

PASTA_DADOS = PASTA_PROJETO / "dados"

# Caminho do arquivo do projeto
DADOS_TRATADOS = PASTA_DADOS / "diabetes_tratado.parquet"

# coloque abaixo o caminho para os arquivos de modelos de seu projeto
PASTA_MODELOS = PASTA_PROJETO / "modelos"

# coloque abaixo outros caminhos que você julgar necessário
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"
