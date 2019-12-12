from Service import Operation
import time
import sys

if sys.argv.__len__() != 2:
    print('How to use:')
    print('     first argument, size of the board [int] ')
    sys.exit(1)

try:
    sBoardSize = sys.argv[1]
    boardSize= int(sBoardSize)

    t0 = time.time()
    operation = Operation()
    operation.buildEightQueens(boardSize)
    tf = time.time()
    total = tf-t0
    print('Elapsed time: %f sec.' % total)

except:
    print(':::Arguments need to be INT.')
    sys.exit(1)