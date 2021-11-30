""" Programa main """

from constantes import *
from tecnico import Tecnico
from servicio import Servicio

#class simulacion
class Simulacion:
    
    #init 
    def __init__(self,
        t_max = T_MAX
    ):
        self.tecnico = Tecnico()
        self.t_max = t_max
        self.t = 0
        # TODO: hay que crear e iniciar la cola de servicios

    #simular
    def simular(self):
        while (self.t < self.t_max):
            # TODO: hay que mirar servicios mientras self.t < self.t_max
            # y actualizar las metricas en cada bucle
            None


if __name__ == '__main__':
    simul = Simulacion()
    simul.simular()

