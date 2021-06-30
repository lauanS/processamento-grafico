from ObjLoader import ObjLoader
from Scene import Scene
from Camera import Camera
from Render import Render

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
    # Posicionando o ursinho
    # No ar (perto da borda superior)
    ursinho.set_translation([-80, 0, 10])
    # Defindo uma inclinação de 90° (em radianos) no eixo y
    # Para deixar o ursinho olhando para baixo
    ursinho.set_rotation(1.5708, 'y')

    # --- Mão --- #
    zoom = 0.75
    # Posicionando a mão que está arremesando o ursinho
    hand.set_scale([zoom, zoom, zoom])
    hand.set_rotation(1.5708, 'z')
    hand.set_translation([80, 0, 1])

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
    render.render_light()
    
if __name__ == '__main__':
    main()
