import customtkinter as ctk
from Proceso import proceso as prcs

__name__ = "__main__"

# Falta terminar la logica para agrefar procesos a la lista de procesos, y mostrarla en la interfaz grafica.
# Ademas de agregar la logica para eliminar procesos

def ProcessCreate():
    PrcssNmDialog = ctk.CTkInputDialog(title="Crear Proceso", text="Ingrese el nombre del proceso:")
    processName = PrcssNmDialog.get_input()
    
    PrcssTamDialog = ctk.CTkInputDialog(title="Crear Proceso", text="Ingrese el tamaño del proceso:")
    processSize = PrcssTamDialog.get_input()

    # Obtener fecha y hora del sistema, o solo hora del sistema, para pasarlo a la var. tiempo_llegada

    proceso = prcs(nombre=processName, estado=True, tamano = processSize, prioridad = 0, tiempo_ejecucion = 0, tiempo_llegada = 0, tiempo_finalizacion = 0, tiempo_espera = 0, tiempo_atencion = 0)

def ProcessExit():
    # Borrar el proceso seleccionado de la lista de procesos, y actualizar la interfaz grafica
    print("Exiting the process...")


