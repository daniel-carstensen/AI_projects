# Author : Daniel Carstensen
# Date : 10/25/2022
# File name : MinimaxAI.py
# Class : COSC76
# Purpose :

import chess
from math import inf
import random


class MinimaxAI:
    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.p_color = None

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

    def cutoff_test(self, board, depth):
        return board.is_game_over() or depth >= self.max_depth

    def max_min_val(self, player, board, depth):
        if self.cutoff_test(board, depth):
            return self.eval(board), None

        if player == 'max':
            best_util = -inf
            next_player = 'min'
        elif player == 'min':
            best_util = inf
            next_player = 'max'

        moves = list(board.legal_moves)
        random.shuffle(moves)

        for curr_move in moves:
            board.push(curr_move)
            curr_util, next_move = self.max_min_val(next_player, board, depth + 1)
            board.pop()

            if player == 'max' and curr_util > best_util or player == 'min' and curr_util < best_util:
                best_util, best_move = curr_util, curr_move

        return best_util, best_move

    def choose_move(self, board):
        self.p_color = board.turn
        best_util, best_move = self.max_min_val('max', board, 0)

        return best_move
