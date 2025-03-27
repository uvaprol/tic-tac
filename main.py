import pygame
from game import *
pygame.init()

W = 610
H = 610

WHITE = (255, 255, 255)
RED   = (179, 55, 55)
GREEN = (47, 99, 64)
BLACK = (0, 0, 0)
BLUE  = (54, 156, 179)

message = ''

display = pygame.display.set_mode((W, H))

def render():
    display.fill(WHITE)
    pygame.draw.line(display, BLACK, (200, 0), (200, H), 5)
    pygame.draw.line(display, BLACK, (405, 0), (405, H), 5)
    pygame.draw.line(display, BLACK, (0, 200), (H, 200), 5)
    pygame.draw.line(display, BLACK, (0, 405), (H, 405), 5)
    for y in range(3):
        for x in range(3):
            display.blit(pygame.font.SysFont("None", 300).render(f'{fill[y][x]}', True, RED if fill[y][x] == 'x' else BLUE), [45 + 200 * x, 0 + 200 * y])
    display.blit(pygame.font.SysFont("None", 50).render(message, True, GREEN), [295, 295])
    pygame.display.flip()

render()
while not game_over:
    events = pygame.event.get()
    for event in events:
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x, y = x // 205, y // 205
            if player_step(x, y):
                message = win_check()
                render()
