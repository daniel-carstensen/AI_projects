# Author : Daniel Carstensen
# Date : 10/25/2022
# File name : MinimaxAI.py
# Class : COSC76
# Purpose : Implementation of Minimax algorithm to find best move in chess game

import chess
from math import inf
import random


# Minimax class that can be instantiated as a player
class MinimaxAI:

    # max_depth: maximum depth of the search tree that should be explored
    # p_color: keep track of the player whose turn it is
    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.p_color = None

    # heuristic evaluation function that returns an estimated utility value of a move
    # heuristic based on assigning values to each piece type in the game and counting the number of pieces
    # for each piece type
    # return the utility value
    def eval(self, board):
        pieces = {chess.PAWN: 1 / 121, chess.KNIGHT: 3 / 121, chess.BISHOP: 3 / 121, chess.ROOK: 5 / 121,
                  chess.QUEEN: 9 / 121, chess.KING: 100 / 121}

        white_utility = 0
        black_utility = 0

        for piece in pieces.keys():
            white_utility += len(board.pieces(piece, chess.WHITE)) * pieces.get(piece)
            black_utility += len(board.pieces(piece, chess.BLACK)) * pieces.get(piece)

        if self.p_color:
            utility = white_utility - black_utility
        else:
            utility = black_utility - white_utility

        return utility

    # cutoff test that stops the search if the game is over (leaf node has been found)
    # or the maximum depth has been reached
    # return True or False
    def cutoff_test(self, board, depth):
        return board.is_game_over() or depth >= self.max_depth

    # max_min (combined max and min function)
    # player: player whose turn it is at current depth
    # board: current move
    # depth: current depth
    # return the best utility value and the corresponding best move
    def max_min_val(self, player, board, depth):
        # return the utility value of the evaluation function if the cutoff test is true
        if self.cutoff_test(board, depth):
            return self.eval(board), None

        if player == 'max':     # if current player is max
            best_util = -inf
            next_player = 'min'
        elif player == 'min':   # if current player is min
            best_util = inf
            next_player = 'max'

        moves = list(board.legal_moves)
        random.shuffle(moves)

        # perform recursive search of each branch of the search tree
        for curr_move in moves:
            board.push(curr_move)
            curr_util, next_move = self.max_min_val(next_player, board, depth + 1)
            board.pop()

            if player == 'max' and curr_util > best_util or player == 'min' and curr_util < best_util:
                best_util, best_move = curr_util, curr_move

        return best_util, best_move

    # choose the best move for the player
    # initialize max_min_val for the player
    # return the best move that was found
    def choose_move(self, board):
        self.p_color = board.turn
        best_util, best_move = self.max_min_val('max', board, 0)

        return best_move
