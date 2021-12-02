""" Programa main """

from utils import *
from constantes import *
from tecnico import Tecnico
from servicio import Servicio

#class simulacion
class Simulacion:
    
    #init 
    def __init__(self,
        t_max = T_MAX,
        ejercicio = EJERCICIO_A
    ):
        self.tecnico = Tecnico()
        self.t_max = t_max
        self.t = 0
        self.ejercicio = ejercicio

    #simular
    def simular(self):
        while (self.t < self.t_max):
            servicio = self.generarServicio() # obtenemos el primer servicio de la cola
            self.tecnico.setServicio(servicio)
            
            t_desplazamiento = self.tecnico.iniciaDesplazamiento(servicio.getMunicipio()) # calculamos lo que tardaremos en desplazarnos
            t_servicio = self.tecnico.iniciaServicio() # calculamos lo que tardaremos en hacer el servicio
            self.t += t_desplazamiento + t_servicio # actualizamos el tiempo
    
    def generarServicio(self):
        # NOTE: no se cuando se genera un servicio pero se haria de esta forma
        municipio = getMunicipioRandom() # TODO: esta función hay que cambiarla por una que represente lo que dice el enunciado
        # enunciado: "Estadísticamente se ha comprobado que el volumen de avisos procedentes de Aranjuez es el triple de los procedentes de Ocaña"
        servicio = Servicio(municipio)
        if (self.ejercicio == EJERCICIO_B):
            gravedad = getGravedadRandom()
            servicio.setGravedad(gravedad)

        return servicio


if __name__ == '__main__':
    simul = Simulacion()
    simul.simular()
    
