# w = arriba,  s = abajo, d = derecha, a = izquierda

def matriz (matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=' ')
        print()
    print("-----------------")

letra = 'o'
pared = '*'
jugador = 'x'


fila = 0
columna = 0

tablero = [[letra]*5 for _ in range(5)]
tablero[0][0] ='I'
tablero[4][4] ='F'

#Paredes
paredes = [
    (0, 2, pared),
    (0, 4, pared),
    (1, 2, pared),
    (3, 1, pared),
    (4, 2, pared),
    (1, 3, pared),
    (2, 4, pared),
    (1, 0, pared),
    (2, 3, pared),
    (3, 0, pared)
]

for pared in paredes:
    tablero[pared[0]][pared[1]] = pared[2]
    
    
# Imprimir la matriz
matriz(tablero)

# Posición de destino
destino = [4, 4]

while [columna, fila] != destino:
    movimiento = input("Ingrese hacia dónde avanzar: ")
    proxima_posicion = [columna, fila]

    if movimiento == 'd':
        if proxima_posicion[1] + 1 >= len(tablero[0]):
            print("¡Te has chocado con el bordes!")
            break
        proxima_posicion[1] += 1 
    elif movimiento == 'a':
        if proxima_posicion[1] - 1 < 0:
            print("¡Te has chocado con el bordes!")
            break
        proxima_posicion[1] -= 1 
    elif movimiento == 'w':
        if proxima_posicion[0] - 1 < 0:
            print("¡Te has chocado con el bordes!")
            break
        proxima_posicion[0] -= 1
    elif movimiento == 's':
        if proxima_posicion[0] + 1 >= len(tablero):
            print("¡Te has chocado con el bordes!")
            break
        proxima_posicion[0] += 1

    if tuple(proxima_posicion) in [(pared[0], pared[1]) for pared in paredes]:
        print("¡Te has chocado con una pared!")
        break

    tablero[columna][fila] = letra
    columna, fila = proxima_posicion
    tablero[columna][fila] = jugador
    matriz(tablero)

if [columna, fila] == destino:
    print("¡Felicidades, has llegado a la meta!")
else:
    print("¡Game over!")