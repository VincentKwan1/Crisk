import chess
import chess.pgn as cp
import chess.svg as db
pgn = open(r'C:\Users\kwanv\Desktop\Programming\Projects\Chess Risk\lichess_db_standard_rated_2013-01.pgn\lichess_db_standard_rated_2013-01.pgn')

first_game = cp.read_game(pgn)
board = chess.Board()
for move in first_game.mainline_moves():
    board.push(move)

db.board(board, size=400)