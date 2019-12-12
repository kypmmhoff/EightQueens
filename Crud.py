from  sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from Model import Base, Engine, Board, Solution

Base.metadata.bind = Engine
DBSession = sessionmaker(bind=Engine)
session = DBSession()

class BoardCrud:

    def solutionByBoardSize(self, boardSize):
        board = session.query(Board).filter(Board.size == boardSize).all()
        result=0
        if board.__len__() > 0:
            solutions = session.query(Solution).filter(Solution.board == board[0]).all()
            result = solutions.__len__()
            print('Board size: %d = %d options' % (boardSize, result))
            for solution in solutions:
                print(solution.positions)

        return result

    def existSolutionByBoard(self, size):
        board = session.query(Board).filter(Board.size == size).all()
        if board.__len__() > 0:
            exist = session.query(func.count(Solution.id)).filter(Solution.board == board[0]).all()
            if exist == 0:
                return False
            return True
        return False

    def saveAllBoard(self, board, solutions):

        if self.existSolutionByBoard(board.size):
            print('>>> There is information with this board size. (%d)' % board.size)
            return

        _board = board
        session.add(_board)
        session.flush()

        for _solution in solutions:
            _solution.board_id = _board.id
            session.add(_solution)
        session.commit()

    def cleanBoardBySize(self, size):
        board = session.query(Board).filter(Board.size == size).all()
        if board.__len__() > 0:
            deleteSolutions = Solution.__table__.delete().where(Solution.board == board[0])
            session.execute(deleteSolutions)
            session.flush()
            session.delete(board[0])
            session.commit()
            print('>>> Board solutions %d have been deleted.' % size)
