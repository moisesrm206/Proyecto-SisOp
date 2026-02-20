from datetime import datetime
import customtkinter as ctk
import tkinter as tk   # Canvas de Tkinter normal
from tkinter.ttk import Treeview as TreeVw
import time as tm
import sys
import os

# Agregar el directorio padre al path para poder importar desde src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# importar la clase proceso de la carpeta src del archivo Proceso.py
from src.Proceso import proceso as prcs

# Lista de procesos y segmentos de memoria
procesos: list[prcs] = []
procesos_espera: list[prcs] = []  # Lista de procesos en espera
segmentos = []  # cada segmento es {"proceso": objeto o None, "tamano": int}

# Diccionario para guardar tiempos de espera (clave = nombre del proceso)
tiempos_espera_inicio = {}

# Valor máximo de la memoria
MEMORIA_MAX = 100

def inicializar_memoria():
    segmentos.clear()
    segmentos.append({"proceso": None, "tamano": MEMORIA_MAX})

# Función para calcular espacio ocupado
def espacio_ocupado():
    return sum(int(seg["tamano"]) for seg in segmentos if seg["proceso"] and seg["proceso"].estado)

def CrearProceso():
    PrcssNmDialog = ctk.CTkInputDialog(title="Crear Proceso", text="Ingrese el nombre del proceso:")
    nombrePrcs = PrcssNmDialog.get_input()

    PrcssTamDialog = ctk.CTkInputDialog(title="Crear Proceso", text="Ingrese el tamaño del proceso:")
    tamProceso = int(PrcssTamDialog.get_input())
    
    tiempo_llegada = datetime.now()
    print(tiempo_llegada)

    proceso = prcs(nombrePrcs, True, tamProceso, 0, 0, tiempo_llegada, None, None, None)

    if not insertar_proceso(proceso):
        # No hay hueco suficiente, el proceso entra en espera
        proceso.estado = False
        tiempos_espera_inicio[proceso.nombre] = tm.time()
        procesos_espera.append(proceso)

    actualizar_tabla()

def combinar_huecos():
    i = 0
    while i < len(segmentos) - 1:
        if segmentos[i]["proceso"] is None and segmentos[i+1]["proceso"] is None:
            # unir huecos contiguos
            segmentos[i]["tamano"] += segmentos[i+1]["tamano"]
            del segmentos[i+1]
        else:
            i += 1

def insertar_proceso(proceso):
    combinar_huecos()
    for i, seg in enumerate(segmentos):
        if seg["proceso"] is None and seg["tamano"] >= proceso.tamano:
            proceso.estado = True            

            # calcular tiempo de espera si aplica
            espera_inicio = tiempos_espera_inicio.get(proceso.nombre)
            if espera_inicio is not None:
                proceso.tiempo_espera = round(tm.time() - espera_inicio, 2)
                del tiempos_espera_inicio[proceso.nombre]
            else:
                proceso.tiempo_espera = 0

            # ocupar parte del hueco
            segmentos[i] = {"proceso": proceso, "tamano": proceso.tamano}
            if seg["tamano"] > proceso.tamano:
                segmentos.insert(i+1, {"proceso": None, "tamano": seg["tamano"] - proceso.tamano})
            procesos.append(proceso)
            return True
    return False

def BorrarProceso():
    BorrarDialog = ctk.CTkInputDialog(title="Salir Proceso", text="Ingrese el nombre del proceso:")
    nombrePrcs = BorrarDialog.get_input()

    for proceso in procesos:
        if proceso.nombre == nombrePrcs and proceso.estado:            
            proceso.tiempo_finalizacion = datetime.now()
            proceso.tiempo_atencion = proceso.tiempo_finalizacion - proceso.tiempo_llegada
            
        else:
            print("Proceso no encontrado o no activo")

    encontrado = eliminar_proceso(nombrePrcs)

    if not encontrado:
        print("Proceso no encontrado")

    # Intentar meter procesos en espera si hay espacio
    liberar_espacio()

    actualizar_tabla()

def eliminar_proceso(nombre):
    for i, seg in enumerate(segmentos):
        if seg["proceso"] and seg["proceso"].nombre == nombre and seg["proceso"].estado:
            seg["proceso"].estado = False
            # ↓ quita la línea de tiempo_finalizacion, ya se asignó en BorrarProceso
            segmentos[i] = {"proceso": None, "tamano": seg["tamano"]}
            combinar_huecos()
            return True
    return False

def liberar_espacio():
    for p in procesos_espera[:]:
        if insertar_proceso(p):
            procesos_espera.remove(p)

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

sb_y= ctk.CTkScrollbar(app, orientation="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=sb_y.set)
sb_x = ctk.CTkScrollbar(app, orientation="horizontal", command=tabla.xview)
tabla.configure(xscrollcommand=sb_x.set)

def formato_tiempo(timedelta):
    if timedelta is None or not hasattr(timedelta, 'total_seconds'):
        return "00:00:00"
    total_segundos = int(timedelta.total_seconds())
    horas, resto = divmod(total_segundos, 3600)
    minutos, segundos = divmod(resto, 60)
    return f"{horas:02}:{minutos:02}:{segundos:02}"

def actualizar_tabla():
    # Limpiar tabla
    for i in tabla.get_children():
        tabla.delete(i)
    for proceso in procesos:        
        tabla.insert("", "end", values=(proceso.nombre, "Activo" if proceso.estado else "Inactivo",
                                        proceso.tamano, proceso.tiempo_llegada.strftime("%H:%M:%S"), proceso.tiempo_finalizacion.strftime("%H:%M:%S") if proceso.tiempo_finalizacion else "00:00:00",
                                        formato_tiempo(proceso.tiempo_atencion), proceso.tiempo_espera))
    for proceso in procesos_espera:
        tabla.insert("", "end", values=(proceso.nombre, "En espera",
                                        proceso.tamano, proceso.tiempo_llegada.strftime("%H:%M:%S"), proceso.tiempo_finalizacion.strftime("%H:%M:%S") if proceso.tiempo_finalizacion else "00:00:00",
                                        formato_tiempo(proceso.tiempo_atencion), proceso.tiempo_espera))

    # Limpiar representación gráfica
    for widget in Estado_Memoria.winfo_children():
        widget.destroy()

    # Canvas de Tkinter normal
    canvas = tk.Canvas(Estado_Memoria, width=120, height=550, bg="#c3d4e7", highlightthickness=0)
    canvas.pack()

    total_altura = 550
    unidad_altura = total_altura / MEMORIA_MAX

    y = 0
    for seg in segmentos:
        altura = int(seg["tamano"]) * unidad_altura
        if seg["proceso"]:
            color = "#4a90e2" if seg["proceso"].estado else "#999999"
            canvas.create_rectangle(0, y, 120, y + altura, fill=color, outline="black")
            canvas.create_text(60, y + altura/2, text=f"{seg['proceso'].nombre} ({seg['tamano']})")
        else:
            canvas.create_rectangle(0, y, 120, y + altura, fill="#d9d9d9", outline="black")
            canvas.create_text(60, y + altura/2, text=f"Hueco ({seg['tamano']})")
        y += altura

tabla.grid(padx = 150, pady = 80, row=1, column=1)

# Inicializar memoria con un hueco total
inicializar_memoria()

app.mainloop()
