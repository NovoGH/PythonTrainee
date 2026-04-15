def realizar_compra(
    productos,
    producto_2="Queso",
    producto_3=None,
    forma_pago=None
):
   
    if forma_pago is None:
        print("Debes indicar la forma de pago.")
        return

    print("=== Realizar compra ===")
    print(f"Productos base: {productos}")

    print(f"Producto 1: {productos[0]}")
    print(f"Producto 2: {productos[1] if len(productos) > 1 else producto_2}")

    if producto_3 is not None:
        print(f"Producto 3: {producto_3}")
    else:
        print("Producto 3: (no seleccionado)")

    print(f"Forma de pago: {forma_pago}")
    print("Compra registrada.\n")

# 1) Solo lista y forma de pago (usa todos los valores por defecto)
realizar_compra(["leche", "pan"], forma_pago="efectivo")

# 2) Cambiando producto_1 y forma de pago
realizar_compra(["arroz"], "arroz integral", forma_pago="tarjeta")

# 3) Especificando 3 productos y forma de pago
realizar_compra(
    ["café", "filtro"],
    
    producto_3="azúcar",
    forma_pago="transferencia"
)

# 4) Cambiando solo producto_3 por nombre y la forma de pago
realizar_compra(
    ["frutas"],
    producto_3="plátanos",
    forma_pago="débito"
)