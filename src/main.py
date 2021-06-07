from ObjLoader import ObjLoader
from ObjView import ObjView
from Scene import Scene

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

    # Visualizando os resultados
    view = ObjView(new_obj)
    view.render()
    
if __name__ == '__main__':
    main()
