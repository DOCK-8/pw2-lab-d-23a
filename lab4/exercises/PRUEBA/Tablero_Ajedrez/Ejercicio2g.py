from interpreter import draw
from chessPictures import *
def impar ():
    fila_impar=square.negative()
    for columna in range (1,8):
        if columna%2==0 and columna!=1:
            fila_impar=square.negative().join(fila_impar)
        else:
            fila_impar=square.join(fila_impar)
    return fila_impar
def par ():
    fila_par=square
    for fila in range (1,8):
        if fila%2==0 and fila!=1:
            fila_par=square.join(fila_par)
        else:
            fila_par=square.negative().join(fila_par)
    return fila_par
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
