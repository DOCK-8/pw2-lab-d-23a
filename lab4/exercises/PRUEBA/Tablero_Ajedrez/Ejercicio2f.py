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
tablero=par()
for fila in range(1,4):
    if fila%2==0 and fila!=1:
       tablero=tablero.up(par())
    else:
       tablero=tablero.up(impar())
draw(tablero)
