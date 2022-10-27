import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from CachedAlphaBetaAI import CachedAlphaBetaAI
from ChessGame import ChessGame


import sys


player1 = CachedAlphaBetaAI(3, 512)
player2 = AlphaBetaAI(3)

game = ChessGame(player1, player2)
# game.board = chess.Board(fen="rn1r2k1/1pq2p1p/p2p1bpB/3P4/P3Q3/2PB4/5PPP/2R1R1K1 w - - 1 2")

while not game.is_game_over():
    print(game)
    game.make_move()


print(str(game.board))
