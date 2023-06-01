#Encargado de comprenderla entrada del usuario y generar la respuesta a ello
import pygame as p
import chessEngi

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT
MAX_FPS = 15
IMAGES = {}

#Agrega imagenes a su respectivo contralador en chessEngi
def loadImages():
    pieces = ["nK","nR","nA","nC","nT","nP","wP","wR","wK","wA","wC","wT"]
    for piece in pieces:
        IMAGES[piece]=p.transform.scale(p.image.load("chessPicture/"+pieces+".png"),(SQ_SIZE,SQ_SIZE))
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
        
def grafic(screen, gs):
    implet(screen)
    implep(screen,gs.tab)

def implet(screen):
    
def implep(screen, tablero):

    
if __name__ == "__main__":
main()