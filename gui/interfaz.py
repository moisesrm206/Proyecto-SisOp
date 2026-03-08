import customtkinter as ctk
import tkinter as tk   # Canvas de Tkinter normal
from tkinter.ttk import Treeview as TreeVw
import sys
import os

# TODO: Dejar de usar grid como sistema de posicionamiento y usar otro, que sea dificil que tenga problemas de posicionamiento,  con el fin de no tener la interfaz como una tabla, y aparezcan botones o algun otro objeto en lugares no tan deseados

# Agregar el directorio padre al path para poder importar desde src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# importar gestor de memoria y procesos
from src.manejador_memoria import ManejadorMemoria

# Valor máximo de la memoria
MEMORIA_MAX = 100

# Altura total para representar la memoria
TAMANNO_REPRESENTACION = 520  


manager = ManejadorMemoria(MEMORIA_MAX)


def CrearProceso():
    PrcssNmDialog = ctk.CTkInputDialog(
        title="Crear Proceso", text="Ingrese el nombre del proceso:"
    )
    nombrePrcs = PrcssNmDialog.get_input()
    if not nombrePrcs:
        return

    PrcssTamDialog = ctk.CTkInputDialog(
        title="Crear Proceso", text="Ingrese el tamaño del proceso:"
    )
    tam_input = PrcssTamDialog.get_input()
    if tam_input is None:
        return
    try:
        tamProceso = int(tam_input)
    except ValueError:
        return

    manager.crear_proceso(nombrePrcs, tamProceso)

    actualizar_tabla()


def BorrarProceso():
    BorrarDialog = ctk.CTkInputDialog(
        title="Salir Proceso", text="Ingrese el nombre del proceso:"
    )
    nombrePrcs = BorrarDialog.get_input()
    if not nombrePrcs:
        return

    manager.registrar_salida(nombrePrcs)

    actualizar_tabla()


app = ctk.CTk()
app.title("Simulador de gestion de memoria")
app.geometry("1200x680")

checkvarFF = ctk.StringVar(value="off")
rdBtnFF = ctk.CTkRadioButton(app, text="First Fit", variable=checkvarFF)
rdBtnFF.grid(row=0, column=0, padx=20, pady=20)

checkvarBF = ctk.StringVar(value="off")
rdBtnBF = ctk.CTkRadioButton(app, text="Best Fit", variable=checkvarBF)
rdBtnBF.grid(row=0, column=1, padx=20, pady=20)

BtnCrear = ctk.CTkButton(app, text="Llegada", command=CrearProceso)
BtnCrear.grid(row=1, column=0, padx=20, pady=20)

BtnBorrar = ctk.CTkButton(app, text="Salir", command=BorrarProceso)
BtnBorrar.grid(row=1, column=1, padx=20, pady=20)

Estado_Memoria = ctk.CTkFrame(
    app,
    width=120,
    height=TAMANNO_REPRESENTACION,
    border_width=1,
    border_color="black",
    fg_color="#c3d4e7",
    corner_radius=15,
)
Estado_Memoria.grid(row=2, column=0, padx=20, pady=20, rowspan=2)

tabla = TreeVw(app, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height=12)
tabla.grid(row=2, column=4, padx=20, pady=20, rowspan=2)  # Ajustar posición y tamaño de la tabla
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

sb_y = ctk.CTkScrollbar(app, orientation="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=sb_y.set)
sb_x = ctk.CTkScrollbar(app, orientation="horizontal", command=tabla.xview)
tabla.configure(xscrollcommand=sb_x.set)


def formato_tiempo(delta):
    if delta is None or not hasattr(delta, "total_seconds"):
        return "00:00:00"
    total_segundos = int(delta.total_seconds())
    horas, resto = divmod(total_segundos, 3600)
    minutos, segundos = divmod(resto, 60)
    return f"{horas:02}:{minutos:02}:{segundos:02}"


def actualizar_tabla():
    # Limpiar tabla
    for i in tabla.get_children():
        tabla.delete(i)

    for proceso in manager.procesos:
        tabla.insert("", "end", values=(
                proceso.nombre, "Activo" if proceso.estado else "Inactivo", proceso.tamano, proceso.tiempo_llegada.strftime("%H:%M:%S"),
                (
                    proceso.tiempo_finalizacion.strftime("%H:%M:%S")
                    if proceso.tiempo_finalizacion
                    else "00:00:00"
                ),
                formato_tiempo(proceso.tiempo_atencion), proceso.tiempo_espera,
            ),
        )
        
    for proceso in manager.procesos_espera:
        tabla.insert("", "end", values=(
                proceso.nombre, "En espera", proceso.tamano, proceso.tiempo_llegada.strftime("%H:%M:%S"),
                (
                    proceso.tiempo_finalizacion.strftime("%H:%M:%S")
                    if proceso.tiempo_finalizacion
                    else "00:00:00"
                ),
                formato_tiempo(proceso.tiempo_atencion), proceso.tiempo_espera,
            ),
        )

    # Limpiar representación gráfica
    for widget in Estado_Memoria.winfo_children():
        widget.destroy()

    # Canvas de Tkinter normal
    canvas = tk.Canvas(
        Estado_Memoria, width=120, height=TAMANNO_REPRESENTACION, bg="#c3d4e7", highlightthickness=0
    )
    canvas.pack()

    total_altura = TAMANNO_REPRESENTACION
    unidad_altura = total_altura / manager.memoria_max

    y: float = 0
    for seg in manager.segmentos:
        altura = int(seg["tamano"]) * unidad_altura
        if seg["proceso"]:
            color = "#4a90e2" if seg["proceso"].estado else "#999999"
            canvas.create_rectangle(0, y, 120, y + altura, fill=color, outline="black")
            canvas.create_text(
                60, y + altura / 2, text=f"{seg['proceso'].nombre} ({seg['tamano']})"
            )
        else:
            canvas.create_rectangle(
                0, y, 120, y + altura, fill="#d9d9d9", outline="black"
            )
            canvas.create_text(60, y + altura / 2, text=f"Hueco ({seg['tamano']})")
        y += altura


tabla.grid(padx=150, pady=80, row=1, column=1)

actualizar_tabla()

app.mainloop()
