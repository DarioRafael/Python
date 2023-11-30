import random
alumnos = ["Juan", "Maria", "Pedro", "Ana", "Luis"]

for alumno in alumnos:
    calificaciones = random.randint(5, 10)
    print(f"Nombre: {alumno} Calificacion: {calificaciones}")

print("//////////////////////////////")
for numero in range(1, 101):
    print(numero, end=" ")
