import pygame
import sys
from handler import score_cells_horizontal, score_cells_vertical
from levels import levels
import time

STAGE = 0
art = levels[STAGE]

SCREEN_SIZE = (1000,1000)
BACKGROUND_COLOR = (255,255,255)
CELL_COLOR = (0,0,0)
CELL_SIZE = 500//len(art[0])


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(BACKGROUND_COLOR)
class Cell:
    def __init__(self,x,y,size):
        self.active = False
        self.x = x
        self.y = y
        self.width = 2
        self.size = size
        self.x_cords = range(x,x+size)
        self.y_cords = range(y,y+size)
        self.r = pygame.Rect(x,y, size,size)

    def draw(self):
        pygame.draw.rect(screen, CELL_COLOR, self.r, self.width)

    def clicked_fy(self, mouse_pos):
        if mouse_pos[0] in self.x_cords and mouse_pos[1] in self.y_cords:
            font = pygame.font.SysFont(None, self.size)
            text = font.render(str('X'), True, (255,0,0))
            if self.active is False:
                rect = pygame.Rect(self.x, self.y, self.size-1, self.size-1)
                pygame.draw.rect(screen, (48,50,52), rect, 0)
                self.active = True
            else:
                pygame.draw.rect(screen, BACKGROUND_COLOR, pygame.Rect(self.x,self.y,self.size,self.size), 0)
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.x, self.y, self.size, self.size), 2)
                self.active = False


def draw_cells(art):
    y = 0
    cell_count = len(art[0])
    for i in range(0,cell_count):
        x = 0
        line = []
        for k in range(0, cell_count):
            c = Cell(250+x, 200+y, CELL_SIZE)
            c.draw()
            x += CELL_SIZE
            line.append(c)
        cell_list.append(line)
        y += CELL_SIZE
    return cell_list

def draw_numbers():
    for i in range(len(cell_list[0])):
        space = -40
        for num in vertical_list[i][::-1]:
            cords = cell_list[0][i].x+30, cell_list[0][i].y + space
            font = pygame.font.SysFont(None, CELL_SIZE//2)
            text = font.render(str(num), True, (255,0,0))
            screen.blit(text, cords)
            space -= 40
    for i in range(len(cell_list[0])):
        space = -40
        for num in horizontal_list[i][::-1]:
            cords = cell_list[i][0].x+space, cell_list[i][0].y + 30
            font = pygame.font.SysFont(None, CELL_SIZE//2)
            text = font.render(str(num), True, (255,0,0))
            screen.blit(text, cords)
            space -= 40

def check_win():
    win_status = True
    for i in range(len(art)):
        for k in range(len(art)):
            if (art[i][k] == 1 and cell_list[i][k].active is True or
                art[i][k] == 0 and cell_list[i][k].active is False):
                pass
            else:
                win_status = False
    return win_status

def show_stage():
    font = pygame.font.SysFont(None, CELL_SIZE // 2)
    text = font.render(f'LEVEL {STAGE+1}', True, (0, 0, 0))
    screen.blit(text, (420,50))

def start_level(art):
    global horizontal_list, vertical_list, cell_list
    cell_list = []
    show_stage()
    horizontal_list, vertical_list = score_cells_horizontal(art), score_cells_vertical(art)
    draw_cells(art)
    draw_numbers()
    
def menu():

    font = pygame.font.SysFont(None, CELL_SIZE // 2)
    text = font.render(f'LEVEL {STAGE+1}', True, (0, 0, 0))
    screen.blit(text, (420,50))

start_level(art)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        if event.type == pygame.MOUSEBUTTONDOWN:
            for line in cell_list:
                for c in line:
                    c.clicked_fy(pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:
            pass

    if check_win():
        STAGE += 1
        screen.fill(BACKGROUND_COLOR)
        art = levels[STAGE]
        CELL_SIZE = 500 // len(art[0])
        start_level(art)
    pygame.display.flip()






