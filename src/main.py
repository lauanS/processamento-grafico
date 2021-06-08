from ObjLoader import ObjLoader
from ObjView import ObjView
from Scene import Scene
from Camera import Camera


def main():
    zoom = 0.5
    # Carregando um objeto
    obj = ObjLoader()
    file_name = 'src/modelos3D/ursinho.obj'
    obj.load_3D_obj(file_name)

    # Criando uma cena
    scene = Scene()
    scene.add_obj(obj)
    scene.set_scale([zoom, zoom, zoom])

    # Aplicando algumas transformações no obj sobre a cena
    new_obj = ObjLoader()
    file_name = 'src/modelos3D/ursinho.obj'
    new_obj.load_3D_obj(file_name)

    new_obj.vertices = scene.apply_scale()

    # Criando uma câmera apontada para o objeto passado como parâmetro
    cam = Camera(new_obj)
    # Definindo posição da câmera, ponto a ser visualizado e o vetor de orientação respectivamente
    cam.set_info([5, -0.5, -2], [11.4173, -5.64501, 3.65125], [1, 1, 1])
    # Mudando a visualização do objeto através da câmera
    new_obj.vertices = cam.transform_visualization()

    # Visualizando os resultados
    view = ObjView(new_obj)
    view.render()


if __name__ == '__main__':
    main()
