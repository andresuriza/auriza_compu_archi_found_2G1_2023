import tkinter as tk
from test import *


def agregar_componentes_seleccion(frame):
    etiqueta_seleccion = tk.Label(
        frame, font=("Arial", 25, "bold"), bg="aquamarine4")
    etiqueta_seleccion.grid(row=0, column=0, padx=10, pady=10)

    text = tk.Label(frame, text="Seleccion de procesador",
                    font=("Arial", 18, "bold"), bg="lightblue")
    text.grid(row=0, column=0, padx=10, pady=10)

    opcionesP = ["Procesador", "Uniciclo", "Multiciclo", "Segmentado R-> S",
                 "Segmentado UR-> L "]  # Lista de opciones
    seleccion = tk.StringVar()  # Variable para almacenar la opción seleccionada
    seleccion.set(opcionesP[0])

    select = tk.OptionMenu(frame, seleccion, *opcionesP)
    select.grid(row=0, column=1, padx=10, pady=10)

    boton_llamar = tk.Button(
        frame, text="Enviar", command=lambda: test(seleccion.get()))
    boton_llamar.grid(row=0, column=3, padx=10, pady=10)
# ------------------------------------------------------------------------------------------------------------------------------------------------
    text = tk.Label(frame, text="Modo de funcionamiento temporal",
                    font=("Arial", 18, "bold"), bg="lightblue")
    text.grid(row=2, column=0, padx=10, pady=10)

    opcionesMT = ["Step-By-Step", "Ritmo establecido",
                  "Completa al final"]  # Lista de opciones
    seleccionMT = tk.StringVar()  # Variable para almacenar la opción seleccionada
    seleccionMT.set(opcionesMT[0])

    select = tk.OptionMenu(frame, seleccionMT, *opcionesMT)
    select.grid(row=2, column=1, padx=10, pady=10)

    boton_llamar = tk.Button(
        frame, text="Enviar", command=lambda: test2(seleccionMT.get()))
    boton_llamar.grid(row=2, column=3, padx=10, pady=10)
