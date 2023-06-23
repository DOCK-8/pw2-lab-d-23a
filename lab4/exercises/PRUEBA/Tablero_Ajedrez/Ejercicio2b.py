from interpreter import draw
from chessPictures import *
draw(knight.negative().verticalMirror().up(knight).join(knight.verticalMirror().up(knight.negative())))
