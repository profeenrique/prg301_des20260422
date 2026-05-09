# P1: pedir la nota final
nota = input("Ingresa tu nota: ")

# P2: convertir el dato a número decimal
nota = float(nota)

# P3: evaluar la nota y mostrar el resultado
if nota == 7.0:
    print("¡Perfecto!")
elif nota < 4.0:
    print("Reprobaste")
elif nota < 6.0:
    print("Aprobaste")
else:
    print("¡Seca!")