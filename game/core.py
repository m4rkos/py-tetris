import pygame
import random

from game.utils.vars import (
    IMAGES_PATH,
    SOUNDS_PATH,
    CELL_SIZE,
    COLS,
    ROWS, 
    WIDTH,
    HEIGHT,
    SIDE_PANEL,
    BLACK,
    GRID,
    WHITE,
    SHAPES,
    COLORS
)

pygame.init()
pygame.mixer.init()

game_over_image = pygame.transform.scale(
        pygame.image.load(IMAGES_PATH + "game_over.png"), 
        (160, 160))

move_sound = pygame.mixer.Sound(SOUNDS_PATH + "mixkit-game-ball-tap-2073.wav")
down_sound = pygame.mixer.Sound(SOUNDS_PATH + "mixkit-arcade-mechanical-bling-210.wav")
fast_down_sound = pygame.mixer.Sound(SOUNDS_PATH + "mixkit-martial-arts-fast-punch-2047.wav")
rotate_sound = pygame.mixer.Sound(SOUNDS_PATH + "mixkit-player-jumping-in-a-video-game-2043.wav")
clear_sound = pygame.mixer.Sound(SOUNDS_PATH + "mixkit-winning-a-coin-video-game-2069.wav")
gameover_sound = pygame.mixer.Sound(SOUNDS_PATH + "mixkit-player-losing-or-failing-2042.wav")

screen = pygame.display.set_mode((WIDTH + SIDE_PANEL, HEIGHT))
pygame.display.set_caption("Py Tetris - premiss.io")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)


class Piece:
    def __init__(self, shape_index=None):
        if shape_index is None:
            shape_index = random.randint(0, len(SHAPES) - 1)

        self.index = shape_index
        self.shape = SHAPES[shape_index]
        self.color = COLORS[shape_index]
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def draw(self):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        (self.x + x) * CELL_SIZE,
                        (self.y + y) * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )

                    pygame.draw.rect(screen, self.color, rect)
                    pygame.draw.rect(screen, BLACK, rect, 2)

    def draw_next(self):
        label = font.render("Next:", True, WHITE)
        screen.blit(label, (WIDTH + 20, 320))

        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        WIDTH + 30 + x * CELL_SIZE,
                        370 + y * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )

                    pygame.draw.rect(screen, self.color, rect)
                    pygame.draw.rect(screen, BLACK, rect, 2)

    def draw_ghost(self, grid):
        ghost_y = self.y

        while True:
            test_piece = Piece(self.index)
            test_piece.shape = [row[:] for row in self.shape]
            test_piece.x = self.x
            test_piece.y = ghost_y + 1

            if valid_position(test_piece, grid):
                ghost_y += 1
            else:
                break

        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        (self.x + x) * CELL_SIZE,
                        (ghost_y + y) * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )

                    ghost_color = (
                        max(self.color[0] // 3, 30),
                        max(self.color[1] // 3, 30),
                        max(self.color[2] // 3, 30)
                    )

                    pygame.draw.rect(screen, ghost_color, rect, 2)


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

    if cleared > 0:
        clear_sound.play()

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


def draw_text(score, game_over):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH + 20, 40))

    help_text = [
        "← → move",
        "↓ down",
        "↑ rotate",
        "Space drop",
        "R restart"
    ]

    small_font = pygame.font.SysFont("Arial", 18)

    for i, text in enumerate(help_text):
        rendered = small_font.render(text, True, WHITE)
        screen.blit(rendered, (WIDTH + 20, 100 + i * 25))

    if game_over:
        screen.blit(game_over_image, (WIDTH + 10, 100))

        over = font.render("GAME OVER", True, (255, 80, 80))
        screen.blit(over, (WIDTH + 15, 300))

        restart_text = pygame.font.SysFont("Arial", 20).render(
            "Press R to Restart",
            True,
            WHITE
        )

        screen.blit(restart_text, (WIDTH + 10, 390))


def hard_drop(piece, grid):
    while valid_position(piece, grid, offset_y=1):
        piece.y += 1


def reset_game():
    grid = create_grid()
    current_piece = Piece()
    next_piece = Piece()

    score = 0
    game_over = False

    return grid, current_piece, next_piece, score, game_over


def main():
    grid, current_piece, next_piece, score, game_over = reset_game()

    fall_time = 0
    fall_speed = 500

    running = True

    while running:
        dt = clock.tick(60)
        fall_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    grid, current_piece, next_piece, score, game_over = reset_game()

                if not game_over:

                    if event.key == pygame.K_LEFT:
                        if valid_position(current_piece, grid, offset_x=-1):
                            current_piece.x -= 1
                            move_sound.play()

                    elif event.key == pygame.K_RIGHT:
                        if valid_position(current_piece, grid, offset_x=1):
                            current_piece.x += 1
                            move_sound.play()

                    elif event.key == pygame.K_DOWN:
                        if valid_position(current_piece, grid, offset_y=1):
                            current_piece.y += 1
                            down_sound.play()

                    elif event.key == pygame.K_UP:
                        old_shape = current_piece.shape
                        current_piece.rotate()
                        rotate_sound.play()

                        if not valid_position(current_piece, grid):
                            current_piece.shape = old_shape

                    elif event.key == pygame.K_SPACE:
                        hard_drop(current_piece, grid)
                        fast_down_sound.play()

        if not game_over and fall_time >= fall_speed:
            fall_time = 0

            if valid_position(current_piece, grid, offset_y=1):
                current_piece.y += 1
            else:
                lock_piece(current_piece, grid)
                grid, cleared = clear_lines(grid)
                score += cleared * 100

                current_piece = next_piece
                next_piece = Piece()

                if not valid_position(current_piece, grid):
                    game_over = True
                    gameover_sound.play()

        draw_grid(grid)

        if not game_over:
            current_piece.draw_ghost(grid)
            current_piece.draw()
            current_piece.draw_next()

        draw_text(score, game_over)

        pygame.display.flip()

    pygame.quit()
