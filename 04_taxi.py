import sys
distancia = float(input("Introduce la distancia recorrida en kilómetros en el taxi: "))
if distancia < 0:
    print("Error: La distancia no puede ser negativa.")
    sys.exit(0)
elif distancia <10:
    recargo_fijo = 0
else:
    recargo_fijo = 2
hora = int(input("Introduce solo la hora en la que empezó el viaje (un número entre 0-23): "))
if hora not in range(0, 24):
    print("Error: La hora debe ser un número entre 0 y 23.")
    sys.exit(0)
if hora >= 6 and hora <= 19:
    costo_por_km = 0.5
    horario = "diurno"
elif hora >= 20 and hora <= 23 or hora >= 0 and hora <= 5:
    costo_por_km = 0.65
    horario = "nocturno"
costo_total = recargo_fijo + (costo_por_km * distancia)
print(f"Horario del viaje: {horario}\n Distancia recorrida: {distancia:.2f} km\n Total a pagar: ${costo_total:.2f}")

