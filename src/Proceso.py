from datetime import date
import time as tm
class proceso:
    #Atributos    
    nombre: str
    estado: bool
    tamano:int  

    #Check: dado que esto debe de ser tiempos manejados en min, seg, y/o fracciones de seg, cambiar el tipo de dato      
    tiempo_llegada: date
    tiempo_finalizacion: date
    tiempo_atencion: date
    tiempo_espera: date

    
    def __init__(self, nombre, estado, tamano, prioridad, tiempo_ejecucion, tiempo_llegada, tiempo_finalizacion, tiempo_espera, tiempo_atencion):
        self.nombre = nombre
        self.estado = estado
        self.tamano = tamano
        self.prioridad = prioridad
        self.tiempo_ejecucion = tiempo_ejecucion
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_finalizacion = tiempo_finalizacion
        self.tiempo_atencion = tiempo_atencion
        self.tiempo_espera = tiempo_espera

    
    