def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.
    El ciclo de vida de la función termina cuando retorna el promedio.
    """
    if not notas:
        return 0  # Evita división por cero si la lista viene vacía

    promedio = sum(notas) / len(notas)
    return promedio

def registrar_estudiante(nombre,notas,asignatura="Python Trainee",aprobado_con=4.0
):
    """
    Registra un estudiante, calcula su promedio y muestra su estado.
    Usa calcular_promedio() y parámetros opcionales con valores por defecto.
    """
    promedio = calcular_promedio(notas)
    promedio_redondeado = round(promedio, 2)

    if promedio >= aprobado_con:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    print("========================================")
    print(f"Estudiante: {nombre}")
    print(f"Asignatura: {asignatura}")
    print("Notas:")
    for nota in notas:
        print(f"  - {nota}")
    print(f"Promedio: {promedio_redondeado}")
    print(f"Estado: {estado}")
    print("========================================\n")


    # CASO 1: Estudiante Aprobado Simple
registrar_estudiante(
    nombre="Ana María",
    notas=[6.5, 7.0, 6.8]
)
# Promedio esperado: 6.77 (aprox)

# CASO 2: Estudiante Reprobado
registrar_estudiante(
    nombre="Sebastián Lopez",
    notas=[3.5, 4.2, 3.8, 3.0]
)
# Promedio esperado: 3.63 (aprox)

# CASO 3: Asignatura Diferente
registrar_estudiante(
    nombre="Claudio Perez",
    notas=[5.5, 6.0, 5.8, 6.2],
    asignatura="JavaScript Trainee"
)
# Promedio esperado: 5.88 (aprox)

# CASO 4: Curso Avanzado (nota de aprobación 5.0)
registrar_estudiante(
    nombre="Felix Martinez",
    notas=[4.5, 4.8, 4.6],
    asignatura="Full Stack Python",
    aprobado_con=5.0      # ← aquí usamos argumento nombrado
)
# Promedio esperado: 4.63 (aprox) y REPROBADO