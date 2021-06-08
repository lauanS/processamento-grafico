import numpy as np
from OpenGL.GL import *

from ObjLoader import ObjLoader


class Camera:
    def __init__(self, obj):
        self.position = np.array([])
        self.look_at = np.array([])
        self.view_up = np.array([])
        self.obj = obj

    # Define as informações principais da câmera
    def set_info(self, position, look_at, view_up):
        self.position = np.array(position)
        self.look_at = np.array(look_at)
        self.view_up = np.array(view_up)

    # Calcula os vetores U, V e N
    def calculate_uvn(self):
        self.n = (self.look_at - self.position) / \
            abs(self.look_at - self.position)
        self.u = (self.view_up * self.n) / abs(self.view_up * self.n)
        self.v = self.n * self.u

    # Calcula as matrizes de translação e rotação da câmera
    def transformation_matrix(self):
        self.calculate_uvn()
        translation_matrix = np.matrix([[1, 0, 0, -self.position[0]],
                                       [0, 1, 0, -self.position[1]],
                                       [0, 0, 1, -self.position[2]],
                                       [0, 0, 0, 1]])

        rotation_matrix = np.matrix([[self.u[0], self.u[1], self.u[2], 0.0],
                                    [self.v[0], self.v[1], self.v[2], 0.0],
                                    [self.n[0], self.n[1], self.n[2], 0.0],
                                    [0.0, 0.0, 0.0, 1.0]])
        # Gera a matrix de projeção
        return rotation_matrix * translation_matrix

    # Faz a transformação do objeto para simular a visualização da câmera
    def transform_visualization(self):
        # Calcula a matriz de transformação
        M = self.transformation_matrix()
        # Obtem os vertices do objeto
        vertices = self.obj.vertices
        # Adiciona 1 ao final de cada linha
        rows = vertices.shape[0]
        ones = np.ones((rows, 1))
        vertices = np.append(vertices, ones, axis=1)
        # Para cada linha, aplica a transformação
        for i in range(len(vertices)):
            vertices[i] = np.matmul(M, vertices[i])

        return vertices[:, :-1, ]


def main():
    obj = ObjLoader()
    file_name = 'src/modelos3D/small.obj'
    obj.load_3D_obj(file_name)
    # Cria a cena
    # Criando uma câmera apontada para o objeto passado como parâmetro
    cam = Camera(obj)
    # Definindo posição da câmera, ponto a ser visualizado e o vetor de orientação respectivamente
    cam.set_info([5, -0.5, -2], [11.4173, -5.64501, 3.65125], [1, 1, 1])
    
    # Mudando a visualização do objeto através da câmera
    print(cam.transform_visualization())


if __name__ == '__main__':
    main()
