# ¿Qué tipo de condición te resultó más intuitiva?
La más intuitiva me pareció el bloque if y elif, si es ésto hago x de lo contrario hago z


# ¿En qué caso usarías condicionales anidadas en un programa real?



En un sistemna basado en roles, usuario, password, rol, etc.



Ejemplo

user = input("Usuario: ")
passw = input("Contraseña: ")

# Primero validamos las credenciales
if user == "admin" and passw == "1234":
    # Solo si entró correctamente, revisamos su rol
    rol = input("Ingresa tu rol (arquitecto / desarrollador): ")
    if rol == "arquitecto":
        print("Acceso completo al sistema")
    elif rol == "desarrollador":
        print("Acceso limitado a sistema")
    else:
        print("Rol no autorizado")
else:
    print("Usuario o contraseña incorrectos")



GitHub: https://github.com/NovoGH/PythonTrainee