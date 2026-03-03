#------------------------------------------------------------
#EJERCICIO 2 — par o impar + mayoría de edad
#------------------------------------------------------------
import sys
import time
try:
    numero = int(input("Introduce un número entero positivo: "))
    if numero < 0:
        print("Error: El número debe ser positivo.")
        sys.exit(0)
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
        
except ValueError:
    print("Error: Eso no es un número. Por favor, ingresa solo dígitos.")
    sys.exit(0)

time.sleep(1.5)
try:
    edad = int(input("Introduce tu edad (solo el número): "))
    if edad < 0 or edad > 110:
        print("Error: Por favor, introduce una edad válida (entre 0 y 110).")
    elif edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
        
except ValueError:
    print("Error: La edad debe ser un número entero.")