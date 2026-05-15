import pygame
import random

pygame.init()

CELL_SIZE = 30
COLS = 10
ROWS = 20
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
SIDE_PANEL = 180

screen = pygame.display.set_mode((WIDTH + SIDE_PANEL, HEIGHT))
pygame.display.set_caption("Tetris Python + Pygame")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

BLACK = (20, 20, 20)
GRID = (45, 45, 45)
WHITE = (240, 240, 240)

SHAPES = [
    [[1, 1, 1, 1]],

    [[1, 1],
     [1, 1]],

    [[0, 1, 0],
     [1, 1, 1]],

    [[1, 0, 0],
     [1, 1, 1]],

    [[0, 0, 1],
     [1, 1, 1]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1, 0],
     [0, 1, 1]]
]

COLORS = [
    (0, 240, 240),
    (240, 240, 0),
    (160, 0, 240),
    (0, 0, 240),
    (240, 160, 0),
    (0, 240, 0),
    (240, 0, 0)
]


class Piece:
    def __init__(self):
        index = random.randint(0, len(SHAPES) - 1)
        self.shape = SHAPES[index]
        self.color = COLORS[index]
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]


def create_grid():
    return [[None for _ in range(COLS)] for _ in range(ROWS)]


def valid_position(piece, grid, offset_x=0, offset_y=0):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = piece.x + x + offset_x
                new_y = piece.y + y + offset_y

                if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                    return False

                if new_y >= 0 and grid[new_y][new_x] is not None:
                    return False

    return True


def lock_piece(piece, grid):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                grid[piece.y + y][piece.x + x] = piece.color


def clear_lines(grid):
    new_grid = [row for row in grid if any(cell is None for cell in row)]
    cleared = ROWS - len(new_grid)

    for _ in range(cleared):
        new_grid.insert(0, [None for _ in range(COLS)])

    return new_grid, cleared


def draw_grid(grid):
    screen.fill(BLACK)

    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if grid[y][x]:
                pygame.draw.rect(screen, grid[y][x], rect)
                pygame.draw.rect(screen, BLACK, rect, 2)
            else:
                pygame.draw.rect(screen, GRID, rect, 1)


def draw_piece(piece):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                rect = pygame.Rect(
                    (piece.x + x) * CELL_SIZE,
                    (piece.y + y) * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
                pygame.draw.rect(screen, piece.color, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)


def draw_text(score, game_over):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH + 20, 40))

    help_text = [
        "← → move",
        "↓ down",
        "↑ rotate",
        "Space drop"
    ]

    small_font = pygame.font.SysFont("Arial", 18)

    for i, text in enumerate(help_text):
        rendered = small_font.render(text, True, WHITE)
        screen.blit(rendered, (WIDTH + 20, 100 + i * 25))

    if game_over:
        over = font.render("GAME OVER", True, (255, 80, 80))
        screen.blit(over, (WIDTH + 15, 250))


def hard_drop(piece, grid):
    while valid_position(piece, grid, offset_y=1):
        piece.y += 1


def main():
    grid = create_grid()
    current_piece = Piece()

    fall_time = 0
    fall_speed = 500

    score = 0
    running = True
    game_over = False

    while running:
        dt = clock.tick(60)
        fall_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if valid_position(current_piece, grid, offset_x=-1):
                        current_piece.x -= 1

                elif event.key == pygame.K_RIGHT:
                    if valid_position(current_piece, grid, offset_x=1):
                        current_piece.x += 1

                elif event.key == pygame.K_DOWN:
                    if valid_position(current_piece, grid, offset_y=1):
                        current_piece.y += 1

                elif event.key == pygame.K_UP:
                    old_shape = current_piece.shape
                    current_piece.rotate()

                    if not valid_position(current_piece, grid):
                        current_piece.shape = old_shape

                elif event.key == pygame.K_SPACE:
                    hard_drop(current_piece, grid)

        if not game_over and fall_time >= fall_speed:
            fall_time = 0

            if valid_position(current_piece, grid, offset_y=1):
                current_piece.y += 1
            else:
                lock_piece(current_piece, grid)
                grid, cleared = clear_lines(grid)
                score += cleared * 100

                current_piece = Piece()

                if not valid_position(current_piece, grid):
                    game_over = True

        draw_grid(grid)

        if not game_over:
            draw_piece(current_piece)

        draw_text(score, game_over)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()