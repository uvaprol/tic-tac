fill = [[' ', ' ', ' '] for _ in range(3)]
step = 'x'
game_over = False

def player_step(x, y):
    global fill, step
    if fill[y][x] == ' ':
        fill[y][x] = step
        step = 'x' if step == 'o' else 'o'
        return True
    return False

def win_check():
    global fill
    for i in fill:
        if i == ['x' for _ in range(3)] or i == ['o' for _ in range(3)]:
            return (f'{i[0]} win')
    for i in range(3):
        if fill[0][i] == fill[1][i] == fill[2][i] and fill[0][i] != ' ':
            return (f'{fill[0][i]} win')
    if (fill[0][0] == fill[1][1] == fill[2][2] or fill[0][2] == fill[1][1] == fill[2][0]) and fill[1][1] != ' ':
        return (f'{fill[1][1]} win')
    for i in fill:
        if ' ' in i:
            return ' '
    return 'Draw'
