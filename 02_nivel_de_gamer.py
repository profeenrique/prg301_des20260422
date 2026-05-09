# P1: pedir el puntaje del jugador
puntaje = input("Ingresa tu puntaje: ")

# P2: convertir el dato a número entero
puntaje = int(puntaje)

# P3: evaluar el puntaje y mostrar el nivel
if puntaje < 1000:
    print("Jugador novato")
elif puntaje <= 3000:
    print("Jugador pro")
else:
    print("Leyenda")