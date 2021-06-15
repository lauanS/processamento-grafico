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

* Carrega um objeto
* Cria uma cena
* Aplica um zoom de 6x (escala com todos os atributos iguais)
* Posiciona o objeto perto da "parede" e do "chão"
* Rotaciona o objeto para ele ficar "olhando para parede"
* Cria uma câmera para o objeto
* Renderiza ele utilizando o matplotlib para preencher os triângulos da imagem

Resultado esperado: Ursinho no canto inferior esquerdo da imagem, "olhando" para esquerda (parede)

### ObjView.py

É uma classe auxiliar, usada durante o desenvolvimento das funções de leitura de objeto, definição do mundo e câmera, enquanto não tinhamos nosso próprio método de rasterização. Ela usa o OpenGL com o Pygame para exibir um objeto 3D. 

* Carrega um objeto e renderiza ele com o OpenGL

### ObjLoader.py

Classe para carregar um arquivo .obj.

Lê suas vertices e faces.

* Carrega um objeto, exibe suas vertices e faces e renderiza ele com o OpenGL

Resultado esperado: Ursinho centralizado na imagem

### Scene.py

Classe que define nosso mundo. Contém uma lista de objeto e métodos para aplicar transformações neles.

* Carrega um objeto3D pequena (apenas um triâgulo)
* Cria uma cena
* Aplica zoom de 0.5
* Movimenta, rotaciona, inclina e altera sua escala
* Exibe as matrizes de vertices resultantes da aplicação de cada operação no objeto original

### Camera.py

Classe responsável por definir a câmera e a perspectiva da projeção

* Carrega um objeto3D
* Cria uma cena
* Aplica um zoom (escala) e incline o objeto
* Define a posição da câmera, ponto a ser visualizado e o vetor de orientação
* Define as informações sobre a perspectiva (frustum)
* Aplica a transformação na câmera
* Altera a perspectiva
* Renderiza o objeto usando o OpenGL 

Resultado esperado: Um ursinho um pouco inclinado

### Render.py

Classe responsável pela rasterização dos objetos 3D. Executa todo o pipeline gráfico.

* Carrega um objeto
* Cria uma cena
* Aplica um zoom de 6x (Para obter uma boa visualização das arestas que formam cada triângulo (faces do objeto))
* Posiciona o objeto muito perto da "parede" e do "chão"
* Rotaciona o objeto para ele ficar "Com uma patinha na parede"
* Cria uma câmera para o objeto
* Renderiza todas as vértices de cada face do objeto