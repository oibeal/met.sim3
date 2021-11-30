# constantes para facilitar calculos despues
MAX_H_MES = 160
MEDIA_H_SERVICIO = 2 # horas de media para hacer un servicio

T_MAX = MAX_H_MES * 60 # el tiempo maximo se mide en minutos
MEDIA_MINS_SERVICIO = MEDIA_H_SERVICIO * 60 # minutos de media para hacer un servicio

# constantes que usaremos en el sistema
MUNICIPIO_ARAN = 0
MUNICIPIO_OCA = 1
MEDIA_MINS_DESP = (15, 10) # minutos de media de desplazamiento segun el municipio
MEDIA_MINS_DESP_MUNICIPOS = 30 # minutos de media de desplazamiento entre municipios

TEC_DESPLAZANDOSE = 0
TEC_EN_SERVICIO = 1

# apartado B del ejercicio
SERVICIO_LEVE = 0
SERVICIO_ESTANDAR = 1
SERVICIO_GRAVE = 2
MEDIA_MINS_SERVICIO_CAT = (15, 30, 55)
VARIANZA_SERVICIO_CAT = (4, 6, 9)