import tkinter as tk
from test import *
from imageSection import agregar_componentes_visualizacion
from dataSection import *
from selectionSection import *
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulator Control")  # Título de la ventana

# Crear los frames para las secciones
frame_seleccion = tk.Frame(ventana, bg="aquamarine4", padx=350, pady=50)
frame_seleccion.pack(side=tk.TOP, fill=tk.X)

frame_datos = tk.Frame(ventana, bg="azure3", padx=100)
frame_datos.pack(side=tk.RIGHT, fill=tk.Y, expand=True)

frame_visualizacion = tk.Frame(ventana, bg="white", padx=300, pady=250)
frame_visualizacion.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Agregar componentes a los frames
agregar_componentes_seleccion(frame_seleccion)
agregar_componentes_datos(frame_datos)
agregar_componentes_visualizacion(frame_visualizacion)

ventana.mainloop()
