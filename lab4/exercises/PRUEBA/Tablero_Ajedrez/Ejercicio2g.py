from interpreter import draw
from chessPictures import *
def impar ():
    an=square.negative()
    for i in range (1,8):
        if i%2==0 and i!=1:
            an=square.negative().join(an)
        else:
            an=square.join(an)
    return an
def par ():
    a=square
    for i in range (1,8):
        if i%2==0 and i!=1:
            a=square.join(a)
        else:
            a=square.negative().join(a)
    return a
def peones():
    return pawn.horizontalRepeat(8)
def fichas():
    return rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
tablero=par().under(fichas())
for fila in range(1,8):
    if fila%2==0 and fila!=1:
        if fila==6:
            tablero=tablero.up(par().under(peones().negative()))
        else:
            tablero=tablero.up(par())
    else:
        if fila==1:
            tablero=tablero.up(impar().under(peones()))
        elif fila==7:
            tablero=tablero.up(impar().under(fichas().negative()))
        else:
           tablero=tablero.up(impar())
draw(tablero)
