
def incrementar_palabra(palabra):
    palabra = list(palabra)
    i = len(palabra) - 1
    while i >= 0:
        if palabra[i] != 'z':
            palabra[i] = chr(ord(palabra[i]) + 1)
            return ''.join(palabra)
        else:
            palabra[i] = 'a'
            i -= 1
    return 'a' + ''.join(palabra)

palabra_objetivo = input("Ingrese una palabra: ")

while len(palabra_objetivo) < 1:
    print("La palabra ingresada no tiene al menos una letra.")
    palabra_objetivo = input("Ingrese una palabra: ")

intentos = 0
palabra_actual = "a"

while palabra_actual != palabra_objetivo:
    print(palabra_actual)
    intentos += 1
    palabra_actual = incrementar_palabra(palabra_actual)

print(f"Se encontró la palabra '{palabra_objetivo}' después de {intentos} intentos.")