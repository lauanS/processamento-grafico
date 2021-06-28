import numpy as np
from OpenGL.GL import *

from ObjLoader import ObjLoader
from ObjView import ObjView
from Scene import Scene

class Camera:
    def __init__(self, obj):
        self.position = np.array([])
        self.look_at = np.array([])
        self.view_up = np.array([])
        self.obj = obj

    # Define as informações principais da câmera
    def set_cam_info(self, position, look_at, view_up):
        self.position = np.array(position)
        self.look_at = np.array(look_at)
        self.view_up = np.array(view_up)

    # Define os limites da projeção perspectiva
    def set_perspective_info(self, left, bottom, near, far):
        self.left = left
        self.right = -left
        self.bottom = bottom
        self.top = -bottom
        self.near = near
        self.far = far

    # Calcula os vetores U, V e N
    def calculate_uvn(self):
        self.n = (self.look_at - self.position) / abs(self.look_at - self.position)
        self.u = (self.view_up * self.n) / abs(self.view_up * self.n)
        self.v = np.cross(self.n, self.u)
        
    # Define as matrizes de translação e rotação da câmera e retorna a matriz de projeção
    def generate_projection_matrix(self):
        self.calculate_uvn()
        translation_matrix = np.matrix([[1, 0, 0, -self.position[0]],
                                        [0, 1, 0, -self.position[1]],
                                        [0, 0, 1, -self.position[2]],
                                        [0, 0, 0, 1]])

        rotation_matrix = np.matrix([[self.u[0], self.u[1], self.u[2], 0.0],
                                     [self.v[0], self.v[1], self.v[2], 0.0],
                                     [self.n[0], self.n[1], self.n[2], 0.0],
                                     [0.0, 0.0, 0.0, 1.0]])
        # Gera a matriz de projeção
        return rotation_matrix * translation_matrix

    # Faz a transformação do objeto para simular a visualização da câmera
    def transform_visualization(self):
        # Calcula a matriz de projeção
        M = self.generate_projection_matrix()
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

    # Muda a perspectiva do objeto
    def change_perspective(self):
        # Calcula a matriz de projeção
        M = np.matrix([[self.near / self.right, 0, 0, 0],
                       [0, self.near / self.top, 0, 0],
                       [0, 0, -((self.far + self.near) / (self.far - self.near)), -
                        (2*(self.far * self.near) / (self.far - self.near))],
                       [0, 0, -1, 0]])
        # Converte o vetor de posição da câmera (Pe) em uma matriz 4x1
        cam_position = np.append(self.position, 1).reshape(4, 1)
        # Gera as coordenadas intermediárias (Pc) em um vetor
        clipping_coordinates = np.squeeze(np.asarray((M * cam_position)))
        # Gera as coordenadas canônicas (Pndc)
        p_ndc = np.array([clipping_coordinates[0] / clipping_coordinates[3],
                          clipping_coordinates[1] / clipping_coordinates[3],
                          clipping_coordinates[2] / clipping_coordinates[3]])

        # Obtem os vertices do objeto
        vertices = self.obj.vertices

        for i in range(len(vertices)):
            vertices[i] = p_ndc * vertices[i]

        return vertices

# Testa a camera em um objeto "inclinado"
def main():
    obj = ObjLoader()
    file_name = 'src/modelos3D/ursinho.obj'
    obj.load_3D_obj(file_name)
    # Cria a cena
    zoom = 0.3
    scene = Scene()
    scene.add_obj(obj)
    # Define a escala e a inclinação
    scene.set_scale([zoom, zoom, zoom])
    scene.set_shear([1,1,0], 'x')
    # Aplica as modificações
    obj.vertices = scene.apply_scale()
    scene.obj_list[0] = obj
    obj.vertices = scene.apply_shear()
    # Criando uma câmera apontada para o objeto passado como parâmetro
    cam = Camera(obj)
    # Definindo posição da câmera, ponto a ser visualizado e o vetor de orientação respectivamente
    cam.set_cam_info([10, 2, -6], [11, 5, 2], [1, 1, 1])
    cam.set_perspective_info(2, 2, -4, -8.5)
    cam.transform_visualization()
    obj.vertices = cam.change_perspective()

    # Renderizando com o OpenGL
    view = ObjView(obj)
    view.render()

if __name__ == '__main__':
    main()
