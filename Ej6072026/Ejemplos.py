"""
    Clasifica una nota numérica (0-100) en letra y descripción.
    A: 90 - 100 Excelente
    B: 80 - 89  Buena
    C: 70 - 79  Aceptado
    D: 60 - 69  Aprobado
    E: 0 - 59   Reprobado
"""

"""
def clasificar_nota(nota):

    if 90 <= nota <= 100:
        return "A", "Excelente"
    elif 80 <= nota <= 89:
        return "B", "Buena"
    elif 70 <= nota <= 79:
        return "C", "Aceptado"
    elif 60 <= nota <= 69:
        return "D", "Aprobado"
    else:
        return "E", "Reprobado"
"""

def clasificar_nota(nota):
    
    decena = int(nota) // 10

    match decena:
        case 10 | 9:
            return "A", "Excelente"
        case 8:
            return "B", "Buena"
        case 7:
            return "C", "Aceptado"
        case 6:
            return "D", "Aprobado"
        case _:
            return "E", "Reprobado"
    
"""Pide una nota entre 0 y 100 y valida el rango."""

def pedir_nota():
    while True:
        try:
            nota = float(input("Ingrese la nota (0 a 100): "))
            if 0 <= nota <= 100:
                return nota
            else:
                print("La nota debe estar entre 0 y 100. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido.")

nota = pedir_nota()
print()
nota = clasificar_nota(nota)
print("Nota clasificada: ", nota)