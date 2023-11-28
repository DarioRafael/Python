import random
numeroUsuario = int(input("Ingrese un numero: "))
numeroRandom = random.randint(1, 100)

while numeroUsuario != numeroRandom:
    if numeroUsuario > numeroRandom:
        print("El numero es menor")
    else:
        print("El numero es mayor")
    numeroUsuario = int(input("Ingrese un numero: "))


print("¡Lo lograste!")
