import numpy as np
from OpenGL.GL import *

from ObjLoader import ObjLoader


class Scene:
    def __init__(self):
        self.vertices = np.array([])
        self.obj_list = []

        # matrizes de transformações #
        self.scale = np.array([1, 1, 1])

    def scaling_matrix(self):
        return np.array([[self.scale[0], 0, 0, 0],
                         [0, self.scale[1], 0, 0],
                         [0, 0, self.scale[2], 0],
                         [0, 0, 0, 1]])

    def rotation_matrix(self):
        pass

    def translation_matrix(self):
        pass

    def shear_matrix(self):
        pass
    
    def model_matrix(self):
        pass

    def set_scale(self, scale):
        self.scale = np.array(scale)

    def apply_scale(self, scale=None):
        if(scale == None):
            scale = self.scale
        
        matrix = self.scaling_matrix()
        # Percorre todos os objetos da cena
        for obj in self.obj_list:
            # Obtem os vertices do objeto
            vertices = obj.vertices
            # Adiciona 1 ao final de cada linha
            rows = vertices.shape[0]
            ones = np.ones((rows, 1))
            vertices = np.append(vertices, ones, axis=1)
            # Para cada linha, aplica a transformação
            for i in range(len(vertices)):
                vertices[i] = np.matmul(matrix, vertices[i])

        return vertices[:,:-1,]

    def add_obj(self, obj):
        self.obj_list.append(obj)

    def print(self):
        print("Vertices:")
        print(self.vertices)
        print("Faces:")
        print(self.faces)


def main():
    obj = ObjLoader()
    file_name = 'src/modelos3D/small.obj'
    obj.load_3D_obj(file_name)
    # Cria a cena
    scene = Scene()

    scene.add_obj(obj)

    # Aplica transformações
    scene.set_scale([0.5, 0.5, 0.5])

    print(scene.apply_scale())


if __name__ == '__main__':
    main()