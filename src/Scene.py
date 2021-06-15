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
    def scaling_matrix(self):
        return np.array([[self.scale[0], 0, 0, 0],
                         [0, self.scale[1], 0, 0],
                         [0, 0, self.scale[2], 0],
                         [0, 0, 0, 1]])

    # Matriz de rotação
    def rotation_matrix(self):
        # rotação em torno do eixo x #
        if (self.axis.lower() == 'x'):
          return np.array([[1, 0, 0, 0],
                          [0, np.cos(self.angle), -np.sin(self.angle), 0],
                          [0, np.sin(self.angle), np.cos(self.angle), 0],
                          [0, 0, 0, 1]])
        
        # rotação em torno do eixo y #
        elif(self.axis.lower() == 'y'):
          return np.array([[np.cos(self.angle), 0, np.sin(self.angle), 0],
                          [0, 1, 0, 0],
                          [-np.sin(self.angle), 0, np.cos(self.angle), 0],
                          [0, 0, 0, 1]])
        
        # rotação em torno do eixo z #
        elif(self.axis.lower() == 'z'):
          return np.array([[np.cos(self.angle), -np.sin(self.angle), 0, 0],
                          [np.sin(self.angle), np.cos(self.angle), 0, 0],
                          [-np.sin(self.angle), 0, 1, 0],
                          [0, 0, 0, 1]])
          
    # Matriz de translação
    def translation_matrix(self):
        return np.array([[1, 0, 0, self.distance[0]],
                         [0, 1, 0, self.distance[1]],
                         [0, 0, 1, self.distance[2]],
                         [0, 0, 0, 1]])
  
    # Matriz de inclinação
    def shear_matrix(self):
        # distorção no eixo x #
        if (self.axis.lower() == 'x'):
          return np.array([[1, 0, 0, 0],
                          [self.shear[1], 1, 0, 0],
                          [self.shear[2], 0, 1, 0],
                          [0, 0, 0, 1]])
        
        # distorção no eixo y #
        elif(self.axis.lower() == 'y'):
          return np.array([[1, self.shear[0], 0, 0],
                          [self.shear[1], 1, 0, 0],
                          [self.shear[2], 0, 1, 0],
                          [0, 0, 0, 1]])
        
        # distorção no eixo z #
        elif(self.axis.lower() == 'z'):
          return np.array([[1, 0, self.shear[0], 0],
                          [0, 1, self.shear[1], 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])
    
    # Define a intensidade da escala - scale:array3x1 = [x, y, z]
    def set_scale(self, scale):
        self.scale = np.array(scale)

    # Aplica a matriz de escala nos objetos
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
    
    # Recebe o ângulo em radianos e o eixo em torno do qual o objeto deve rotacionar-se
    # axis = 'x', 'y' ou 'z' 
    def set_rotation(self, angle, axis):
        self.angle = angle
        self.axis = axis

    # Aplica a rotação
    def apply_rotation(self, angle=None, axis=None):
        if(angle == None or axis == None):
            angle = self.angle
            axis = self.axis
        
        matrix = self.rotation_matrix()
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

    # recebe um array [x,y,z] com a distância desejada entre o objeto e cada eixo
    def set_translation(self, distance):
        self.distance = np.array(distance)

    # Aplica a translação
    def apply_translation(self, distance=None):
        if(distance == None):
            distane = self.distance
        
        matrix = self.translation_matrix()
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
    
    # Recebe um array [x,y,z] com a distorção (shear) e o eixo com relação
    # ao qual se aplicará a distorção.
    # Distorção no eixo x: [0,y,z], onde y e z correspondem à distorção com relação a x
    # Distorção no eixo y: [x,0,z], onde x e z correspondem à distorção com relação a y
    # Distorção no eixo z: [x,y,0], onde x e y correspondem à distorção com relação a z
    def set_shear(self, shear, axis):
      self.shear = np.array(shear)
      self.axis = axis

    # Aplica a inclinação
    def apply_shear(self, shear=None, axis=None):
        if(shear == None or axis == None):
            shear = self.shear
            axis = self.axis
        
        matrix = self.shear_matrix()
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

    scene.add_obj(obj)

    # Aplica transformações
    scene.set_scale([0.5, 0.5, 0.5])
    scene.set_translation([0.5, 0.5, 0.5])
    scene.set_rotation(30, 'x')
    scene.set_shear([0,1,1], 'x')

    print('\nObjeto original\n', obj.vertices)
    print('\nEscala\n', scene.apply_scale())
    print('\nTranslação\n', scene.apply_translation())
    print('\nRotação\n', scene.apply_rotation())
    print('\nInclinação\n', scene.apply_shear())


if __name__ == '__main__':
    main()
