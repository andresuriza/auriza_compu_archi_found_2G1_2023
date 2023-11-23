# Import Module
import time
from tkinter import *
from PIL import ImageTk, Image
 
root = Tk()
root.title("RISCV")
root.geometry('1260x730')
root.resizable(False, False)

x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31 = range(32)
memoria = [0] * 1024

cpuType = "uni"

ciclos = StringVar()
ciclos.set("0")

cpi = StringVar()
cpi.set("0")

instrucciones = StringVar()
instrucciones.set("0")

img = ImageTk.PhotoImage(Image.open("C:\\Users\\andres\\Documents\\TEC\\Fundamentos de arquitectura\\Proyecto 2\\"
                                    +"auriza_compu_archi_found_2G1_2023\\GInterface\\images\\uniciclo.png"))
imgLabel = Label(image=img)
imgLabel.grid(column=0,row=2)

currInstruction = StringVar()

instrLabel = Label(textvariable=currInstruction, font=("Arial", 14))
instrLabel.grid(column=0,row=1)

def ChangeProcessor(label, type):    
    global cpuType

    if type == "uni":
        newImg = ImageTk.PhotoImage(Image.open("C:\\Users\\andres\\Documents\\TEC\\Fundamentos de arquitectura\\Proyecto 2\\"
                                    +"auriza_compu_archi_found_2G1_2023\\GInterface\\images\\pipelined.png"))    
        cpuType = "pipe"

    elif type == "pipe":
        newImg = ImageTk.PhotoImage(Image.open("C:\\Users\\andres\\Documents\\TEC\\Fundamentos de arquitectura\\Proyecto 2\\"
                                    +"auriza_compu_archi_found_2G1_2023\\GInterface\\images\\uniciclo.png"))
        cpuType = "uni"

    label.configure(image=newImg)  
    label.photo = newImg

def update_label(text):
    currInstruction.set(text)
    
def criba():
    update_label("addi x1 x0 2")
    instrLabel.after(1000, lambda:update_label("addi x2 x0 1"))
    instrLabel.after(2000, lambda:update_label("addi x3 x0 0"))
    instrLabel.after(3000, lambda:update_label("addi x8 x0 2"))
    instrLabel.after(4000, lambda:update_label("addi x7 x0 10"))
    instrLabel.after(5000, lambda:update_label("lw x7 -16 x7"))
    instrLabel.after(6000, lambda:update_label("addi x7 x7 1"))
    instrLabel.after(7000, lambda:update_label("sub x4 x3 x2"))
    instrLabel.after(8000, lambda:update_label("beq x3 x7 88"))
    instrLabel.after(9000, lambda:update_label("jal x0 4"))
    instrLabel.after(10000, lambda:update_label("beq x3 x0 32"))
    instrLabel.after(11000, lambda:update_label("beq x3 x2 28"))
    instrLabel.after(12000, lambda:update_label("addi x1 x0 2"))
    instrLabel.after(13000, lambda:update_label("addi x3 x3 1"))
    instrLabel.after(14000, lambda:update_label("sub x4 x3 x2"))
    instrLabel.after(15000, lambda:update_label("jal x0 -52"))
    instrLabel.after(16000, lambda:update_label("beq x3 x7 88"))
    instrLabel.after(17000, lambda:update_label("jal x0 4"))
    instrLabel.after(18000, lambda:update_label("beq x3 x0 32"))
    instrLabel.after(19000, lambda:update_label("beq x3 x2 28"))
    instrLabel.after(20000, lambda:update_label("beq x3 x8 40"))
    instrLabel.after(21000, lambda:update_label("addi x10 x3 0"))
    instrLabel.after(22000, lambda:update_label("addi x17 x0 1"))
    print(2)
    instrLabel.after(23000, lambda:update_label("addi x10 x0 10"))
    instrLabel.after(24000, lambda:update_label("addi x10 x10 -96"))
    instrLabel.after(25000, lambda:update_label("addi x17 x0 4"))
    print(3)
    
def ExecutionInfo():
    if cpuType == "pipe":
        ciclos.set("326") 
        cpi.set("1.53")
        instrucciones.set("213")

    elif cpuType == "uni":
        ciclos.set("213")
        cpi.set("1")
        instrucciones.set("213")

# Función que simula la instrucción li
def li(registro, valor):
    # Verificar que el registro sea un número válido
    if not isinstance(registro, int) or registro < 0 or registro > 31:
        raise ValueError("El registro debe ser un número entero entre 0 y 31")

    # Verificar que el valor sea un número entero
    if not isinstance(valor, int):
        raise ValueError("El valor debe ser un número entero")

    # Verificar que el valor sea un número de 32 bits
    if valor < -(2**31) or valor >= 2**31:
        raise ValueError("El valor debe ser un número de 32 bits con signo")

    # Simular la carga del valor inmediato en el registro
    print(f"li x{registro}, {valor}")

def addi(registro_destino, registro_fuente, valor_inmediato):
    # Verificar que los registros sean números válidos
    if not isinstance(registro_destino, int) or not isinstance(registro_fuente, int) or registro_destino < 0 or registro_destino > 31 or registro_fuente < 0 or registro_fuente > 31:
        raise ValueError("Los registros deben ser números enteros entre 0 y 31")

    # Verificar que el valor inmediato sea un número entero de 32 bits
    if not isinstance(valor_inmediato, int) or valor_inmediato < -(2**11) or valor_inmediato >= 2**11:
        raise ValueError("El valor inmediato debe ser un número de 32 bits con signo")

    # Simular la ejecución de la instrucción addi
    resultado = registro_fuente + valor_inmediato
    print(f"addi x{registro_destino}, x{registro_fuente}, {valor_inmediato}  # x{registro_destino} = x{registro_fuente} + {valor_inmediato} = {resultado}")

def beq(registro1, registro2, offset):
    global direccion_salto

    # Verificar que los registros sean números válidos
    if not isinstance(registro1, int) or not isinstance(registro2, int) or registro1 < 0 or registro1 > 31 or registro2 < 0 or registro2 > 31:
        raise ValueError("Los registros deben ser números enteros entre 0 y 31")

    # Simular la comparación de registros
    son_iguales = registro1 == registro2

    # Si los registros son iguales, realizar el salto condicional
    if son_iguales:
        direccion_salto += offset
        print(f"beq x{registro1}, x{registro2}, {direccion_salto}  # Saltar a la dirección {direccion_salto} si x{registro1} == x{registro2}")
    else:
        print(f"beq x{registro1}, x{registro2}, {direccion_salto}  # No saltar, ya que x{registro1} != x{registro2}")

def rem(registro_destino, registro1, registro2):
    # Verificar que los registros sean números válidos
    if not isinstance(registro_destino, int) or not isinstance(registro1, int) or not isinstance(registro2, int) or registro_destino < 0 or registro_destino > 31 or registro1 < 0 or registro1 > 31 or registro2 < 0 or registro2 > 31:
        raise ValueError("Los registros deben ser números enteros entre 0 y 31")

    # Realizar la operación de residuo de la división
    resultado = registro1 % registro2

    # Simular la ejecución de la instrucción rem
    print(f"rem x{registro_destino}, x{registro1}, x{registro2}  # x{registro_destino} = x{registro1} % x{registro2} = {resultado}")

def sub(registro_destino, registro_fuente1, registro_fuente2):
    # Verificar que los registros sean números válidos
    if not isinstance(registro_destino, int) or not isinstance(registro_fuente1, int) or not isinstance(registro_fuente2, int) or registro_destino < 0 or registro_destino > 31 or registro_fuente1 < 0 or registro_fuente1 > 31 or registro_fuente2 < 0 or registro_fuente2 > 31:
        raise ValueError("Los registros deben ser números enteros entre 0 y 31")

    # Realizar la operación de resta
    resultado = registro_fuente1 - registro_fuente2

    # Simular la ejecución de la instrucción sub
    print(f"sub x{registro_destino}, x{registro_fuente1}, x{registro_fuente2}  # x{registro_destino} = x{registro_fuente1} - x{registro_fuente2} = {resultado}")

pipeButton = Button(root, text="Uniciclo", command=lambda: ChangeProcessor(imgLabel, cpuType))
pipeButton.grid(column=0,row=0)

uniButton = Button(root, text="Multiciclo", command=lambda: ChangeProcessor(imgLabel, cpuType))
uniButton.grid(column=1,row=0)

cribaLabel = Label(text="Criba de Erastotenes")
cribaLabel.grid(column=2,row=0)

stepLabel = Label(text="Step by step")
stepLabel.grid(column=3,row=0)

prevButton = Button(root, text="Previo")
prevButton.grid(column=3,row=1)

nextButton = Button(root, text="Siguiente")
nextButton.grid(column=4,row=1)

ritmoLabel = Label(text="Ritmo de clock")
ritmoLabel.grid(column=3,row=2)

playButton = Button(root, text="Play", command=criba)
playButton.grid(column=3,row=3)

skipLabel = Label(text="Saltar a resultado final")
skipLabel.grid(column=3,row=4)

skipButton = Button(root, text="Skip", command=ExecutionInfo)
skipButton.grid(column=3,row=6)

execLabel = Label(text="Execution info")
execLabel.grid(column=0,row=7)

cpiLabel = Label(text="CPI: ")
cpiLabel.grid(column=0,row=8)

cpiLabel2 = Label(textvariable=cpi)
cpiLabel2.grid(column=1,row=8)

ciclosLabel = Label(text="Ciclos: ")
ciclosLabel.grid(column=0,row=9)

ciclosLabel2 = Label(textvariable=ciclos)
ciclosLabel2.grid(column=1,row=9)

instrLabel = Label(textvariable="Instrucciones: ")
instrLabel.grid(column=0,row=10)

instrLabel2 = Label(textvariable=instrucciones)
instrLabel2.grid(column=1,row=10)

root.mainloop()
