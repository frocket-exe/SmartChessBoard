import chess
import chess.svg

board = chess.Board()
print(board)
board.push(chess.Move.from_uci("e2e4"))
print()
print(board)
board.push(chess.Move.from_uci("d7d5"))
print()
print(board)
print(board.legal_moves)
board.push(chess.Move.from_uci("e4d5"))
print()
print(board)

# find_move
# piece_count
# piece_at