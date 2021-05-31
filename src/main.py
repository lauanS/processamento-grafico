import numpy as np

from OpenGL.GL import *
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import math

class ObjLoader:
    def __init__(self):
        self.vertices = np.array([])
        self.faces = np.array([])
        self.file = ""
        ##

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
    
    def print(self):
        print("Vertices:")
        print(self.vertices)
        print("Faces:")
        print(self.faces)

class objItem:

    def __init__(self, object):
        self.angle = 0
        self.vertices = []
        self.faces = []
        self.coordinates = [0, 0, -65]  # [x,y,z]
        self.teddy = object
        self.position = [0, 0, -50]


    def render_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glClearColor(0.902, 0.902, 1, 0.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 0, math.sin(math.radians(self.angle)), 0, math.cos(math.radians(self.angle)) * -1, 0, 1, 0)
        glTranslatef(self.coordinates[0], self.coordinates[1], self.coordinates[2])

def main():
    obj = ObjLoader()
    file_name = 'src/modelos3D/small.obj'
    obj.load_3D_obj(file_name)
    obj.print()
    obj.render_scene()

def main_guide():
    pygame.init()
    pygame.display.set_mode((640, 480), pygame.DOUBLEBUF | pygame.OPENGL)
    pygame.display.set_caption("Ursinho super bonitinho")
    clock = pygame.time.Clock()
    # Feature checker
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glEnable(GL_CULL_FACE)
    #
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(800) / 600, .1, 1000.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    ursinho = ObjLoader()
    ursinho.load_3D_obj('src/modelos3D/ursinho.obj')
    objectTeddy = objItem(ursinho)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        objectTeddy.render_scene()
        objectTeddy.teddy.render_scene()
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    
if __name__ == '__main__':
    main_guide()
