import tkinter as tk


def agregar_componentes_seleccion(frame):
    etiqueta_seleccion = tk.Label(frame, text="Ventana de selección")
    etiqueta_seleccion.pack(padx=10, pady=10)
    # Aquí puedes agregar selects, botones u otros componentes para la selección
    opciones = ["Procesador", "Uniciclo", "Multiciclo", "Segmentado Riesgos->Stalls",
                "Segmentado -> Unidad de Riesgos y levantamiento "]  # Lista de opciones
    seleccion = tk.StringVar()  # Variable para almacenar la opción seleccionada
    seleccion.set(opciones[0])

    select = tk.OptionMenu(frame, seleccion, *opciones)
    select.pack(padx=10, pady=10)

    boton_llamar = tk.Button(
        frame, text="Iniciar", command=lambda: test(seleccion.get()))

    boton_llamar.pack(padx=10, pady=10)
