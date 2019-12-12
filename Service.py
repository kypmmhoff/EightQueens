from BuildOptions import Movements
from ByThread import BuildByThread
from Utils import mergeDictionaries, formatArray
from Model import Board, Solution
from Crud import BoardCrud

class Operation:

    def buildEightQueens(self, boardSize):
        combinationsBoard = []
        resultBoard={}

        bc = BoardCrud()
        if not bc.existSolutionByBoard(boardSize):
            print('There are no solutions stored for %d, building...' % boardSize)
            mov = Movements(boardSize)
            combinationsBoard = mov.combinationsBoard
            
            founded = BuildByThread(0, boardSize, combinationsBoard)
            resultBoard = mergeDictionaries(resultBoard, founded.results)  

            self.saveSolutionsBoard(boardSize, resultBoard)

        return self.getBoardBySize(boardSize)        

    def saveSolutionsBoard(self, sizeBoard, resultBoard):
        board = Board(size=sizeBoard, description='%dX%d Size' % (sizeBoard, sizeBoard))
        solutions = []

        print('Start storing board.')
        for key in resultBoard:
            coord = resultBoard[key]
            stringArray = formatArray(coord)
            solutions.append( Solution(positions=stringArray) )

        bc = BoardCrud()
        bc.saveAllBoard(board, solutions)

    def getBoardBySize(self, sizeBoard):
        bc = BoardCrud()
        return bc.solutionByBoardSize(sizeBoard)
     


            