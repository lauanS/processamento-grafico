from OpenGL.GL import *
import pygame
from OpenGL.GLU import *
import math

from ObjLoader import ObjLoader

class ObjView:
    def __init__(self, object):
        self.angle = 0
        self.vertices = []
        self.faces = []
        self.coordinates = [0, 0, -65]  # [x,y,z]
        self.object3D = object
        self.position = [0, 0, -50]

    def render_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glClearColor(0.902, 0.902, 1, 0.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 0, math.sin(math.radians(self.angle)), 0, math.cos(math.radians(self.angle)) * -1, 0, 1, 0)
        glTranslatef(self.coordinates[0], self.coordinates[1], self.coordinates[2])

    def render(self):
        pygame.init()
        pygame.display.set_mode((640, 480), pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption("Visualização pelo OpenGL - pygame")
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

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            self.render_scene()
            self.object3D.render_scene()
            pygame.display.flip()
            clock.tick(30)
        pygame.quit()

if __name__ == '__main__':
    obj = ObjLoader()
    file_name = 'src/modelos3D/ursinho.obj'
    obj.load_3D_obj(file_name)
    view = ObjView(obj)
    view.render()