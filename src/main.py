import customtkinter as ctk
from Proceso import proceso as prcs

#Falta terminar la logica para agrefar procesos a la lista de procesos, y mostrarla en la interfaz grafica. Ademas de agregar la logica para eliminar procesos
def ProcessCreate():
    PrcssNmDialog = ctk.CTkInputDialog(title="Crear Proceso", text="Ingrese el nombre del proceso:")
    processName = PrcssNmDialog.get_input()
    
    PrcssTamDialog = ctk.CTkInputDialog(title="Crear Proceso", text="Ingrese el tamaño del proceso:")
    processSize = PrcssTamDialog.get_input()

    proceso = prcs(nombre=processName, estado=True, tamano = processSize, prioridad = 0, tiempo_ejecucion = 0, tiempo_llegada = 0, tiempo_finalizacion = 0, tiempo_espera = 0, tiempo_atencion = 0)

def ProcessExit():
    print("Exiting the process...")

app = ctk.CTk()

app.title("Simulador de gestion de memoria")
app.geometry("700x550")


button = ctk.CTkButton(app, text="Llegada", command=ProcessCreate)
button.grid(row=0, column=0, padx=20, pady=20)

BtnExit = ctk.CTkButton(app, text="Salir", command=ProcessExit)
BtnExit.grid(row=0, column=1, padx=20, pady=20)

app.mainloop()
