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
        
    def makeMove(self,move):
        self.tab[move.startRow][move.startCol] = "--"
        self.tab[move.endRow][move.endCol] = move.pieceMoved
        self.Cmov.append(move)
        self.movW = not self.movW
        
class movi ():
    ranksToRows = {"1":7, "2":6, "3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    
    def __init__(self, startSq, endSq, tabl):
        self.startRow = int(startSq[0])
        self.startCol = int(startSq[1])
        self.endRow = int(endSq[0])
        self.endCol = int(endSq[1])
        self.pieceMoved = tabl[self.startRow][self.startCol]
        self.pieceCaptured = tabl[self.endRow][self.endCol]
    
    def getChessNotation(self):
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)
    def getRankFile(self,r,c):
        return self.colsToFiles[c] + self.rowsToRanks[r]    