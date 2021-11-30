""" Tecnico del sistema """

import numpy as np
from utils import *
from constantes import *

#class tecnico
class Tecnico:
    
    #init 
    def __init__(self):
        self.servicio = None
        self.estado = None
        self.municipio = getMunicipioRandom() # Hay que discutir donde comienza el tecnico por defecto

    def setServicio(self, servicio):
        self.servicio = servicio
    
    def getEstado(self):
        return self.estado
    
    def getMunicipio(self):
        return self.municipio

    def iniciaServicio(self):
        self.estado = TEC_EN_SERVICIO
        if (self.servicio is not None):
            m_servicio = self.servicio.getTServicio()
        else:
            m_servicio = 0

        return m_servicio

    def iniciaDesplazamiento(self, municipio): # NOTE: (Oier) el municipio podria obtenerse del servicio en vez de mandarse por aqui
        self.estado = TEC_DESPLAZANDOSE
        if (self.municipio == municipio):
            m_desplazamiento = MEDIA_MINS_DESP[self.municipio]
        else:
            m_desplazamiento = MEDIA_MINS_DESP_MUNICIPOS
            self.municipio = municipio # actualizamos el municipio al que se mueve

        return np.random.exponential(m_desplazamiento)