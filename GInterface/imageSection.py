import tkinter as tk


def agregar_componentes_visualizacion(frame):
    etiqueta_visualizacion = tk.Label(
        frame, text="Ventana de visualización de imágenes")
    etiqueta_visualizacion.pack(padx=10, pady=10)
    # Cambia "ruta_de_la_imagen.jpg" por el nombre de tu archivo
    # Ruta de la imagen que deseas cargar
    # imagen = tk.PhotoImage(file="images/adelt.PNG")
    # label_imagen = tk.Label(frame, image=imagen)
    # label_imagen.pack()
