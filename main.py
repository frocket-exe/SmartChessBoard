import chess

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

print(board)
tryMove(board, "e2", "e5")
tryMove(board, "e2", "e3")
tryMove(board, "g1", "f3")
tryMove(board, "g1", "g3")
tryMove(board, "e2", "e4")
tryMove(board, "e7", "e5")
tryMove(board, "d2", "d4")
tryMove(board, "e5", "d4")