# Funciones que sirven de apoyo
import random
from constantes import *

def getMunicipioRandom():
    num_municipios = len(MEDIA_MINS_DESP) - 1 # esta tupla contiene tantas posiciones como municipios hay en el sistema
    return random.randint(0, num_municipios)

def getGravedadRandom():
    x = random.randint(0, 100) # para sacar un porcentaje
    fin = False
    prob = 0
    pos = 0
    while (not fin and pos < len(PROB_SERVICIOS)):
        prob += PROB_SERVICIOS[pos]
        if (x <= prob):
            fin = True
        else:
            pos += 1
    
    return pos