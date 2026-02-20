from datetime import timedelta
from datetime import datetime
from datetime import date
import time as tm
class proceso:
    # Atributos    
    nombre: str
    estado: bool
    tamano: int  

    # TODO: Revisar que el tipo de dato date sea correcto, y si es necesario importar alguna libreria para manejar fechas
    tiempo_llegada: datetime
    tiempo_finalizacion: datetime
    tiempo_atencion: timedelta
    tiempo_espera: float
    tiempo_espera_inicio: None  #NUEVO

    def __init__(self, nombre, estado, tamano, prioridad, tiempo_ejecucion,
                 tiempo_llegada, tiempo_finalizacion, tiempo_espera, tiempo_atencion):
        self.nombre = nombre
        self.estado = estado
        self.tamano = int(tamano)
        self.prioridad = prioridad
        self.tiempo_ejecucion = tiempo_ejecucion
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_finalizacion = tiempo_finalizacion
        self.tiempo_atencion = tiempo_atencion
        self.tiempo_espera = tiempo_espera
        self.tiempo_espera_inicio = None  #NUEVO
