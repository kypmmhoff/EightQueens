import numpy as np

class Movements:

    def __init__(self, maxlength):
        combinationsBoard =[]
        for horizontalIndex in range(0,maxlength):
            row = self.getMatrixFrom(horizontalIndex, maxlength)
            combinationsBoard.append(row) 
        self.combinationsBoard = combinationsBoard       

    def getMatrixFrom(self, indexBase, maxSizeMatrix):
        array = []
        for column in range(0, maxSizeMatrix):        
            cell = self.getCellsByPosition(indexBase, column, maxSizeMatrix)
            array.append(cell)
        return array

    def getCellsByPosition(self, indexBase, column, maxSizeMatrix):
        tmpMatrix = np.zeros( (maxSizeMatrix,maxSizeMatrix), dtype=int )
        tmpVector = np.ones(maxSizeMatrix, dtype=int)[np.newaxis]
        identitySum= column - indexBase
        identity = np.eye(maxSizeMatrix, maxSizeMatrix, identitySum, dtype=int)

        rotSum = ( (maxSizeMatrix-1) - indexBase) - column
        r=np.eye(maxSizeMatrix, maxSizeMatrix, rotSum, dtype=int)
        les = np.rot90( r )
        tmpMatrix[indexBase:indexBase +1, 0:maxSizeMatrix] =  tmpMatrix[indexBase:indexBase +1, 0:maxSizeMatrix] + tmpVector    
        tmpMatrix[0:maxSizeMatrix, column:column +1] =  tmpMatrix[0:maxSizeMatrix, column:column +1] + tmpVector.T
        tmpMatrix = tmpMatrix + identity
        tmpMatrix = tmpMatrix + les
        return tmpMatrix