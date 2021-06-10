from ObjLoader import ObjLoader
from ObjView import ObjView
from Scene import Scene
from Camera import Camera


def main():
    zoom = 0.4  # Para visualizar a perspectiva o melhor valor que achamos foi 0.4
    # Carregando um objeto
    obj = ObjLoader()
    file_name = 'src/modelos3D/ursinho.obj'
    obj.load_3D_obj(file_name)

    # -----------------------Criando uma cena----------------------- #
    scene = Scene()
    scene.add_obj(obj)
    scene.set_scale([zoom, zoom, zoom])

    # Aplicando algumas transformações no obj sobre a cena
    new_obj = ObjLoader()
    file_name = 'src/modelos3D/ursinho.obj'
    new_obj.load_3D_obj(file_name)

    new_obj.vertices = scene.apply_scale()

    # -----------------------Câmera e Projeção----------------------- #

    # OBS(*): Execute a função transform_visualization separadamente da change_perspective se não souber os valores corretos,
    # pois aparentemente fica uma coisa estranha.

    # Criando uma câmera apontada para o objeto passado como parâmetro
    cam = Camera(new_obj)

    # Definindo posição da câmera, ponto a ser visualizado e o vetor de orientação respectivamente
    cam.set_cam_info([5, 2, -3], [16.0481, -2.92233, 2.75786], [1, 1, 1])

    # Mudando a visualização do objeto através da câmera (*)
    # new_obj.vertices = cam.transform_visualization()

    # Definindo os limites da projeção de perspectiva - Parâmetros: (left, bottom, -near, -far)
    # por padrão right = -left e top = -bottom; Obs*: near e far não podem ter o mesmo valor
    cam.set_perspective_info(2, 2, -4, -8.5)

    # Mudando a perspectiva de visualização do objeto através da câmera (*)
    new_obj.vertices = cam.change_perspective()

    # -------------------Visualizar os resultados------------------- #
    view = ObjView(new_obj)
    view.render()


if __name__ == '__main__':
    main()
