import tkinter as tk
from test import *


def agregar_componentes_datos(frame):

    etiqueta_datos = tk.Label(frame, text="Análisis de datos", font=(
        "Arial", 18, "bold"), bg="lightblue")
    etiqueta_datos.pack(padx=10, pady=10)

    ciclos = tk.Label(frame, text="Ciclo de Ejecución", font=(
        "Arial", 18, "bold"), bg="lightblue")
    ciclos.pack(padx=10, pady=10)

    tiempoE = tk.Label(frame, text="Tiempo de Ejecución", font=(
        "Arial", 18, "bold"), bg="lightblue")
    tiempoE.pack(padx=10, pady=10)

    pC = tk.Label(frame, text="Valor de PC", font=(
        "Arial", 18, "bold"), bg="lightblue")
    pC.pack(padx=10, pady=10)

    registros = tk.Label(frame, text="Valor de Registros", font=(
        "Arial", 18, "bold"), bg="lightblue")
    registros.pack(padx=10, pady=10)
