import tkinter as tk
from test import *

cicloT = None
tiempoET = None
pCT = None
registrosT = None


def enviar_dato(valorSel):
    global cicloT, tiempoET, pCT, registrosT

    if valorSel == "Uniciclo":

        cicloT.config(text=f"El resultado es: {uniciclo(valorSel)}")


def agregar_componentes_datos(frame):
    global cicloT, tiempoET, pCT, registrosT
    etiqueta_datos = tk.Label(frame, text="Análisis de datos", font=(
        "Arial", 18, "bold"), bg="lightblue")
    etiqueta_datos.pack(padx=10, pady=10)

    ciclos = tk.Label(frame, text="Ciclo de Ejecución", font=(
        "Arial", 18, "bold"), bg="lightblue")
    ciclos.pack(padx=10, pady=10)

    cicloT = tk.Label(frame, text="resultado")
    cicloT.pack()

    tiempoE = tk.Label(frame, text="Tiempo de Ejecución", font=(
        "Arial", 18, "bold"), bg="lightblue")
    tiempoE.pack(padx=10, pady=10)

    tiempoET = tk.Label(frame, text="resultado")
    tiempoET.pack()

    pC = tk.Label(frame, text="Valor de PC", font=(
        "Arial", 18, "bold"), bg="lightblue")
    pC.pack(padx=10, pady=10)

    pCT = tk.Label(frame, text="resultado")
    pCT.pack()

    registros = tk.Label(frame, text="Valor de Registros", font=(
        "Arial", 18, "bold"), bg="lightblue")
    registros.pack(padx=10, pady=10)

    registrosT = tk.Label(frame, text="resultado")
    registrosT.pack()
