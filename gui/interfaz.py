
import customtkinter as ctk
import __main__
app = ctk.CTk()

app.title("Simulador de gestion de memoria")
app.geometry("1000x700")


button = ctk.CTkButton(app, text="Llegada", command=__main__.ProcessCreate)
button.grid(row=0, column=0, padx=20, pady=20)

BtnExit = ctk.CTkButton(app, text="Salir", command=__main__.ProcessExit)
BtnExit.grid(row=0, column=1, padx=20, pady=20)

app.mainloop()