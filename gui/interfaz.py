
import customtkinter as ctk
from tkinter.ttk import Treeview as TreeVw
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
    corner_radius=20,
)
Estado_Memoria.place(x=50, y=70)


tabla = TreeVw(app, columns=(1,2,3,4,5,6,7), show="headings", height = 8)
tabla.heading(1, text="Nombre")
tabla.heading(2, text="Estado")
tabla.heading(3, text="Tamaño")
tabla.heading(4, text="Llegada")
tabla.heading(5, text="Finalización")
tabla.heading(6, text="Tiempo de atención")
tabla.heading(7, text="Tiempo de espera")

''' #TODO: Agregar un loop para mostrar los procesos en la tabla, y actualizar la tabla cada vez que se cree o borre un proceso
    tambien cambiar la forma en la que se muestra la tabla para que no se vaya mas alla del borde del frame de estado de memoria,
    y agregar un scroll para la tabla en caso de que se agreguen muchos procesos.
'''

tabla.grid(padx = 150, pady = 80, column=1)

app.mainloop()

