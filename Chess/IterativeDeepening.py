# Author : Daniel Carstensen
# Date : 10/25/2022
# File name : IterativeDeepening.py
# Class : COSC76
# Purpose : Implementation of Iterative Deepening to iteratively call a chess search algorithm with increasing depth

from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
import chess


# Iterative Deepening class
class IterativeDeepening:

    # search_method: search method to be used by iterative deepening
    # max_depth: maximum depth of the search tree that should be explored using the search method
    # board: current chess board
    # best_moves: array that holds the best move at each depth
    def __init__(self, search_method, board):
        self.search_method = search_method
        self.max_depth = self.search_method.max_depth
        self.board = board
        self.best_moves = []

    # function to change the search method
    def change_search(self, search_method):
        self.search_method = search_method

    # function to iteratively call the search method with increasing depth until the maximum depth is reached
    def find_moves(self):
        for i in range(1, self.max_depth+1):
            self.search_method.max_depth = i
            self.best_moves.append(self.search_method.choose_move(self.board))

    # clear the array of best moves
    def clear_moves(self):
        self.best_moves.clear()

    # return the array of best moves
    def get_best_moves(self):
        return self.best_moves


# some testing using both AlphaBetaAI and MiniMaxAI
iter_deep = IterativeDeepening(AlphaBetaAI(4), chess.Board())
iter_deep.find_moves()
print(iter_deep.get_best_moves())

iter_deep.clear_moves()
iter_deep.change_search(MinimaxAI(4))
iter_deep.find_moves()
print(iter_deep.get_best_moves())