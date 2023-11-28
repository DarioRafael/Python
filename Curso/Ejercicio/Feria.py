hijoDueño = input("¿Eres el dueño del hijo?: y/n ")

if hijoDueño == 'y':
    print("Puedes entrar")
else:
    edad = int(input("¿Cuál es tu edad?: "))

    if edad >= 18:
        print("Puedes entrar")
    else:
        print("No puedes entrar")






