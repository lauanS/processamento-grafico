# Processamento Gráfico

Repositório dos trabalhos da disciplina de Processamento Gráfico

## Guia para execução do projeto

Para executar esse projeto, será necessário ter o [Python(3.9.x)](https://www.python.org/downloads/) instalado e algum gerenciador de pacotes, como o [pip](https://pypi.org/project/pip/) (que já vem junto com o python) ou o [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html) (que vem junto ao instalar o anaconda/miniconda).

Recomendamos que crie uma ambiente virtual (_Virtual Environments_) para executar esse projeto nas mesmas condições.

**pg-env:** Nome sugerido para o ambiente virtual

```bash
python3 -m venv pg-env

# Ou, caso tenho o conda instalado

conda create --name pg-env

# Com o conda é possível especifícar a versão do python.

conda create --name pg-env python=3.9.5
```

Agora ative o ambiente criado:

```bash
source pg-env/bin/activate
# Ou
conda activate pg-env
```

Instale os pacotes necessários para execução do programa:

```bash
# Utilizando o pip
# Numpy
pip install numpy==1.20.2
pip install matplotlib==3.4.2

# Utilizando o conda
# Numpy
conda install numpy=1.20.2
conda install -c conda-forge matplotlib=3.4.2
```

Versões usadas durante desenvolvimento:
Programa/pacote | Versão
--------- | ------
Python | 3.9.5
pip | 21.1.1
Conda | 4.10.1
NumPy | 1.20.2
Matplotlib | 3.4.2

## Instalação para o desenvolvimento

Algumas funções que foram implementadas antes da criação da classe Render() usam o OpenGL para visualização, será necessário usar instalar algumas bibliotecas para visualizar algumas demonstrações:

```bash
# Pelo pip (recomendado)
pip install PyOpenGL PyOpenGL_accelerate
pip install pygame

# ou pelo conda (acho melhor pelo pip nesse caso)

conda install pyopengl
conda install pyopengl-accelerate
conda install pygame
```

Caso apareça algum erro relacionado ao PyOpenGL_accelerate, recomendo desinstalar o pacote :

```bash
pip uninstall PyOpenGL-accelerate
```

## Demonstrações

Cada classe possuí uma função Main() própria, ao pedir para executar o arquivo da classe em vez do arquivo main.py, será realizado uma pequena demonstração da classe, abaixo tem uma lista descrevendo cada arquivo e o que ele executa na sua função main().


### main.py 

Arquivo principal, executa todo o pipeline gráfico.

* Carrega dois objeto
* Cria uma cena
* Aplica um zoom de 6x (escala com todos os atributos iguais)
* Posiciona o ursinho perto do "teto" e a mão embaixo dele
* Rotaciona o ursinho para ele ficar "olhando para baixo"
* Cria uma câmera para o objeto
* Renderiza ele e tonaliza cada face dos objetos

Resultado esperado: Ursinho no canto superir da imagem, "olhando" para baixo onde estára uma mão

### Render.py

Classe responsável pela rasterização dos objetos 3D. Executa todo o pipeline gráfico.

* Carrega dois objeto
* Cria uma cena
* Aplica um zoom de 6x (escala com todos os atributos iguais)
* Posiciona o ursinho perto do "teto" e a o rockerArm embaixo dele
* Rotaciona o ursinho para ele ficar "olhando para baixo" e o rockerArm
* Cria uma câmera para o objeto
* Renderiza ele e tonaliza cada face dos objetos

Resultado esperado: Ursinho no canto superir da imagem, "olhando" para baixo onde estára o rockerArm
