def calcular_importe_final(importe):
    """Devuelve el importe final aplicando el descuento correspondiente."""
    if importe > 800:
        descuento = 0.12
    elif importe > 500:
        descuento = 0.10
    elif importe > 300:
        descuento = 0.05
    else:
        descuento = 0.0
    return importe * (1 - descuento)

importe = float(input("Ingrese el importe de la compra (€): "))
final = calcular_importe_final(importe)
print(f"El importe final a pagar" f" es: €{final:.2f}")
