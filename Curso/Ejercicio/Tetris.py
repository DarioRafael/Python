import pygame
import random

pygame.init()

# Definición de variables
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Formas de las piezas
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [1]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1]],
]

# Clase para representar una pieza
class Piece:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*reversed(self.shape)))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen,
                        self.color,
                        (GRID_SIZE * (self.x + j), GRID_SIZE * (self.y + i), GRID_SIZE, GRID_SIZE),
                    )

# Función para verificar colisiones
def check_collision(piece, dx=0, dy=0):
    for i, row in enumerate(piece.shape):
        for j, cell in enumerate(row):
            if (
                cell
                and (
                    piece.x + j + dx < 0
                    or piece.x + j + dx >= GRID_WIDTH
                    or piece.y + i + dy >= GRID_HEIGHT
                    or (piece.y + i + dy >= 0 and grid[piece.y + i + dy][piece.x + j + dx] is not None)
                )
            ):
                return True
    return False

# Función para eliminar filas completas
def clear_lines():
    full_rows = [i for i, row in enumerate(grid) if all(cell is not None for cell in row)]
    for row in full_rows:
        del grid[row]
        grid.insert(0, [None] * GRID_WIDTH)

# Inicialización de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Inicialización del juego
clock = pygame.time.Clock()
fall_time = 0
fall_speed = 1

current_piece = Piece(random.choice(SHAPES), random.choice([RED, CYAN, MAGENTA, YELLOW, GREEN, BLUE, ORANGE]))
next_piece = Piece(random.choice(SHAPES), random.choice([RED, CYAN, MAGENTA, YELLOW, GREEN, BLUE, ORANGE]))

grid = [[None] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Bucle principal del juego
running = True
clock = pygame.time.Clock()
fall_time = 0

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not check_collision(current_piece, dx=-1):
                current_piece.move(-1, 0)
            elif event.key == pygame.K_RIGHT and not check_collision(current_piece, dx=1):
                current_piece.move(1, 0)
            elif event.key == pygame.K_DOWN:
                # Permitir que la pieza caiga automáticamente hacia abajo
                while not check_collision(current_piece, dy=1):
                    current_piece.move(0, 1)

            elif event.key == pygame.K_UP and not check_collision(current_piece):
                current_piece.rotate()

    # Movimiento automático hacia abajo
    fall_time += clock.get_rawtime()
    if fall_time > 1000 / fall_speed:
        fall_time = 0
        if not check_collision(current_piece, dy=1):
            current_piece.move(0, 1)
        else:
            # Fijar la pieza actual en el tablero
            for i, row in enumerate(current_piece.shape):
                for j, cell in enumerate(row):
                    if cell:
                        if current_piece.y + i >= 0:
                            grid[current_piece.y + i][current_piece.x + j] = current_piece.color
            # Verificar y eliminar filas completas
            clear_lines()
            # Establecer la nueva pieza actual y la próxima pieza
            current_piece = next_piece
            next_piece = Piece(random.choice(SHAPES), random.choice([RED, CYAN, MAGENTA, YELLOW, GREEN, BLUE, ORANGE]))
            # Verificar si hay colisión con la nueva pieza
            if check_collision(current_piece):
                running = False

    # Dibujar el tablero y las piezas
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, cell, (GRID_SIZE * j, GRID_SIZE * i, GRID_SIZE, GRID_SIZE))

    current_piece.draw()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
