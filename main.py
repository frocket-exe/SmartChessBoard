import chess
import json

board = chess.Board()

def tryMove(board, oldSquareName, newSquareName):
    # oldSquare = (chess.parse_square(oldSquareName))
    # newSquare = (chess.parse_square(newSquareName))
    print()
    try:
        moveAttempt = board.find_move(oldSquareName, newSquareName)
        board.push(moveAttempt)
        print(board)
    except:
        print("Move not legal!")

# print(board)
# tryMove(board, "e2", "e5")
# tryMove(board, "e2", "e3")
# tryMove(board, "g1", "f3")
# tryMove(board, "g1", "g3")
# tryMove(board, "e2", "e4")
# tryMove(board, "e7", "e5")
# tryMove(board, "d2", "d4")
# tryMove(board, "e5", "d4")

def indexToBoardNum(arrIndex):
    row = 7-(arrIndex//8)
    column = arrIndex%8
    boardNum = row*8 + column
    return boardNum

def findMoved(oldBoard, newBoard):
    for i in range(0, 64):
        if(oldBoard[i] != newBoard[i]):
            return (indexToBoardNum(i))


def boardChange(board, oldBoard, newBoard):
    global moveFrom
    oldEmpty = oldBoard.count(0)
    # oldFull = oldBoard.count(1)
    newEmpty = newBoard.count(0)
    # newFull = newBoard.count(1)
    if newEmpty > oldEmpty:
        tryMoveFrom = findMoved(oldBoard, newBoard)
        if board.turn == board.piece_at(tryMoveFrom).color:
            moveFrom = tryMoveFrom
    if newEmpty < oldEmpty:
        moveTo = findMoved(oldBoard, newBoard)
        if moveTo != moveFrom:
            tryMove(board, moveFrom, moveTo)


with open ("board-states.json") as f:
    boardStates = json.load(f)

moveFrom = ""
print(board)
for i in range(1, len(boardStates)):
    boardChange(board, boardStates[i-1], boardStates[i])