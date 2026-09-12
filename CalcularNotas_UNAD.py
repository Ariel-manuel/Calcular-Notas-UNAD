import tkinter as tk
from tkinter import ttk

class PromedioApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Cálculo de Promedio UNAD Nota 75%")
        
        self.etiqueta_nota = tk.Label(self.ventana, text="Ingrese el Total de Puntos Obtenidos: ")
        self.etiqueta_nota.pack()
        
        self.entrada_nota = tk.Entry(self.ventana, justify='center')
        self.entrada_nota.pack()
        self.entrada_nota.config(fg='blue')
        
        self.etiqueta_formula = tk.Label(self.ventana, text="Ingrese la fórmula para calcular el promedio:")
        self.etiqueta_formula.pack()
        
        self.entrada_formula = tk.Entry(self.ventana, justify='center', show='*')
        self.entrada_formula.pack()
        self.entrada_formula.insert(0, "nota * 5 / 120")  # Fórmula por defecto
        
        self.mostrar_formula = tk.IntVar()
        self.checkbox_formula = ttk.Checkbutton(self.ventana, text="Mostrar fórmula", variable=self.mostrar_formula, command=self.actualizar_formula)
        self.checkbox_formula.pack()
        
        self.boton_calcular = tk.Button(self.ventana, text="Calcular Nota", command=self.calcular_promedio)
        self.boton_calcular.pack(pady=10)        
        self.boton_limpiar = tk.Button(self.ventana, text="Nueva Calificación", command=self.limpiar_calificacion)
        self.boton_limpiar.pack(pady=10)
        
        self.etiqueta_promedio = tk.Label(self.ventana, text="Su promedio de la nota es: ")
        self.etiqueta_promedio.pack()
        self.etiqueta_promedio.config(fg='green')
        
        self.etiqueta_porcentaje = tk.Label(self.ventana, text="El porcentaje Obtenido: ")
        self.etiqueta_porcentaje.pack()
        self.etiqueta_porcentaje.config(fg='blue')
        
        self.etiqueta_desarrollo = tk.Label(self.ventana, text="Desarrollador: Ariel Berna @ 2023", anchor='sw')
        self.etiqueta_desarrollo.pack(side='left', padx=10, pady=10)
        
        self.ventana.mainloop()
    
    def calcular_promedio(self):
        try:
            nota = float(self.entrada_nota.get())
            formula = self.entrada_formula.get()
            promedio = eval(formula)  # Evaluar la fórmula ingresada
            porcentaje = (promedio / 5) * 100
            self.etiqueta_promedio.config(text=f"El promedio de la nota es: {promedio:.1f}")
            self.etiqueta_porcentaje.config(text=f"El porcentaje de la nota es: {porcentaje:.1f}%")
        except ValueError:
            tk.messagebox.showerror("Error", "Ingrese un valor numérico válido.")
    
    def limpiar_calificacion(self):
        self.entrada_nota.delete(0, tk.END)
    
    def actualizar_formula(self):
        if self.mostrar_formula.get() == 1:
            self.entrada_formula.config(show='')
        else:
            self.entrada_formula.config(show='*')

# Iniciar la aplicación
app = PromedioApp()
