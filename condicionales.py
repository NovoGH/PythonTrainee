# 1. Decisión simple
# Pedir un número entre 1 y 12


#edad = int(input("Por favor, ingresa un edad y presiona Enter: "))

"""

if edad >=18:
    print("Eres mayor de edad")
elif edad <18:
    print("Eres menor de edad")


# 2. Decisión múltiple con elif
# Solicita al usuario una calificación (entre 1 y 7) e imprime el resultado evaluativo:
"""


"""

calificacion = int(input("Por favor, ingresa calificación entre 1 y 7, y presiona Enter: "))


while calificacion < 1 or calificacion > 7:
    print("Solo se aceptan calificaciones entre 1 y 7.")
    calificacion = int(input("Ingresa nuevamente un calificación (1 a 7): "))



if calificacion == 7:
    print("Excelente")

elif calificacion == 6:
    print("Muy bien")

elif calificacion == 5:
    print("Bien")

elif calificacion == 4:
    print("Suficiewnte")

elif calificacion < 4 and calificacion > 0:
    print("Insufciciente")

 """


# 3. Condiciones anidadas
# Solicita un número entero.


"""
numero_entero = int(input("Por favor, ingresar un númewro entero, y presiona Enter: "))

if numero_entero > 0:
    print("El número es positivo")

elif numero_entero == 0:
    print("El número es cero")

else:
    print("El número es negativo")
"""


# 4. Condición de borde
# Solicita al usuario un número entre 1 y 100.


"""
numero_usuario = int(input("Ingrese un número entre 1 y 100: "))

# Verificar si está exactamente en los límites 1 o 100
if numero_usuario == 1 or numero_usuario == 100:
    print("Estás en un límite permitido")

# Verificar si está dentro del rango pero no en los extremos
elif 1 < numero_usuario < 100:
    print("Dentro del rango")

# Cualquier otro caso se considera fuera del rango
else:
    print("Fuera del rango")
"""



