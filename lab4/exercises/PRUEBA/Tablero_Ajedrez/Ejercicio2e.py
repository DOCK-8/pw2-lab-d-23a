from interpreter import draw
from chessPictures import *
a=square
for i in range (1,8):
    if i%2==0 and i!=1:
        a=square.join(a)
    else:
        a=square.negative().join(a)
draw(a)
