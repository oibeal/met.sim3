# Funciones que sirven de apoyo
import random
from constantes import *

def getMunicipioRandom():
    num_municipios = len(MEDIA_MINS_DESP) - 1 # esta tupla contiene tantas posiciones como municipios hay en el sistema
    return random.randint(0, num_municipios)