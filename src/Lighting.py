import numpy as np


class Lighting:
  def __init__(self):
    # Define a posição da câmera
    self.camera = np.array([])
    # Define a posição da fonte (objeto) de luz
    self.position = np.array([800, 10,10])
    # Intensidade
    self.intensity = 1

  def diffuse_reflection_flat(self, point_a, point_b, point_c, k=1):
    """ Calcula a reflexão difusa 
        k = Coeficiente de reflexão difusa
    """
    # Obtem o vetor normal a face
    vector_ab = point_b - point_a
    vector_ac = point_c - point_a
    vector_normal = np.cross(vector_ab, vector_ac)
    # Obtem o ponto do meio da face
    face_position = (point_a + point_b + point_c)/3
    # Obtem o vetor da face a luz
    vector_face_to_light = self.position - face_position
    theta_angle = self.__angle_between(vector_face_to_light, vector_normal)

    return self.intensity * k * np.cos(theta_angle)

  # Retorna o vetor normal ao plano
  def normal(self, v1, v2):
    return np.cross(v1, v2)

  # Retorna o ângulo de reflexão da luz (L = vetor de incidência da luz; N = vetor normal do plano)
  def reflected_angle(self, L, N):
    # Obtendo o ângulo de incidência da luz
    unitL = L / np.linalg.norm(L)
    unitN = N / np.linalg.norm(N)
    product = np.dot(unitL, unitN)
    angle = np.arccos(product)
    reflected_angle = np.pi - angle
    
    return reflected_angle

  def light_intensity(self, L, N, R):
    ref_angle = self.reflected_angle(L, N)
    
    # Obtendo ângulo entre normal e a câmera
    unitR = R / np.linalg.norm(R)
    unitN = N / np.linalg.norm(N)
    product = np.dot(unitR, unitN)
    angle = np.arccos(product)

    observation_angle = angle - ref_angle

    return np.sin(observation_angle)

  def __unit_vector(self, vector):
    """ Retorna o vetor unitário """
    return vector / np.linalg.norm(vector)

  def __angle_between(self, v1, v2):
    """ Retorna o angulo em radiano entre dois vetores """
    v1_u = self.__unit_vector(v1)
    v2_u = self.__unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))  



