class proceso:
    #Atributos    
    nombre: str
    estado: str
    tamano:int        
    tiempo_llegada: int
    tiempo_finalizacion: int
    tiempo_atencion: int
    tiempo_espera: int
    
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

    
    