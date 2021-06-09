import numpy as np
from matplotlib import pyplot as plt

from ObjLoader import ObjLoader
from ObjView import ObjView
from Scene import Scene
from Camera import Camera

class Render:
    def __init__(self, object = {}):
        self.object = object
        self.image = np.zeros((600, 600))

    def render(self):
        vertices = self.object.vertices
        for i in range(len(vertices)):
            startpoint = vertices[i]
            self.draw_pixel(startpoint[0], startpoint[1])
        
        plt.imshow(self.image, interpolation='nearest')
        plt.show()

    def draw_triangle(self, point_a, point_b, point_c):
        self.draw_line(point_a[0], point_a[1], point_b[0], point_b[1])
        self.draw_line(point_b[0], point_b[1], point_c[0], point_c[1])
        self.draw_line(point_c[0], point_c[1], point_a[0], point_a[1])
    
    # Desenha uma linha na imagem
    def draw_line(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0

        # Valor inicial de d
        d = 2 * dy - dx 
        # Incremento de E
        incE = 2 * dy
        # Incremento de NE
        incNe = 2 * (dy - dx)

        x = x0
        y = y0
        self.draw_pixel(x, y)

        while(x < x1):
            # Escolhe E
            if(d < x1):                
                d = d + incE
                x = x + 1
            # Escolhe NE
            else:                
                d = d + incE
                x = x + 1
                y = y + 1
            self.draw_pixel(x, y)

    # Pinta um pixel na imagem
    def draw_pixel(self, x, y):
        # print(f'X: {x}[{int(x)}]|Y: {y}[{int(y)}]')
        self.image[299 - int(x)][299 - int(y)] = 1
        



def main():
    # -----------------------Carregando um objeto ----------------------- #
    obj = ObjLoader()
    file_name = 'src/modelos3D/coarseTri.hand.obj'
    obj.load_3D_obj(file_name)

    # -----------------------Criando uma cena----------------------- #
    zoom = 0.8
    scene = Scene()
    scene.add_obj(obj)
    scene.set_scale([zoom, zoom, zoom])
    obj.vertices = scene.apply_scale()
    # ----------------------- Camera ----------------------- #
    # Criando uma câmera apontada para o objeto passado como parâmetro
    cam = Camera(obj)
    # Definindo posição da câmera, ponto a ser visualizado e o vetor de orientação respectivamente
    cam.set_cam_info([5, 4, 3], [0.0, 10.0, 0.0], [0, 0, 1])
    cam.set_perspective_info(2, 2, -4, -8.5)
    cam.transform_visualization()
    obj.vertices = cam.change_perspective()
    # Renderiza ele
    render = Render(obj)
    render.render()

if __name__ == '__main__':
    main()