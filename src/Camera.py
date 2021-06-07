import numpy as np



class Camera:
    def __init__(self):
        self.position = np.array(
            (1, 3), dtype=[('x', np.float64), ('y', np.float64), ('z', np.float64)])
        self.look_at = np.array([])
        self.view_up = np.array([])

        # matrizes de transformações #
    def projection_matrix(self):
        translation_matrix = np.array([[1, 0, 0, -self.position['x']],
                                       [0, 1, 0, -self.position['y']],
                                       [0, 0, 1, -self.position['z']],
                                       [0, 0, 0, 1]])
        # Não ta nem um pouco completo
        u = v = n = []
        rotation_matrix = np.array([[u[0], u[1], u[2], 0]
                                    [v[0], v[1], v[2], 0]
                                    [n[0], n[1], n[2], 1]
                                    [0, 0, 0, 1]])

        # gerando a matrix de projeção
        return np.matmul(translation_matrix, rotation_matrix)

    def set_position():


def main():
    pass


if __name__ == '__main__':
    main()
