from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal=self.img[::-1]
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    neg=[]
    for linea in range(len(self.img)):
        negativo=""
        for pixel in range(len(self.img[linea])):
            negativo+=self._invColor(self.img[linea][pixel])
        neg.append(negativo)
    return Picture(neg)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    nuevo=[]
    for linea in range(len(p.img)):
        nuevo.append(self.img[linea]+p.img[linea])
    return Picture(nuevo)

  def up(self, p):
    nuevo=p.img+self.img
    return Picture(nuevo)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    new=[]
    for (linea1,linea2) in zip(range(len(p.img)),range(len(self.img))):
        lineas=""
        for (pixel1,pixel2) in zip(p.img[linea1],self.img[linea2]):
            if pixel1==" ":
                lineas+=pixel2
            else:
                lineas+=pixel1
        new.append(lineas)
    return Picture(new)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeticion=[]
    for lineas in range(len(self.img)):
        repeticion.append(self.img[lineas]*int(n))
    return Picture(repeticion)

  def verticalRepeat(self, n):
    repeticion=[]
    repeticion+=self.img*int(n)
    return Picture(repeticion)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

