import numpy as np
from OpenGL.GL import *

# Classe para carregar um objeto salvo
class ObjLoader:
    def __init__(self):
        self.vertices = np.array([])
        self.faces = np.array([])
        # Scale
        self.scale = np.array([1, 1, 1])
        # Rotation
        self.angle = 0
        self.axis = "x"
        # translation
        self.distance = np.array([0, 0, 0])
        
        self.shear = np.array([1, 1, 1])
        self.shear_axis = np.array('x')
        self.file = ""

    # Define a intensidade da escala - scale:array3x1 = [x, y, z]
    def set_scale(self, scale):
        self.scale = np.array(scale)

    # Recebe o ângulo em radianos e o eixo em torno do qual o objeto deve rotacionar-se
    # axis = 'x', 'y' ou 'z' 
    def set_rotation(self, angle, axis):
        self.angle = angle
        self.axis = axis    

    # recebe um array [x,y,z] com a distância desejada entre o objeto e cada eixo
    def set_translation(self, distance):
        self.distance = np.array(distance)
    
    # Recebe um array [x,y,z] com a distorção (shear) e o eixo com relação
    # ao qual se aplicará a distorção.
    # Distorção no eixo x: [0,y,z], onde y e z correspondem à distorção com relação a x
    # Distorção no eixo y: [x,0,z], onde x e z correspondem à distorção com relação a y
    # Distorção no eixo z: [x,y,0], onde x e y correspondem à distorção com relação a z
    def set_shear(self, shear, axis):
      self.shear = np.array(shear)
      self.shear_axis = axis
    
    # Carrega um objeto 3D no disco
    def load_3D_obj(self, file_name):
        try:
            obj_file = open(file_name)
            for line in obj_file:
                # Vertices: 'v x_value y_value z_value'
                if line[:2] == "v ":
                    vertex = np.array(line.split()[1:])
                    vertex = np.array([vertex.astype(np.double)])
                    if self.vertices.size == 0:
                        self.vertices = vertex
                    else:
                        self.vertices = np.concatenate((self.vertices, vertex), axis=0)
                # Faces: 'f v1_value v2_value v3_value ... vn_value'
                elif line[:2] == "f ":
                    face = np.array(line.split()[1:])
                    face = np.array([face.astype(np.double)])
    
                    if self.faces.size == 0:
                        self.faces = face
                    else:
                        self.faces = np.concatenate((self.faces, face), axis=0)
            obj_file.close()
        except IOError:
            print(".obj file not found.")
    
    def show_3D_obj(self):
        return 1
    
    # Renderiza a cena usando o OpenGL (debug)
    def render_scene(self):
        if len(self.faces) > 0:
            ##
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
            glBegin(GL_TRIANGLES)
            for face in self.faces:
                for f in face:
                    vertexDraw = self.vertices[int(f) - 1]
                    if int(f) % 3 == 1:
                        glColor4f(0.282, 0.239, 0.545, 0.35)
                    elif int(f) % 3 == 2:
                        glColor4f(0.729, 0.333, 0.827, 0.35)
                    else:
                        glColor4f(0.545, 0.000, 0.545, 0.35)
                    glVertex3fv(vertexDraw)
            glEnd()
    
    # Imprime os vertices e as faces (debug)
    def print(self):
        print("Vertices:")
        print(self.vertices)
        print("Faces:")
        print(self.faces)

# Testa se está carregando um objeto corretamente 
def main():
    obj = ObjLoader()
    file_name = 'src/modelos3D/ursinho.obj'
    obj.load_3D_obj(file_name)
    obj.print()
    obj.render_scene()
    
if __name__ == '__main__':
    main()
