import chess
import json

board = chess.Board()

def tryMove(board, oldSquareName, newSquareName):
    oldSquare = (chess.parse_square(oldSquareName))
    newSquare = (chess.parse_square(newSquareName))
    print()
    try:
        moveAttempt = board.find_move(oldSquare, newSquare)
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

def boardChange(oldBoard, newBoard):
    global movingPiece
    oldEmpty = oldBoard.count(0)
    # oldFull = oldBoard.count(1)
    newEmpty = newBoard.count(0)
    # newFull = newBoard.count(1)
    if newEmpty > oldEmpty:
        movingPiece = 

with open ("board-states.json") as f:
    boardStates = json.load(f)

movingPiece = ""
boardChange(boardStates[0], boardStates[1])