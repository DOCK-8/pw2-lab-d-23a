#Encargado de comprenderla entrada del usuario y generar la respuesta a ello
import pygame as p
import chessEngi

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT/DIMENSION
MAX_FPS = 15
IMAGES = {}

#Agrega imagenes a su respectivo contralador en chessEngi
def loadImages():
    pieces = ["nK","nR","nA","nC","nT","nP","wP","wR","wK","wA","wC","wT"]
    for piece in pieces:
        IMAGES[piece]=p.transform.scale(p.image.load("chessPicture/"+piece+".png"),(SQ_SIZE,SQ_SIZE))
#Clase main-> Ejecucion
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngi.game()
    loadImages()
    run = True
    while run:
        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
        clock.tick(MAX_FPS)
        p.display.flip()
        grafic(screen,gs)
'''
Integracion de piezas y tablero
'''     
def grafic(screen, gs):
    implet(screen)
    implep(screen,gs.tab)
'''
integrar los cuadros al tablero
'''
def implet(screen):
    color=[p.Color("white"),p.Color("gray")]
    for k in range(DIMENSION):
        for i in range(DIMENSION):
            col=color[((k+i)%2)]
            p.draw.rect(screen,col,p.Rect(i*SQ_SIZE,k*SQ_SIZE,SQ_SIZE,SQ_SIZE))         

'''
Integrar las piezas
'''            
def implep(screen, tablero):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece= tablero[r][c]
            if(piece != "--"):
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
    
    
    
    
    
if __name__ == "__main__":
    main()