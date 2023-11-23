from tkinter import Tk, Canvas
from PIL import Image, ImageTk
from dataSection import *


def agregar_componentes_visualizacion(frame):
    global imagePath
    # Abrir la imagen con Pillow
    imagen_pillow = Image.open(imagePath)  # Reemplaza con la ruta de tu imagen

    # Redimensionar la imagen según sea necesario
    ancho_canvas = 750  # ajusta según tus necesidades
    alto_canvas = 470  # ajusta según tus necesidades
    imagen_redimensionada = imagen_pillow.resize(
        (ancho_canvas, alto_canvas), Image.ANTIALIAS)

    # Convertir la imagen redimensionada a un formato compatible con Tkinter
    frame.imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

    # Crear un widget Canvas para mostrar la imagen
    frame.canvas = Canvas(frame, width=ancho_canvas, height=alto_canvas)
    frame.canvas.pack()

    # Mostrar la imagen en el Canvas
    frame.canvas.create_image(0, 0, anchor="nw", image=frame.imagen_tk)
