import copy as cp
import numpy as np

class BuildByThread:

    def __init__(self, indexThread, boardSize, combinationsBoard ):
        self.combinationsBoard = combinationsBoard
        self.results = {}
        self.maxBoardSize = boardSize
        for boardInit in range(0,boardSize):
            recarray = cp.copy(self.combinationsBoard[indexThread][boardInit])
            self.evaluateMatrix(recarray,'%d,%d' % (indexThread, boardInit))  

    def normalize(self, stringBuilded):
        inArray=np.array(stringBuilded.split(',')).reshape(-1,2)
        if inArray.__len__() == self.maxBoardSize:
            sortedArray = sorted(inArray, key=lambda k: [ k[0], k[1] ])
            key=''
            for value in sortedArray:
                key+= '%s%s' % (value[0],value[1])
        
            if not(key in self.results):
                self.results[key]=sortedArray

    def evaluateMatrix(self, matrixToEvaluate, tmpResult):

        option = np.where(matrixToEvaluate == 0)

        if option[0].__len__() == 0:
            self.normalize(tmpResult)
            return

        for position in range(0, option[0].__len__()):
            queenOption = self.combinationsBoard[ option[0].item(position) ][ option[1].item(position) ]        
            self.evaluateMatrix(matrixToEvaluate + queenOption, tmpResult + ',%d,%d' % (option[0].item(position), option[1].item(position) ))       