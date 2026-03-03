import sys
subtotal = float(input("Introduce el subtotal de la compra: "))
tipo_de_cliente = input("¿Qué tipo de cliente eres, regular o VIP?: ").strip().lower()
if subtotal < 0:
    print("Error: El subtotal no puede ser negativo.")
    sys.exit(0)
if tipo_de_cliente not in ["regular", "vip"]:
    print("Error: El tipo de cliente debe ser 'regular' o 'VIP'.")
    sys.exit(0)
if tipo_de_cliente == "regular" and subtotal >= 100:
    descuento = subtotal * 0.05
if tipo_de_cliente == "regular" and subtotal < 100:
    descuento = 0
elif tipo_de_cliente == "vip":
    descuento = subtotal * 0.15
total = subtotal - descuento
print(f"El subtotal de la compra es: ${subtotal:.2f}\n El porcentaje de descuento aplicado es: {descuento/subtotal*100:.2f}%\n El descuento aplicado es: ${descuento:.2f}\n El total a pagar es: ${total:.2f}")