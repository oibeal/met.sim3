# constantes para facilitar calculos despues
MAX_H_MES = 160
# MEDIA_H_SERVICIO = 2 # horas de media para hacer un servicio

T_MAX = MAX_H_MES * 60 # el tiempo maximo se mide en minutos
# MEDIA_MINS_SERVICIO = MEDIA_H_SERVICIO * 60 # minutos de media para hacer un servicio

# constantes que usaremos en el sistema
# MUNICIPIO_ARAN = 0
# MUNICIPIO_OCA = 1
# MEDIA_MINS_DESP = (15, 10) # minutos de media de desplazamiento segun el municipio
# MEDIA_MINS_DESP_MUNICIPOS = 30 # minutos de media de desplazamiento entre municipios


# apartado B del ejercicio
EJERCICIO_A = "A"
EJERCICIO_B = "B"

SERVICIO_LEVE = 0
SERVICIO_ESTANDAR = 1
SERVICIO_GRAVE = 2
PROB_SERVICIOS = (35, 45, 20)
MEDIA_MINS_SERVICIO_CAT = (15, 30, 55)
VARIANZA_SERVICIO_CAT = (4, 6, 9)



TIEMPO_ESTADO = [120, 120, 15, 10, 30, 30]


TABLA_ALIAS = [
        [0.00, 0.00, 0.00, 0.25, 0.75, 0.00],
        [0.00, 0.00, 0.75, 0.00, 0.00, 0.25],
        [0.00, 1.00, 0.00, 0.00, 0.00, 0.00],
        [1.00, 0.00, 0.00, 0.00, 0.00, 0.00],
        [0.00, 1.00, 0.00, 0.00, 0.00, 0.00],
        [1.00, 0.00, 0.00, 0.00, 0.00, 0.00]
]

ESTADOS = {
    0: "ServicioOcaña",
    1: "ServicioAranjuez",
    2: "ViajeAA",
    3: "ViajeOO",
    4: "ViajeOA",
    5: "ViajeAO",
}

