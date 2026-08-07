import chess
import chess.svg

# DOCUMENTATION:
# https://python-chess.readthedocs.io/en/latest/core.html#chess.parse_square

board = chess.Board()
# print(board)
# board.push(chess.Move.from_uci("e2e4"))
# print()
# print(board)
# board.push(chess.Move.from_uci("d7d5"))
# print()
# print(board)
# print(board.legal_moves)
# board.push(chess.Move.from_uci("e4d5"))
# print()
# print(board)

print(board.is_legal(board.find_move(12, 28)))
board.push(board.find_move(12, 28))
print(board)
# piece_count
# piece_at