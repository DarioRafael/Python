numero_objetivo = int(input("Ingrese un número de al menos 5 dígitos: "))



while numero_objetivo < 10:  #Para cambiar digitos
    print("El número ingresado no tiene al menos 5 dígitos.")
    numero_objetivo = int(input("Ingrese un número de al menos 5 dígitos: "))

intentos = 0
numero_actual = 0       # Sí ya sabemos cuántos digitos tiene, podemos agregar que empiece ejemplo: 10000  porqué tendra 5 digitos o más.

while numero_actual != numero_objetivo:
    print(numero_actual)
    intentos += 1
    numero_actual += 1

print(f"Se encontró el número {numero_objetivo} después de {intentos} intentos.")


