import numpy as np
# Biblioteca para renderizar a imagem
from matplotlib import pyplot as plt

from ObjLoader import ObjLoader
from Scene import Scene
from Camera import Camera

# Classe que rasteriza a imagem gerada
class Render:
    def __init__(self, obj_list):
        # Objeto que será renderizado
        self.obj_list = obj_list
        # Matriz da imagem (600 por 600 para a mão) com zoom em 0.8
        # Use 100x100 para o ursinho com zoom em 0.8
        # Use 1200x1200 no ursinho com zoom em 6
        self.image = np.zeros((1200, 1200))

    # Atualiza o tamanho da matrix - shape:tupla -> (x,y)
    def set_img_shape(self, shape):
        self.image = np.zeros(shape)

    # Renderiza todas as arestas do objeto
    def render(self):
        for index in range(len(self.obj_list)):
            obj = self.obj_list[index]
            # Obtem as vertices do objeto (pontos)
            vertices = obj.vertices
            faces = obj.faces

            # Para cada face, desenha seu triangulo
            for i in range(len(faces)):
                point_a = vertices[int(faces[i][0]) - 1]
                point_b = vertices[int(faces[i][1]) - 1]
                point_c = vertices[int(faces[i][2]) - 1]
                self.draw_triangle(point_a, point_b, point_c)

        # Plota a matrix como uma imagem
        plt.imshow(self.image, interpolation='nearest')
        plt.show()
    
    # Função para renderixar apenas os pontos do objeto
    def render_pixels(self):
        # Obtem as vertices do objeto (pontos)
        vertices = self.object.vertices

        # Para cada ponto, desenha ele na matrix, usando seu x e y
        for i in range(len(vertices)):
            self.draw_pixel(vertices[i][0], vertices[i][1])


        vertices = self.object2.vertices

        # Para cada ponto, desenha ele na matrix, usando seu x e y
        for i in range(len(vertices)):
            self.draw_pixel(vertices[i][0], vertices[i][1])
        # Plota a matrix como uma imagem
        plt.imshow(self.image, interpolation='nearest')
        plt.show()

    # Função para desenhar um triângulo
    def draw_triangle(self, point_a, point_b, point_c):
        self.draw_line(point_a[0], point_a[1], point_b[0], point_b[1])
        self.draw_line(point_b[0], point_b[1], point_c[0], point_c[1])
        self.draw_line(point_c[0], point_c[1], point_a[0], point_a[1])

    # Função para renderizar um objeto usando plot.fill do matplotlib
    def render_matplot(self):
        for index in range(len(self.obj_list)):
            obj = self.obj_list[index]
            # Obtem as vertices do objeto (pontos)
            vertices = obj.vertices
            faces = obj.faces

            # Para cada ponto, desenha ele na matrix, usando seu x e y
            for i in range(len(faces)):
                point_a = vertices[int(faces[i][0]) - 1]
                point_b = vertices[int(faces[i][1]) - 1]
                point_c = vertices[int(faces[i][2]) - 1]

                norm = int(len(self.image)/2)
                triangle_x = [point_a[0] + norm, point_b[0] + norm, point_c[0] + norm, point_a[0] + norm]
                triangle_y = [point_a[1] + norm, point_b[1] + norm, point_c[1] + norm, point_a[1] + norm]

                plt.fill(triangle_x, triangle_y, 'y')
        # Plota a matrix como uma imagem
        plt.imshow(self.image, interpolation='nearest')
        plt.show()

    # Função interna para obter o sinal de um valor
    def __signal(self, value):
        if(value < 0):
            return -1
        return 1

    # Desenha uma linha na imagem 
    def draw_line(self, x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        signal_x = self.__signal(x1 - x0)
        signal_y = self.__signal(y1 - y0)
        
        x = x0
        y = y0
        if(signal_x < 0):
            x -= 1
        if(signal_y < 0):
            y -= 1

        # trocar deltax com deltay dependendo da inclinacao da reta 
        interchange = False
        if ( dy > dx):
            tmp = dx
            dx = dy
            dy = tmp
            interchange = True

        # Valor inicial de d
        d = 2 * dy - dx

        for i in range(int(dx)):
            self.draw_pixel(x, y)
            while(d >= 0):
                if(interchange):
                    x = x + signal_x;
                else:
                    y = y + signal_y;
                d = d - 2 * dx
            
            if(interchange):
                y = y + signal_y
            else:
                x = x + signal_x
            
            d = d + 2 * dy

    # Pinta um pixel na imagem
    def draw_pixel(self, x, y):
        # print(f'X: {x}[{int(x)}]|Y: {y}[{int(y)}]')
        self.image[int(len(self.image)/2) - int(x)
                   ][int(len(self.image)/2) - int(y)] = 1


# Demonstração usando nosso rasterizador
def main():
    # -----------------------Carregando um objeto ----------------------- #
    #--- Objetos ---#
    # paths
    hand_path = 'coarseTri.hand.obj'
    ursinho_path = 'ursinho.obj'
    base_path = 'src/modelos3D/'
    # Carregando os objetos
    hand = ObjLoader()
    ursinho = ObjLoader()
    
    hand.load_3D_obj(base_path + hand_path)
    ursinho.load_3D_obj(base_path + ursinho_path)

    # -----------------------Criando uma cena----------------------- #
    # Definindo as transformações de cada objeto

    # --- URSINHO --- #
    zoom = 6
    # Definindo um zoom no ursinho para visualizar melhor os detalhes
    ursinho.set_scale([zoom, zoom, zoom])
    # Deixando o ursinho "na pose" 
    # Segurando na parede (borda a esquerda da imagem)
    # E no chão (Borda inferior da imagem)
    ursinho.set_translation([50, -78, 1])
    # Defindo uma inclinação de 90° (em radianos) no eixo z para deixar o ursinho em pé
    ursinho.set_rotation(1.5708, 'z')

    # --- Mão --- #
    zoom = 0.9
    hand.set_scale([zoom, zoom, zoom])

    # Criando a cena e adicionando seu objeto nela
    scene = Scene()
    scene.add_obj(ursinho)
    scene.add_obj(hand)
    # Aplicando cada transformação separadamente
    # e atualizando o objeto presente no mundo
    scene.apply_rotation()
    scene.apply_scale()
    scene.apply_translation()
    
    # ----------------------- Camera ----------------------- #
    # Criando uma câmera apontada para o objeto passado como parâmetro
    cam = Camera(scene.obj_list)
    # Definindo posição da câmera, ponto a ser visualizado e o vetor de orientação respectivamente
    # Position - lookAt - viewUp
    cam.set_cam_info([5, 5, 3], [6.0, 6.0, 5.0], [ 1, 1,  1])
    # Frustum
    cam.set_perspective_info(2, 2, -4, -8.5) 
    # Aplicando a transformação 
    # cam.transform_visualization()
    cam.change_perspective()
    # ----------------------- Render ----------------------- #
    # Renderizando o objeto
    render = Render(cam.obj_list)
    render.render()



if __name__ == '__main__':
    main()
