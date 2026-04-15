
def validar_acceso(edad, tiene_entrada, esta_en_lista_vip):
    """
    Devuelve True si la persona puede entrar al club, False en caso contrario.
    Requisitos:
    - Edad mayor o igual a 18
    - Y además tener entrada comprada O estar en la lista VIP
    """
    es_mayor_de_edad = edad >= 18
    cumple_condicion_extra = tiene_entrada or esta_en_lista_vip

    return es_mayor_de_edad and cumple_condicion_extra


# Ejemplos de uso
edad = int(input("Edad: "))
entrada = input("¿Tiene entrada comprada? (s/n): ").lower() == "s"
vip = input("¿Está en la lista VIP? (s/n): ").lower() == "s"

if validar_acceso(edad, entrada, vip):
    print("Acceso permitido")
else:
    print("Acceso denegado")