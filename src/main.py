from ObjLoader import ObjLoader
from Scene import Scene
from Camera import Camera
from Render import Render

def main():
    # -----------------------Carregando um objeto ----------------------- #
    obj = ObjLoader()
    # Objetos
    hand = 'coarseTri.hand.obj'
    urso = 'ursinho.obj'
    file_name = 'src/modelos3D/' + urso
    obj.load_3D_obj(file_name)

    # -----------------------Criando uma cena----------------------- #
    # Criando a cena e adicionando seu objeto nela
    scene = Scene()
    scene.add_obj(obj)
    # Definindo os valores das transformações
    zoom = 6
    # Definindo um zoom no ursinho para visualizar melhor os detalhes
    scene.set_scale([zoom, zoom, zoom])
    # Posicionando o ursinho
    # Perto da parede (borda a esquerda da imagem)
    # E no chão (Borda inferior da imagem)
    scene.set_translation([50, -80, 1])
    # Defindo uma inclinação de 90° (em radianos) no eixo y
    # Para deixar o ursinho de castigo olhando para parede (borda a esquerda da img)
    scene.set_rotation(1.5708, 'y')
    # Aplicando cada transformação separadamente
    # e atualizando o objeto presente no mundo
    obj.vertices = scene.apply_rotation()
    scene.obj_list[0] = obj
    obj.vertices = scene.apply_scale()
    scene.obj_list[0] = obj
    obj.vertices = scene.apply_translation()
    
    # ----------------------- Camera ----------------------- #
    # Criando uma câmera apontada para o objeto passado como parâmetro
    cam = Camera(obj)
    # Definindo posição da câmera, ponto a ser visualizado e o vetor de orientação respectivamente
    # Position - lookAt - viewUp
    cam.set_cam_info([5, 5, 3], [6.0, 6.0, 5.0], [ 1, 1,  1])
    # Frustum
    cam.set_perspective_info(2, 2, -4, -8.5) 
    # Aplicando a transformação 
    cam.transform_visualization()
    obj.vertices = cam.change_perspective()
    # Renderizando o objeto
    render = Render(obj)
    render.render_matplot()

if __name__ == '__main__':
    main()
