import numpy as np


class Lighting:
    def __init__(self):
      # Define a posição da câmera
      self.camera = []
      # Define a posição da fonte (objeto) de luz
      self.source = []
      # Define o plano (vetores diretores)
      self.plane = []

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



