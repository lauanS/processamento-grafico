# Processamento Gráfico

Repositório dos trabalhos da disciplina de Processamento Gráfico

## Guia para execução do projeto

Para executar esse projeto, será necessário ter o [Python(3.9.x)](https://www.python.org/downloads/) instalado e algum gerenciador de pacotes, como o [pip](https://pypi.org/project/pip/) (que já vem junto com o python) ou o [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html) (que vem junto ao instalar o anaconda/miniconda).

Recomendamos que crie uma ambiente virtual (*Virtual Environments*) para executar esse projeto nas mesmas condições.

**pg-env:** Nome sugerido para o ambiente virtual

```shell
python3 -m venv pg-env 

# Ou, caso tenho o conda instalado

conda create --name pg-env

# Com o conda é possível especifícar a versão do python.

conda create --name pg-env python=3.9.5
```


Agora ative o ambiente criado:
```shell
source pg-env/bin/activate
# Ou
conda activate pg-env
```

Instale os pacotes necessários para execução do programa:

```shell
# Utilizando o pip
# Numpy
pip install numpy==1.20.2

# Utilizando o conda
# Numpy
conda install numpy=1.20.2
```

Versões usadas durante desenvolvimento:
  Programa/pacote | Versão
--------- | ------
Python | 3.9.5
pip | 21.1.1
Conda | 4.10.1
NumPy | 1.20.2
