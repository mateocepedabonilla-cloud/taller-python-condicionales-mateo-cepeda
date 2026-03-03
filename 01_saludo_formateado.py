while True:
    nombre = input("¿Cuál es tu nombre? ").capitalize()
    if nombre.isdigit():
        print("Error: El nombre no puede ser un número. Por favor, ingresa un nombre válido.")
    elif not nombre:
        print("El nombre no puede estar vacío. Por favor, ingresa un nombre válido.")
    else:
        break
while True:
    try:
        edad = int(input("¿Cuál es tu edad? "))
        if edad > 0:
            break
        else:
           print("Por favor, ingresa una edad válida (mayor a 0).")
    except ValueError:
        print("Por favor, introduce un número válido para la edad.")
while True:
    ciudad = input("¿En qué ciudad vives? ").capitalize().strip()
    if not ciudad:
        print("La ciudad no puede estar vacía.")
    elif ciudad.isdigit():
        print("Error: La ciudad no puede ser un número.")
    else:
        break

print(f"Hola, {nombre}, tienes {edad} años y vives en {ciudad}.")