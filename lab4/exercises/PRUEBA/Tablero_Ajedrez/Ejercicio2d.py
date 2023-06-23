from interpreter import draw
from chessPictures import *
a=square.negative()
for i in range (1,8):
    if i%2==0 and i!=1:
        a=square.negative().join(a)
    else:
        a=square.join(a)
draw(a)
