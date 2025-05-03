# Análise estatística de base de dados de diabetes

![imagem](relatorios/imagens/diabetes.jpg)

## Organização do projeto

```
├── .gitignore            <- Arquivos e diretórios a serem ignorados pelo Git
├── ambiente.yml          <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE               <- Licença de código aberto (MIT)
├── README.md             <- README principal para desenvolvedores que usam este projeto.
|
├── dados                 <- Arquivos de dados para o projeto.
|
├── notebooks             <- Jupyter Notebooks.
│
│   └── src               <- Código-fonte para uso neste projeto.
│       │
│       ├── __init__.py   <- Torna um módulo Python
│       ├── config.py     <- Configurações básicas do projeto
│       └── estatistica.py<- Funções criadas especificamente para este projeto
|
├── referencias           <- Dicionários de dados.
|
├── imagens               <- Imagens utilizadas no projeto.
```

### Descrição das pastas e arquivos principais:

- **.gitignore**: Arquivos e diretórios a serem ignorados pelo Git.
- **ambiente.yml**: Arquivo de requisitos para garantir que todos os pacotes e dependências sejam configurados corretamente ao reproduzir o ambiente de análise.
- **LICENSE**: Arquivo de licença (MIT) para o projeto.
- **README.md**: Documento principal com informações sobre o projeto.
- **dados**: Contém todos os arquivos de dados utilizados para análise.
- **notebooks**: Contém os Jupyter Notebooks com as análises realizadas.
- **src**: Diretório com o código-fonte utilizado no projeto.
- **referencias**: Contém dicionários de dados e referências auxiliares.
- **imagens**: Armazena imagens usadas no projeto, como a imagem de diabetes mencionada.

###  Análise de Dados de Pacientes Diabéticos
Descrição
Dataset com 442 pacientes diabéticos, 10 variáveis preditoras (idade, sexo, IMC, etc.) e 1 variável target (progressão da doença após 1 ano). Dados normalizados (centrados pela média e escalados pelo desvio padrão).

### Análise Exploratória
- Estrutura: 442 entradas, sem valores nulos.

- Colunas renomeadas para o português (ex: age → idade, sex → sexo).

### Correlação
- Maior correlação com a variável target: IMC (0,59) e triglicerídeos (0,57).

- Menor correlação: HDL (-0,39).

### Otimização
- Conversão de tipos de dados, reduzindo o tamanho de memória de 38,1 KB para 13,5 KB (~64,57%).


