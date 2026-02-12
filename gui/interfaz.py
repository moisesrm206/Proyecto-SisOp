
import customtkinter as ctk
import time as tm
import sys
import os

# Agregar el directorio padre al path para poder importar desde src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#importar la clase proceso de la carpeta src del archivo Proceso.py
from src.Proceso import proceso as prcs

#Lista de procesos (sin tamaño máximo definido)
procesos = []

def CrearProceso():
    PrcssNmDialog = ctk.CTkInputDialog(title="Crear Proceso", text="Ingrese el nombre del proceso:")
    nombrePrcs = PrcssNmDialog.get_input()

    PrcssTamDialog = ctk.CTkInputDialog(title="Crear Proceso", text="Ingrese el tamaño del proceso:")
    tamProceso = PrcssTamDialog.get_input()
    
    tiempo_llegada = tm.localtime()
    print(tiempo_llegada)

    proceso = prcs(nombrePrcs, True, tamProceso, 0, 0, tiempo_llegada, 0, 0, 0)
    procesos.append(proceso)

def BorrarProceso():
    BorrarDialog = ctk.CTkInputDialog(title="Borrar Proceso", text="Ingrese el nombre del proceso a borrar:")
    nombrePrcs = BorrarDialog.get_input()
    for proceso in procesos:
        if proceso.nombre == nombrePrcs:
            procesos.remove(proceso)
            break
        else:
            print("Proceso no encontrado")
            

app = ctk.CTk()

app.title("Simulador de gestion de memoria")
app.geometry("1000x700")


BtnCrear = ctk.CTkButton(app, text="Llegada", command=CrearProceso)
BtnCrear.grid(row=0, column=0, padx=20, pady=20)

BtnBorrar = ctk.CTkButton(app, text="Salir", command=BorrarProceso)
BtnBorrar.grid(row=0, column=1, padx=20, pady=20)

Estado_Memoria = ctk.CTkFrame(
    app,
    width=100,
    height=450,
    border_width=2,
    border_color="black",
    fg_color="transparent",  # Sin relleno
)
Estado_Memoria.place(x=50, y=50)

app.mainloop()

