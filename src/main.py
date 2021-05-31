import numpy as np

class ObjLoader(object):
    def __init__(self):
        self.vertices = np.array([])
        self.faces = np.array([])
        self.file = ""
        ##

    def load_3D_obj(self, file_name):
        try:
            obj_file = open(file_name)
            for line in obj_file:
                # Vertices: 'v x_value y_value z_value'
                if line[:2] == "v ":
                    vertex = np.array(line.split()[1:])
                    vertex = np.array([vertex.astype(np.double)])
                    if self.vertices.size == 0:
                        self.vertices = vertex
                    else:
                        self.vertices = np.concatenate((self.vertices, vertex), axis=0)
                # Faces: 'f v1_value v2_value v3_value ... vn_value'
                elif line[:2] == "f ":
                    face = np.array(line.split()[1:])
                    face = np.array([face.astype(np.double)])
    
                    if self.faces.size == 0:
                        self.faces = face
                    else:
                        self.faces = np.concatenate((self.faces, face), axis=0)
            obj_file.close()
        except IOError:
            print(".obj file not found.")
    
    def show_3D_obj(self):
        return 1;
    
    def print(self):
        print("Vertices:")
        print(self.vertices)
        print("Faces:")
        print(self.faces)
        
def main():
    obj = ObjLoader()
    file_name = 'src/modelos3D/small.obj'
    obj.load_3D_obj(file_name)
    obj.print()

if __name__ == '__main__':
    main()
