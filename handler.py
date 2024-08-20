def score_cells_horizontal(art):
    horizontal = {n: [] for n in range(len(art))}
    i = -1
    for list in art:
        lenght = 0
        i += 1
        for cell in list:
            if cell == 0 and lenght != 0:
                horizontal[i].append(lenght)
                lenght = 0
            elif cell == 1:
                lenght += 1
        if lenght != 0:
            horizontal[i].append(lenght)
    return horizontal

def score_cells_vertical(art):
    vertical = {n: [] for n in range(len(art))}
    i = -1
    for j in range(0,len(art[0])):
        lenght = 0
        i += 1
        for k in range(0,len(art[0])):
            cell = art[k][j]
            if cell == 0 and lenght != 0:
                vertical[i].append(lenght)
                lenght = 0
            elif cell == 1:
                lenght += 1
        if lenght != 0:
            vertical[i].append(lenght)
    return vertical
