# Pedir al usuario que ingrese un número de al menos 5 dígitos
numero_objetivo = int(input("Ingrese un número de al menos 5 dígitos: "))

# Verificar que el número tiene al menos 5 dígitos
while numero_objetivo < 10000:
    print("El número ingresado no tiene al menos 5 dígitos.")
    numero_objetivo = int(input("Ingrese un número de al menos 5 dígitos: "))

# Inicializar variables
intentos = 0
numero_actual = 10000

# Bucle while para buscar el número objetivo
while numero_actual != numero_objetivo:
    print(numero_actual)
    intentos += 1
    numero_actual += 1

# Imprimir el resultado
print(f"Se encontró el número {numero_objetivo} después de {intentos} intentos.")
