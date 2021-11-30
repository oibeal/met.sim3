""" Servicios de averia """

from constantes import *
import numpy as np
import random

#class servicio
class Servicio:
    
    #init 
    def __init__(self, municipio, gravedad = None):
        self.municipio = municipio
        self.gravedad = gravedad # esto es para el apartado B del ejercicio
   
    def getGravedad(self):
        return self.gravedad
    
    def getMunicipio(self):
        return self.municipio

    def getTServicio(self):
        if (self.gravedad is not None):
            # ejercicio B
            m_servicio = MEDIA_MINS_SERVICIO_CAT[self.gravedad]
            v_servicio = VARIANZA_SERVICIO_CAT[self.gravedad]
            t_servicio = random.normalvariate(m_servicio, v_servicio)
        else:
            # ejercicio A
            m_servicio = MEDIA_MINS_SERVICIO
            t_servicio = np.random.exponential(m_servicio)

        return t_servicio