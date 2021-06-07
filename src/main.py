from ObjLoader import ObjLoader
from ObjView import ObjView

def main():
    obj = ObjLoader()
    file_name = 'src/modelos3D/ursinho.obj'
    obj.load_3D_obj(file_name)

    view = ObjView(obj)
    view.render()
    
if __name__ == '__main__':
    main()
