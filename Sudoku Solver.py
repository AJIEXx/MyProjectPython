# This Python project uses the pygame library (see pip install instructions) to implement a GUI for automatically solving sudoku puzzles. We use several user-defined functions to create the GUI, as shown below.
# To solve a sudoku puzzle, this program uses a backtracking algorithm that incrementally checks for solutions, either adopting or abandoning the current solution if it’s not viable.
# This step of abandoning a solution is the defining feature of a backtracking approach, as the program steps back to try a new solution until it finds a valid one. This process is incrementally carried out until the entire grid has been correctly filled.
# Feel free to experiment with different sudoku problems, and even think about expanding the size of the problem grid (you’ll need a new base image if you do this).
#
# Этот проект на Python использует библиотеку pygame (см. Инструкции по установке pip) для реализации графического интерфейса для автоматического решения головоломок судоку. Мы используем несколько пользовательских функций для создания графического интерфейса, как показано ниже.
# Для решения головоломки судоку эта программа использует алгоритм обратного отслеживания, который постепенно проверяет наличие решений, либо принимая, либо отказываясь от текущего решения, если оно нежизнеспособно.
# Этот шаг отказа от решения является определяющей чертой подхода с возвратом, поскольку программа делает шаг назад, чтобы попробовать новое решение, пока не найдет правильное. Этот процесс выполняется постепенно, пока вся сетка не будет заполнена правильно.
# Не стесняйтесь экспериментировать с различными задачами судоку и даже подумайте об увеличении размера сетки задач (для этого вам понадобится новое базовое изображение).

'''
Sudoku Solver
-------------------------------------------------------------
pip install pygame
image link:
https://www.pngitem.com/pimgs/m/210-2106648_empty-sudoku-grid-grid-6x6-png-transparent-png.png
'''


import pygame


pygame.font.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('SUDOKU SOLVER USING BACKTRACKING')
img = pygame.image.load('icon.png')
pygame.display.set_icon(img)
font1 = pygame.font.SysFont('comicsans', 40)
font2 = pygame.font.SysFont('comicsans', 20)
x = 0
y = 0
dif = 500 / 9
val = 0

# Default Sudoku Board
grid = [
   [7, 8, 0, 4, 0, 0, 1, 2, 0],
   [6, 0, 0, 0, 7, 5, 0, 0, 9],
   [0, 0, 0, 6, 0, 1, 0, 7, 8],
   [0, 0, 7, 0, 4, 0, 2, 6, 0],
   [0, 0, 1, 0, 5, 0, 9, 3, 0],
   [9, 0, 4, 0, 6, 0, 0, 0, 5],
   [0, 7, 0, 3, 0, 0, 0, 1, 2],
   [1, 2, 0, 0, 0, 7, 4, 0, 0],
   [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def get_coord(pos):
   x = pos[0] // dif
   y = pos[1] // dif


def draw_box():
   for i in range(2):
       pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)
                        * dif), (x * dif + dif + 3, (y + i)*dif), 7)
       pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif,
                        y * dif), ((x + i) * dif, y * dif + dif), 7)


def draw():
   for i in range(9):
       for j in range(9):
           if grid[i][j] != 0:
               pygame.draw.rect(screen, (0, 153, 153),
                                (i * dif, j * dif, dif + 1, dif + 1))
               text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
               screen.blit(text1, (i * dif + 15, j * dif + 15))

   for i in range(10):
       if i % 3 == 0:
           thick = 7
       else:
           thick = 1
       pygame.draw.line(screen, (0, 0, 0), (0, i * dif),
                        (500, i * dif), thick)
       pygame.draw.line(screen, (0, 0, 0), (i * dif, 0),
                        (i * dif, 500), thick)


def draw_val(val):
   text1 = font1.render(str(val), 1, (0, 0, 0))
   screen.blit(text1, (x * dif + 15, y * dif + 15))


def raise_error_1():
   text1 = font1.render('WRONG !!!', 1, (0, 0, 0))
   screen.blit(text1, (20, 570))


def raise_error_2():
   text1 = font1.render('Wrong !!! Not a valid Key', 1, (0, 0, 0))
   screen.blit(text1, (20, 570))


def valid(m, i, j, val):
   for it in range(9):
       if m[i][it] == val:
           return False
       if m[it][j] == val:
           return False

   it = i // 3
   jt = j // 3

   for i in range(it * 3, it * 3 + 3):
       for j in range(jt * 3, jt * 3 + 3):
           if m[i][j] == val:
               return False
   return True


def solve(grid, i, j):
   while grid[i][j] != 0:
       if i < 8:
           i += 1
       elif i == 8 and j < 8:
           i = 0
           j += 1
       elif i == 8 and j == 8:
           return True

   pygame.event.pump()
   for it in range(1, 10):
       if valid(grid, i, j, it) == True:
           grid[i][j] = it
           x = i
           y = j
           screen.fill((255, 255, 255))
           draw()
           draw_box()
           pygame.display.update()
           pygame.time.delay(20)

           if solve(grid, i, j) == 1:
               return True
           else:
               grid[i][j] = 0
           screen.fill((255, 255, 255))

           draw()
           draw_box()
           pygame.display.update()
           pygame.time.delay(50)
   return False


def instruction():
  text1 = font2.render(
      'PRESS D TO RESET TO DEFAULT / R TO EMPTY\n', 1, (0, 0, 0))
  text2 = font2.render(
      'ENTER VALUES AND PRESS ENTER TO VISUALIZE\n', 1, (0, 0, 0))
  screen.blit(text1, (20, 520))
  screen.blit(text2, (20, 540))


def result():
  text1 = font1.render('FINISHED PRESS R or D\n', 1, (0, 0, 0))
  screen.blit(text1, (20, 570))


run = True
flag_1 = 0
flag_2 = 0
rs = 0
error = 0
while run:
   screen.fill((255, 255, 255))
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
       if event.type == pygame.MOUSEBUTTONDOWN:
           flag_1 = 1
           pos = pygame.mouse.get_pos()
           get_coord(pos)
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
               x -= 1
               flag_1 = 1
           if event.key == pygame.K_RIGHT:
               x += 1
               flag_1 = 1
           if event.key == pygame.K_UP:
               y -= 1
               flag_1 = 1
           if event.key == pygame.K_DOWN:
               y += 1
               flag_1 = 1
           if event.key == pygame.K_1:
               val = 1
           if event.key == pygame.K_2:
               val = 2
           if event.key == pygame.K_3:
               val = 3
           if event.key == pygame.K_4:
               val = 4
           if event.key == pygame.K_5:
               val = 5
           if event.key == pygame.K_6:
               val = 6
           if event.key == pygame.K_7:
               val = 7
           if event.key == pygame.K_8:
               val = 8
           if event.key == pygame.K_9:
               val = 9
           if event.key == pygame.K_RETURN:
               flag_2 = 1

           # If R pressed clear sudoku board
           if event.key == pygame.K_r:
               rs = 0
               error = 0
               flag_2 = 0
               grid = [
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]
               ]

           # If D pressed reset board to default
           if event.key == pygame.K_d:
               rs = 0
               error = 0
               flag_2 = 0
               grid = [
                   [7, 8, 0, 4, 0, 0, 1, 2, 0],
                   [6, 0, 0, 0, 7, 5, 0, 0, 9],
                   [0, 0, 0, 6, 0, 1, 0, 7, 8],
                   [0, 0, 7, 0, 4, 0, 2, 6, 0],
                   [0, 0, 1, 0, 5, 0, 9, 3, 0],
                   [9, 0, 4, 0, 6, 0, 0, 0, 5],
                   [0, 7, 0, 3, 0, 0, 0, 1, 2],
                   [1, 2, 0, 0, 0, 7, 4, 0, 0],
                   [0, 4, 9, 2, 0, 6, 0, 0, 7]
               ]

   if flag_2 == 1:
       if solve(grid, 0, 0) == False:
           error = 1
       else:
           rs = 1
       flag_2 = 0

   if val != 0:
       draw_val(val)
       if valid(grid, int(x), int(y), val) == True:
           grid[int(x)][int(y)] = val
           flag_1 = 0
       else:
           grid[int(x)][int(y)] = 0
           raise_error_2()
       val = 0

   if error == 1:
       raise_error_1()
   if rs == 1:
       result()
   draw()
   if flag_1 == 1:
       draw_box()
   instruction()

   pygame.display.update()