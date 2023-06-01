#encargado de los Movimientos validos, funcionamiento
from typing import Any


class game():
    def __init__(self):
        self.tab=[
            ["nT","nC","nA","nK","nR","nA","nC","nT"],
            ["nP","nP","nP","nP","nP","nP","nP","nP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wT","wC","wA","wR","wK","wA","wC","wT"],
        ]
        self.movW = True
        self.Cmov =[]