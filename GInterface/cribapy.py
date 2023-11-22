

x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31 = range(32)
memoria = [0] * 1024

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