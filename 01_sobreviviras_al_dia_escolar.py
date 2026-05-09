# P1: pedir la cantidad de horas dormidas
horas = input("¿Cuántas horas dormiste? ")

# P2: convertir el dato a número entero
horas = int(horas)

# P3: evaluar las horas de sueño y mostrar el resultado
if horas < 5:
    print("Modo zombie")
elif horas <= 7:
    print("Funcionando")
else:
    print("Full energía")