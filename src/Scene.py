import numpy as np
from OpenGL.GL import *

from ObjLoader import ObjLoader

# Classe do mundo, onde os objetos serão posicionados
class Scene:
    def __init__(self):
        self.vertices = np.array([])
        self.obj_list = []

        # matrizes de transformações #
        self.scale = np.array([1, 1, 1])

    # Matriz de escala
    def scaling_matrix(self, scale):
        return np.array([[scale[0], 0, 0, 0],
                         [0, scale[1], 0, 0],
                         [0, 0, scale[2], 0],
                         [0, 0, 0, 1]])

    # Matriz de rotação
    def rotation_matrix(self, angle, axis):
        # rotação em torno do eixo x #
        if (axis.lower() == 'x'):
          return np.array([[1, 0, 0, 0],
                          [0, np.cos(angle), -np.sin(angle), 0],
                          [0, np.sin(angle), np.cos(angle), 0],
                          [0, 0, 0, 1]])
        
        # rotação em torno do eixo y #
        elif(axis.lower() == 'y'):
          return np.array([[np.cos(angle), 0, np.sin(angle), 0],
                          [0, 1, 0, 0],
                          [-np.sin(angle), 0, np.cos(angle), 0],
                          [0, 0, 0, 1]])
        
        # rotação em torno do eixo z #
        elif(axis.lower() == 'z'):
          return np.array([[np.cos(angle), -np.sin(angle), 0, 0],
                          [np.sin(angle), np.cos(angle), 0, 0],
                          [-np.sin(angle), 0, 1, 0],
                          [0, 0, 0, 1]])
          
    # Matriz de translação
    def translation_matrix(self, distance):
        return np.array([[1, 0, 0, distance[0]],
                         [0, 1, 0, distance[1]],
                         [0, 0, 1, distance[2]],
                         [0, 0, 0, 1]])
  
    # Matriz de inclinação
    def shear_matrix(self, shear, axis):
        # distorção no eixo x #
        if (axis.lower() == 'x'):
          return np.array([[1, 0, 0, 0],
                          [shear[1], 1, 0, 0],
                          [shear[2], 0, 1, 0],
                          [0, 0, 0, 1]])
        
        # distorção no eixo y #
        elif(axis.lower() == 'y'):
          return np.array([[1, shear[0], 0, 0],
                          [shear[1], 1, 0, 0],
                          [shear[2], 0, 1, 0],
                          [0, 0, 0, 1]])
        
        # distorção no eixo z #
        elif(axis.lower() == 'z'):
          return np.array([[1, 0, shear[0], 0],
                          [0, 1, shear[1], 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])

    # Aplica a matriz de escala nos objetos
    def apply_scale(self):
        # Percorre todos os objetos da cena
        for index in range(len(self.obj_list)):
            obj = self.obj_list[index]
            matrix = self.scaling_matrix(obj.scale)
            self.apply_transform(matrix, index)
    
    # Aplica a rotação
    def apply_rotation(self):
        # Percorre todos os objetos da cena
        for index in range(len(self.obj_list)):
            obj = self.obj_list[index]
            matrix = self.rotation_matrix(obj.angle, obj.axis)
            self.apply_transform(matrix, index)

    # Aplica a translação
    def apply_translation(self):
        # Percorre todos os objetos da cena
        for index in range(len(self.obj_list)):
            obj = self.obj_list[index]
            matrix = self.translation_matrix(obj.distance)
            self.apply_transform(matrix, index)
    
    # Aplica a inclinação
    def apply_shear(self):        
        # Percorre todos os objetos da cena
        for index in range(len(self.obj_list)):
            obj = self.obj_list[index]
            matrix = self.shear_matrix(obj.shear, obj.shear_axis)
            self.apply_transform(matrix, index)

    # Aplica a transformação da matriz no objeto [index]
    def apply_transform(self, matrix, index):
        # Obtem os vertices do objeto
        obj = self.obj_list[index]
        vertices = obj.vertices
        # Adiciona 1 ao final de cada linha
        rows = vertices.shape[0]
        ones = np.ones((rows, 1))
        vertices = np.append(vertices, ones, axis=1)
        # Para cada linha, aplica a transformação
        for i in range(len(vertices)):
            vertices[i] = np.matmul(matrix, vertices[i])
        self.obj_list[index].vertices = vertices[:,:-1,]

    # Adiciona um objeto no mundo
    def add_obj(self, obj):
        self.obj_list.append(obj)

# Demonstração das operações em um objeto super pequeno (triângulo)
def main():
    obj = ObjLoader()
    file_name = 'src/modelos3D/small.obj'
    obj.load_3D_obj(file_name)

    # Cria a cena
    scene = Scene()


    # Aplica transformações
    obj.set_scale([0.5, 0.5, 0.5])
    obj.set_translation([0.5, 0.5, 0.5])
    obj.set_rotation(30, 'x')
    obj.set_shear([0,1,1], 'x')

    scene.add_obj(obj)
    print('\nObjeto original\n', obj.vertices)
    scene.apply_scale()
    print('\nEscala\n', scene.obj_list[0].vertices)
    scene.apply_translation()
    print('\nTranslação\n', scene.obj_list[0].vertices)
    scene.apply_rotation()
    print('\nRotação\n', scene.obj_list[0].vertices)
    scene.apply_shear()
    print('\nInclinação\n', scene.obj_list[0].vertices)


if __name__ == '__main__':
    main()
