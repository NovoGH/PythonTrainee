def calcular_promedio(lista_notas):
    if not lista_notas:
        return 0  # Si la lista está vacía, devuelve 0.
    
    for x in lista_notas:
        suma = sum(lista_notas)
        promedio = suma / len(lista_notas)
        registrar_estudiante("Pablo", promedio, "Java", True)
    #return promedio

    #return promedio


def registrar_estudiante(nombreEstudiante, promedio, asignatura, aprobado_con):
    estudiante = {
        "nombre": nombreEstudiante,
        "asignatura": asignatura,
        "aprobado_con": aprobado_con
    }
    #promedio = calcular_promedio([6, 5, 7, 4, 5, 6])
    estudiante["promedio"] = promedio
    listaEstudiantes = []
    listaEstudiantes.append(estudiante)
    return estudiante


# Ejemplo de uso: 
                          

promedio = calcular_promedio([1, 2, 3, 4, 5])
print(f"El promedio es: {promedio}")



'''
EJERCICIO: Registro de Notas de Estudiantes con Promedio

CONTEXTO
Eres profesor y necesitas crear DOS funciones:
    1. Una que calcule el promedio de varias notas 
    2. Otra que registre al estudiante con sus notas y promedio 

PARTE 1: CREAR LA FUNCIÓN DE PROMEDIO
Crea una función llamada calcular_promedio() que:
Parámetros:
    • notas (lista) - Lista con las notas del estudiante 
Lo que debe hacer:
    • Sumar todas las notas de la lista 
    • Dividir entre la cantidad de notas 
    • RETORNAR el promedio (usar return) 
Pista:
    • Para sumar una lista: sum(notas) 
    • Para contar elementos: len(notas) 

PARTE 2: CREAR LA FUNCIÓN DE REGISTRO
Crea una función llamada registrar_estudiante() que tenga los siguientes parámetros:
Parámetros OBLIGATORIOS:
    1. nombre (string) - Nombre del estudiante 
    2. notas (lista) - Lista con las notas obtenidas (ej: [6.5, 7.0, 5.8]) 
Parámetros OPCIONALES (con valores por defecto):
    3. asignatura (string) - Nombre de la materia. Por defecto: "Python Trainee" 
    4. aprobado_con (float) - Nota mínima para aprobar. Por defecto: 4.0 
Lo que debe hacer la función:
    1. Llamar a la función calcular_promedio() pasándole las notas 
    2. Determinar si el estudiante aprobó (promedio >= aprobado_con) 
    3. Imprimir: 
        ◦ Línea de separación 
        ◦ Nombre del estudiante 
        ◦ Asignatura 
        ◦ Todas las notas (una por línea) 
        ◦ El promedio calculado 
        ◦ Si aprobó o reprobó 
        ◦ Línea de separación 
Ejemplo de salida esperada:
========================================
Estudiante: Juan Pérez
Asignatura: Python Trainee
Notas:
  - 6.5
  - 7.0
  - 5.8
Promedio: 6.43
Estado: APROBADO
========================================
Pistas:
    • Usa un bucle for para mostrar cada nota 
    • Para determinar aprobado/reprobado: if promedio >= aprobado_con: 
    • Para redondear el promedio: round(promedio, 2) 

PARTE 3: PROBAR LAS FUNCIONES
Prueba tus funciones con estos 4 casos:

CASO 1: Estudiante Aprobado Simple
Registra un estudiante que aprobó usando valores por defecto.
Datos:
    • Nombre: "Ana Torres" 
    • Notas: [6.5, 7.0, 6.8] 
    • (Usar asignatura y nota de aprobación por defecto) 
Resultado esperado:
    • Promedio: 6.77 
    • Estado: APROBADO 

CASO 2: Estudiante Reprobado
Registra un estudiante con notas bajas.
Datos:
    • Nombre: "Carlos Ruiz" 
    • Notas: [3.5, 4.2, 3.8, 3.0] 
    • (Usar valores por defecto) 
Resultado esperado:
    • Promedio: 3.63 
    • Estado: REPROBADO 

CASO 3: Asignatura Diferente
Registra un estudiante en una asignatura diferente.
Datos:
    • Nombre: "María López" 
    • Notas: [5.5, 6.0, 5.8, 6.2] 
    • Asignatura: "JavaScript Trainee" 
    • (Mantener nota de aprobación por defecto: 4.0) 
Resultado esperado:
    • Asignatura: JavaScript Trainee 
    • Promedio: 5.88 
    • Estado: APROBADO 

CASO 4: Curso Avanzado (nota de aprobación más alta)
Registra un estudiante en un curso donde se necesita nota 5.0 para aprobar.
Datos:
    • Nombre: "Luis Morales" 
    • Notas: [4.5, 4.8, 4.6] 
    • Asignatura: "Full Stack Python" 
    • Nota mínima para aprobar: 5.0 
Resultado esperado:
    • Promedio: 4.63 
    • Estado: REPROBADO (porque el promedio es menor a 5.0) 
Desafío: ¿Cómo pasas aprobado_con=5.0 sin cambiar el orden de los parámetros?

CRITERIOS DE EVALUACIÓN
Tu ejercicio está completo cuando:
La función calcular_promedio() retorna correctamente el promedio
La función registrar_estudiante() está definida con todos sus parámetros
Los parámetros opcionales tienen valores por defecto
La función llama correctamente a calcular_promedio()
Muestra todas las notas, el promedio y el estado
Los 4 casos de prueba funcionan correctamente

PREGUNTAS DE REFLEXIÓN
    1. ¿Por qué necesitamos usar return en la función calcular_promedio()? 
    2. ¿Cómo puedes cambiar solo el parámetro aprobado_con sin cambiar asignatura? 
    3. ¿Qué ventaja tiene separar el cálculo del promedio en su propia función? 
    4. ¿Podrías agregar más notas a la lista sin modificar la función?
'''
