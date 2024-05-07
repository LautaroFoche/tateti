import pygame
pygame.init()
screen = pygame.display.set_mode((450,450))
pygame.display.set_caption('Tic Tac Toe')
fondo = pygame.image.load('static/tictactoe_background.png')
reset = pygame.image.load('static/RESET.png')
equis = pygame.image.load('static/x.png')
circulo = pygame.image.load('static/circle.png')
ganador_x = pygame.image.load('static/jugx.png')
ganador_o = pygame.image.load('static/jug0.png')
fondo = pygame.transform.scale(fondo, (450, 450))
reset = pygame.transform.scale(reset, (96, 29))
equis = pygame.transform.scale(equis, (125, 125))
circulo = pygame.transform.scale(circulo, (125, 125))
ganador_x = pygame.transform.scale(ganador_x, (400, 400))
ganador_o = pygame.transform.scale(ganador_o, (400, 400))
coor = [[(40,50), (165,50), (290,50)],
        [(40,175), (165,175), (290,175)],
        [(40,300), (165,300), (290,300)]]
tablero = [['','',''],
           ['','',''],
           ['','','']]
turno = 'X'
gameover = False
clock = pygame.time.Clock()
def graficar_board ():
    screen.blit(fondo, (0,0))
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 'X':
                dibujar_x(fila, col)
            elif tablero[fila][col] == 'O':
                dibujar_o(fila,col)
    screen.blit(reset, (1, 1))
def dibujar_x(fila, col):
    screen.blit(equis, coor[fila][col])
def dibujar_o(fila, col):
    screen.blit(circulo, coor[fila][col])
def ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
            return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
            return True
    return False
fin = False
while not gameover:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (mouseX >= 12 and mouseX < 87) and (mouseY >= 12 and mouseY < 25):
                tablero = [['','',''],
                           ['','',''],
                           ['','','']]
                turno = 'X'
                fin = False
            if (mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425) and not fin:
                fila = (mouseY - 50) // 125
                col = (mouseX - 40) // 125
                if tablero[fila][col] == '':
                    tablero[fila][col] = turno
                    fin = ganador()
                    if turno == 'X':
                        turno = 'O'
                    elif turno == 'O':
                        turno = 'X'
    graficar_board()
    if fin and turno == 'O': 
        screen.blit(ganador_x, (15, 35))
    elif fin and turno == 'X':
        screen.blit(ganador_o, (15, 35 ))
    pygame.display.update()
pygame.quit()