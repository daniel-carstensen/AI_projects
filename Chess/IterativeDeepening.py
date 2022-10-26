# Author : Daniel Carstensen
# Date : 10/25/2022
# File name : IterativeDeepening.py
# Class : COSC76
# Purpose :

from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
import chess


class IterativeDeepening:

    def __init__(self, search_method, board):
        self.search_method = search_method
        self.max_depth = self.search_method.max_depth
        self.board = board
        self.best_moves = []

    def change_search(self, search_method):
        self.search_method = search_method

    def find_moves(self):
        for i in range(1, self.max_depth+1):
            self.search_method.max_depth = i
            self.best_moves.append(self.search_method.choose_move(self.board))

    def clear_moves(self):
        self.best_moves.clear()


iter_deep = IterativeDeepening(AlphaBetaAI(4), chess.Board())
iter_deep.find_moves()
print(iter_deep.best_moves)

iter_deep.clear_moves()
iter_deep.change_search(MinimaxAI(4))
iter_deep.find_moves()
print(iter_deep.best_moves)