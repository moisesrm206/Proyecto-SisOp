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
procesos: list[prcs] = []

def CrearProceso():
    PrcssNmDialog = ctk.CTkInputDialog(title="Crear Proceso", text="Ingrese el nombre del proceso:")
    nombrePrcs = PrcssNmDialog.get_input()

    PrcssTamDialog = ctk.CTkInputDialog(title="Crear Proceso", text="Ingrese el tamaño del proceso:")
    tamProceso = PrcssTamDialog.get_input()
    
    # TODO: Revisar o cambiar el tipo de dato, ya que el formato de fecha no es algo muy deseado al mostrarse en tabla, 
    # TODO: un ejemplo de como sale es: 2026 02 15 12 35 20 05 06, esto es año, mes, dia, hora, minuto, segundo, y probablemente milisegundos,
    # TODO: revisar si es posible mostrar solo la hora, o el formato de fecha deseado, o si es necesario cambiar el tipo de dato a string y mostrar la fecha en el formato deseado
        
    tiempo_llegada = tm.strftime("%H:%M:%S", tm.localtime())
    print(tiempo_llegada)

    proceso = prcs(nombrePrcs, True, tamProceso, 0, 0, tiempo_llegada, 0, 0, 0)
    procesos.append(proceso)
    actualizar_tabla()

def BorrarProceso():
    BorrarDialog = ctk.CTkInputDialog(title="Salir Proceso", text="Ingrese el nombre del proceso:")
    nombrePrcs = BorrarDialog.get_input()

    encontrado = False

    for proceso in procesos:
        if proceso.nombre == nombrePrcs:
            proceso.estado = False  # Cambiar a inactivo
            proceso.tiempo_finalizacion = tm.strftime("%H:%M:%S", tm.localtime())  # Registrar hora de salida
            encontrado = True
            break

    if not encontrado:
        print("Proceso no encontrado")

    actualizar_tabla()

app = ctk.CTk()

app.title("Simulador de gestion de memoria")
app.geometry("1000x700")

BtnCrear = ctk.CTkButton(app, text="Llegada", command=CrearProceso)
BtnCrear.grid(row=0, column=0, padx=20, pady=20)

BtnBorrar = ctk.CTkButton(app, text="Salir", command=BorrarProceso)
BtnBorrar.grid(row=0, column=1, padx=20, pady=20)

Estado_Memoria = ctk.CTkFrame(
    app,
    width=120,
    height=550,
    border_width=1,
    border_color="black",
    fg_color="#c3d4e7",
    corner_radius=15,
)
Estado_Memoria.place(x=50, y=70)


tabla = TreeVw(app, columns=(1,2,3,4,5,6,7), show="headings", height = 12)
tabla.heading(1, text="Nombre")
tabla.heading(2, text="Estado")
tabla.heading(3, text="Tamaño")
tabla.heading(4, text="Llegada")
tabla.heading(5, text="Finalización")
tabla.heading(6, text="Tiempo de atención")
tabla.heading(7, text="Tiempo de espera")

tabla.column(1, width=60)
tabla.column(2, width=50)
tabla.column(3, width=60)
tabla.column(4, width=120)
tabla.column(5, width=120)
tabla.column(6, width=120)
tabla.column(7, width=120)

# ? INFO: El scrollbar horizontal no funciona, no se muestran barras para mover, pero si funciona el vertical,
# ? no se muestra la barra tampoco, pero se puede mover usando la rueda del raton
sb_y= ctk.CTkScrollbar(app, orientation="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=sb_y.set)
sb_x = ctk.CTkScrollbar(app, orientation="horizontal", command=tabla.xview)
tabla.configure(xscrollcommand=sb_x.set)

def actualizar_tabla():
    for i in tabla.get_children():
        tabla.delete(i)
    for proceso in procesos:
        tabla.insert("", "end", values=(proceso.nombre, proceso.estado, proceso.tamano, proceso.tiempo_llegada, proceso.tiempo_finalizacion, proceso.tiempo_atencion, proceso.tiempo_espera))


tabla.grid(padx = 150, pady = 80, row=1, column=1)


app.mainloop()
