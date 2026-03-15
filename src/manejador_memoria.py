from datetime import datetime
import time as tm

from src.Proceso import proceso as prcs


class ManejadorMemoria:
    def __init__(self, memoria_max: int):
        self.memoria_max = memoria_max
        self.procesos: list[prcs] = []
        self.procesos_espera: list[prcs] = []
        
        # Cada segmento es un diccionario con 'proceso' y 'tamano'
        self.segmentos: list[dict] = [] 
        self.tiempos_espera_inicio: dict[str, float] = {}
        self.inicializar_memoria()

    def inicializar_memoria(self):
        self.segmentos.clear()
        self.segmentos.append({"proceso": None, "tamano": self.memoria_max})


    def combinar_huecos_juntos(self):
        i = 0
        while i < len(self.segmentos) - 1:
            if (
                self.segmentos[i]["proceso"] is None
                and self.segmentos[i + 1]["proceso"] is None
            ):
                self.segmentos[i]["tamano"] += self.segmentos[i + 1]["tamano"]
                del self.segmentos[i + 1]
            else:
                i += 1

    # Algoritmo de Primer Ajuste/FirstFit
    def insertar_proceso_FF(self, proceso: prcs):
        self.combinar_huecos_juntos()
        for i, seg in enumerate(self.segmentos):
            if seg["proceso"] is None and seg["tamano"] >= proceso.tamano:
                proceso.estado = True

                espera_inicio = self.tiempos_espera_inicio.get(proceso.nombre)
                if espera_inicio is not None:
                    proceso.tiempo_espera = round(tm.time() - espera_inicio, 2)
                    del self.tiempos_espera_inicio[proceso.nombre]
                else:
                    proceso.tiempo_espera = 0

                self.segmentos[i] = {"proceso": proceso, "tamano": proceso.tamano}
                if seg["tamano"] > proceso.tamano:
                    self.segmentos.insert(
                        i + 1,
                        {"proceso": None, "tamano": (seg["tamano"] - proceso.tamano)},
                    )
                self.procesos.append(proceso)
                return True
        return False

    #Algoritmo de Mejor Ajuste/BestFit
    def insertar_proceso_BF(self, proceso: prcs):
        self.combinar_huecos_juntos()

        mejor_indice=-1  # Índice del mejor hueco encontrado, inicializado en -1 (ninguno encontrado)
        mejor_tamano=-1  # Tamaño del mejor hueco encontrado, inicializado en -1 (ninguno encontrado)
        
        for i, seg in enumerate(self.segmentos):
            if seg["proceso"] is None and seg["tamano"] >= proceso.tamano:
                if mejor_tamano == -1 or seg["tamano"] < mejor_tamano:
                    mejor_indice = i
                    mejor_tamano = seg["tamano"]

        if mejor_indice != -1:
            proceso.estado = True

            espera_inicio = self.tiempos_espera_inicio.get(proceso.nombre)
            if espera_inicio is not None:
                proceso.tiempo_espera = round(tm.time() - espera_inicio, 2)
                del self.tiempos_espera_inicio[proceso.nombre]
            else:
                proceso.tiempo_espera = 0

            tamano_hueco_original = self.segmentos[mejor_indice]["tamano"]
            self.segmentos[mejor_indice] = {"proceso": proceso, "tamano": proceso.tamano}
            if tamano_hueco_original > proceso.tamano:
                self.segmentos.insert(
                    mejor_indice + 1,
                    {"proceso": None, "tamano": (tamano_hueco_original - proceso.tamano)},
                )
            self.procesos.append(proceso)
            return True
        return False

    def crear_proceso(self, nombre: str, tamano: int, checkvar: str):
        proceso = prcs(nombre, True, tamano, 0, 0, datetime.now(), None, 0, None)
        insertado=False        
        if checkvar == "FF":
            insertado = self.insertar_proceso_FF(proceso)
        elif checkvar == "BF":
            insertado = self.insertar_proceso_BF(proceso)

        elif not insertado:
            proceso.estado = False
            self.tiempos_espera_inicio[proceso.nombre] = tm.time()
            self.procesos_espera.append(proceso)

        return proceso, insertado

    def eliminar_proceso(self, nombre: str):
        for i, seg in enumerate(self.segmentos):
            if seg["proceso"] and seg["proceso"].nombre == nombre and seg["proceso"].estado:
                seg["proceso"].estado = False
                self.segmentos[i] = {"proceso": None, "tamano": seg["tamano"]}
                self.combinar_huecos_juntos()
                return True
        return False

    def liberar_espacio(self):
        for proceso in self.procesos_espera[:]:
            if self.insertar_proceso_FF(proceso):
                self.procesos_espera.remove(proceso)

    def registrar_salida(self, nombre: str):
        for proceso in self.procesos:
            if proceso.nombre == nombre and proceso.estado:
                proceso.tiempo_finalizacion = datetime.now()
                proceso.tiempo_atencion = (
                    proceso.tiempo_finalizacion - proceso.tiempo_llegada
                )
                break

        eliminado = self.eliminar_proceso(nombre)
        if eliminado:
            self.liberar_espacio()
        return eliminado
    
    