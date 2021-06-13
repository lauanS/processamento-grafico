import numpy as np
# Biblioteca para renderizar a imagem
from matplotlib import pyplot as plt

from ObjLoader import ObjLoader
from ObjView import ObjView
from Scene import Scene
from Camera import Camera


class Render:
    def __init__(self, object={}):
        # Objeto que será renderizado
        self.object = object
        # Matriz da imagem (600 por 600 para a mão)
        # Use 100x100 para o ursinho
        self.image = np.zeros((100, 100))

    def render(self):
        # Obtem as vertices do objeto (pontos)
        vertices = self.object.vertices
        faces = self.object.faces

        # Para cada ponto, desenha ele na matrix, usando seu x e y
        for i in range(len(faces)):
            point_a = vertices[int(faces[i][0]) - 1]
            point_b = vertices[int(faces[i][1]) - 1]
            point_c = vertices[int(faces[i][2]) - 1]
            self.draw_triangle(point_a, point_b, point_c)
            self.draw_triangle(-point_a, -point_b, -point_c)
        # Plota a matrix como uma imagem
        plt.imshow(self.image, interpolation='nearest')
        plt.show()

    # Função para desenhar um triângulo
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
            if(d <= 0):
                d = d + incE
                x = x + 1
            # Escolhe NE
            else:
                d = d + incNe
                x = x + 1
                y = y + 1
            self.draw_pixel(x, y)

    # Pinta um pixel na imagem
    def draw_pixel(self, x, y):
        # print(f'X: {x}[{int(x)}]|Y: {y}[{int(y)}]')
        self.image[int(len(self.image)/2) - int(x)
                   ][int(len(self.image)/2) - int(y)] = 1


def main():
    # -----------------------Carregando um objeto ----------------------- #
    obj = ObjLoader()
    pathHand = 'coarseTri.hand.obj'
    urso = 'ursinho.obj'
    file_name = 'src/modelos3D/' + urso
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
    cam.set_cam_info([5, 4, 3], [1.0, 1.0, 1.0], [1, 1, 1])
    cam.set_perspective_info(2, 2, -4, -8.5)
    cam.transform_visualization()
    obj.vertices = cam.change_perspective()
    # Renderiza ele
    render = Render(obj)
    render.render()


if __name__ == '__main__':
    main()
