import tkinter as tk
from tkinter import ttk, messagebox, Radiobutton


def register():
    team= entry_equipo.get().strip()
    integrante= entry_integrante.get().strip()
    categoria = categoria_var.get()
    micro = micro_var.get()
    rol = rol_var.get()
    reglas = reglas_var.get()
    materiales= materiales_var.get()

    if not team:
        messagebox.showerror("ERROR","Error, El nombre del equipo es obligatorio")
        return
    if not integrante:
        messagebox.showerror("ERROR","Error, El nombre del integrante es obligatorio")
        return
    if not micro:
        messagebox.showerror("ERROR","Error, El nombre del microcontrolador a usar es obligatorio")
        return
    if not reglas:
        messagebox.showerror("error","Acepte los terminos primero")
        return
    reglas = "si" if reglas else "no"
    materiales= "si" if materiales else "no"

    print("formulario cansat")
    print(f"Equipo: {team}")
    print(f"Categoria: {categoria}")
    print(f"Microcontrolador: {micro}")
    print(f"Integrante: {integrante}")
    print(f"Rol: {rol}")
    print(f"Materiales: {materiales}")
    print(f"Reglas: {reglas}")

    messagebox.showinfo("Registrado correctamente", "registro completado")

root = tk.Tk()
root.title("formulario cansat")
root.geometry("400x800")
root.resizable(False,True)

style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel",font=("Segoe UI",10))
style.configure("Tittle.TLabel",font=("Segoe UI",10,"bold"))
style.configure("TButton",font=("Segoe UI",10,"bold"))
style.configure("Accent.TButton",background="#2E8B57",foreground="white")

main_frame=ttk.Frame(root,padding=20)
main_frame.pack(fill="both",expand=True)

ttk.Label(main_frame, text="formulario cansat", style="Title.TLabel").grid(row=0, column=0, columnspan=2, pady=10)

#DATOS
datos_frame= ttk.LabelFrame(main_frame, text="Datos del Equipo", padding=10)
datos_frame.grid(row=1,column=0,columnspan=2,sticky="ew",pady=10)

ttk.Label(datos_frame, text="Equipo").grid(row=0,column=0,sticky="w")
entry_equipo= ttk.Entry(datos_frame, width=30)
entry_equipo.grid(row=0,column=1,pady=5)

ttk.Label(datos_frame,text="Integrante:").grid(row=1,column=0,sticky="w")
entry_integrante= ttk.Entry(datos_frame, width= 30)
entry_integrante.grid(row=1,column=1,pady=5)


# SECCION CATEGORIAS
categoria_frame=ttk.LabelFrame(main_frame,text="Categoria",padding=10)
categoria_frame.grid(row=2,column=0,columnspan=2,sticky="ew",pady=10)

categoria_var= tk.StringVar(value="CANSAT BÁSICO")

ttk.Radiobutton(categoria_frame, text="Cansat Basico", variable=categoria_var,value="Cansat Básico").grid(row=0,column=0,sticky="w")
ttk.Radiobutton(categoria_frame, text= "Cansat Intermedio", variable=categoria_var,value="Cansat Intermedio").grid(row=1,column=0,sticky="w")
ttk.Radiobutton(categoria_frame, text= "Cansat Avanzado", variable=categoria_var,value="Cansat Avanzado").grid(row=2,column=0,sticky="w")

# SECCION MICROCONTROLADOR
ttk.Label(main_frame, text="Microcontrolador:").grid(row=3,column=0,columnspan=2,sticky="ew",pady=(8,0))

micro_var = tk.StringVar()
combo_micro = ttk.Combobox(main_frame, textvariable= micro_var, state="readonly", width=27)
combo_micro ["values"] = ("ESP32","ESP32-S3","ARDUINO","RASPBERRY PI ZERO 2W", "RASPBERRY PI PICO")
combo_micro.current(0)
combo_micro.grid(row=3,column=1,padx=(150,0),pady=(10,0))

# SECCION ROL

rol_frame = ttk.LabelFrame(main_frame, text="ROL DEL INTEGRANTE", padding=10)
rol_frame.grid(row=4,column=0,columnspan=2,sticky="ew",pady=10)

rol_var = tk.StringVar(value="PROGRAMACION")

ttk.Radiobutton(rol_frame, text="Programación", variable=rol_var, value="Programación").grid(row=0, column=0, sticky="w")
ttk.Radiobutton(rol_frame, text="Electrónica", variable=rol_var, value="Electrónica").grid(row=1, column=0, sticky="w")
ttk.Radiobutton(rol_frame, text="Diseño", variable=rol_var, value="Diseño").grid(row=2, column=0, sticky="w")

# CONFIRMACIONES DE LLENADO
confirm_frame= ttk.LabelFrame(main_frame, text="Confirmacion", padding=10)
confirm_frame.grid(row=5,column=0,columnspan=2,sticky="ew",pady=10)

materiales_var = tk.BooleanVar()
ttk.Checkbutton(confirm_frame, text="tiene todos los componenetes", variable=materiales_var).grid(row=0,column=0,sticky="w")

reglas_var = tk.BooleanVar()
ttk.Checkbutton(confirm_frame, text= "terminos y condiciones", variable=reglas_var).grid(row=1,column=0,sticky="w")


# BOTON DE CONFIRMACION
btn_registrar= ttk.Button(main_frame, text="Registrar",command=register)
btn_registrar.grid(row=6,column=0,columnspan=2,pady=20,ipadx=40,ipady=5)



root.mainloop()