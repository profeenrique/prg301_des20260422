# P1: pedir el dinero disponible
dinero = input("¿Cuánto dinero tienes? ")

# P2: convertir el dato a número entero
dinero = int(dinero)

# P3: evaluar cuánto puede comprar y mostrar el resultado
if dinero < 2000:
    print("Solo te alcanza para un dulce")
elif dinero <= 5000:
    print("Puedes comprar un completo")
else:
    print("Menú completo")