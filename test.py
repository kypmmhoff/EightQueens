from Service import Operation

class TestCases:

    def test_sizeFour(self):
        boardSize = 4
        expectedSize = 2
        operation = Operation()
        result = operation.buildEightQueens(boardSize)        
        assert result == expectedSize

    def test_sizeFive(self):
        boardSize = 5
        expectedSize = 10
        operation = Operation()
        result = operation.buildEightQueens(boardSize)        
        assert result == expectedSize        

    def test_sizeSix(self):
        boardSize = 6
        expectedSize = 4
        operation = Operation()
        result = operation.buildEightQueens(boardSize)        
        assert result == expectedSize

    def test_sizeSeven(self):
        boardSize = 7
        expectedSize = 40
        operation = Operation()
        result = operation.buildEightQueens(boardSize)        
        assert result == expectedSize

    def test_sizeEight(self):
        boardSize = 8
        expectedSize = 92
        operation = Operation()
        result = operation.buildEightQueens(boardSize)        
        assert result == expectedSize                

