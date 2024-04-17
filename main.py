import pygame
from time import sleep
pygame.init()
w = 610 # ширина экрана
h = 610 # высота экрана
display = pygame.display.set_mode((w, h))

white = (255, 255, 255)
red = (179, 55, 55)
green = (47, 99, 64)
black = (0, 0, 0)
blue = (54, 156, 179)

field = [['' for _ in range(3)] for _ in range(3)]
X_flag = True
message = ''
game_over = False

def render():
    display.fill(white)
    pygame.draw.line(display, black, (200, 0), (200, h), 5)
    pygame.draw.line(display, black, (405, 0), (405, h), 5)
    pygame.draw.line(display, black, (0, 200), (h, 200), 5)
    pygame.draw.line(display, black, (0, 405), (h, 405), 5)
    for y in range(3):
        for x in range(3):
            if field[y][x] == 'x':
                display.blit(pygame.font.SysFont("None", 300).render('x', True, red), [45 + 200 * x, 0 + 200 * y])
            elif field[y][x] == 'o':
                display.blit(pygame.font.SysFont("None", 300).render('o', True, blue), [45 + 200 * x, 0 + 200 * y])
    display.blit(pygame.font.SysFont("None", 50).render(message, True, green), [295, 295])
    pygame.display.flip()

def check_game_over():
    global game_over
    global message
    for line in field:
        if line == ['x', 'x', 'x'] or line == ['o', 'o', 'o']:
            message = 'You win!'
            game_over = True
            return
    for colum in range(3):
        if field[0][colum] == field[1][colum] == field[2][colum] == 'x' or field[0][colum] == field[1][colum] == field[2][colum] == 'o':
            message = 'You win!'
            game_over = True
            return
    if field[0][0] == field[1][1] == field[2][2] == 'x' or field[0][1] == field[1][1] == field[2][0] == 'x' or field[0][0] == field[1][1] == field[2][2] == 'o' or field[0][1] == field[1][1] == field[2][0] == 'o':
        message = 'You win!'
        game_over = True
        return

    for line in field:
        if not '' in line:
            game_over = True
        else:
            game_over = False
            break
    if game_over:
        message = 'Draw'
        game_over = True

def user_step(x, y):
    global X_flag
    global field
    if field[y][x] == '':
        if X_flag:
            field[y][x] = 'x'
            X_flag = False
        else:
            field[y][x] = 'o'
            X_flag = True

render()
while not game_over:
    display.fill(white)
    events = pygame.event.get()
    for event in events:
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x, y = x // 205, y // 205
            user_step(x, y)
            check_game_over()
            render()

sleep(5)
