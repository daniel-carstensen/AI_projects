# Author : Daniel Carstensen
# Date : 10/25/2022
# File name : CachedAlphaBetaAI.py
# Class : COSC76
# Purpose : Implementation of Alpha-beta pruning algorithm to find best move in chess game
#           implementing transposition table as LRU cache

import chess
from math import inf
import random
from LRUCache import LRUCache


# Alpha-beta pruning class with cache that can be instantiated as a player
class CachedAlphaBetaAI:

    # max_depth: maximum depth of the search tree that should be explored
    # p_color: keep track of the player whose turn it is
    # max_size: maximum size of cache
    # cache: instance of LRU cache
    def __init__(self, max_depth, max_size):
        self.max_depth = max_depth
        self.p_color = None
        self.cache = LRUCache(max_size)

    # heuristic evaluation function that returns an estimated utility value of a move
    # heuristic based on assigning values to each piece type in the game and counting the number of pieces
    # for each piece type
    # use cache to store calculated utility
    # return the utility value
    def eval(self, board, hash_board):

        # if hashed board has value in cache return value
        if self.cache.get(hash_board) is not None:
            print('Cached Utility used')    # print that cache is used to return previously calculated utility
            return self.cache.get(hash_board)

        pieces = {chess.PAWN: 1/ 121, chess.KNIGHT: 3 / 121, chess.BISHOP: 3 / 121, chess.ROOK: 5 / 121,
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

        self.cache.put(hash_board, utility)     # store utility value in cache

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
    # alpha: minimum utility of the max player
    # beta: maximum utility of the min player
    # return the best utility value and the corresponding best move
    def max_min_val(self, player, board, depth, alpha, beta):
        if self.cutoff_test(board, depth):
            return self.eval(board, hash(str(board))), None

        if player == 'max':     # if current player is max
            best_util = -float('inf')
            next_player = 'min'
        elif player == 'min':   # if current player is min
            best_util = float('inf')
            next_player = 'max'

        moves = list(board.legal_moves)
        random.shuffle(moves)

        # perform recursive search of each branch of the search tree
        for curr_move in moves:
            board.push(curr_move)
            curr_util, next_move = self.max_min_val(next_player, board, depth + 1, alpha, beta)
            board.pop()

            if player == 'max':
                if curr_util > best_util:
                    best_util, best_move = curr_util, curr_move
                    alpha = max(alpha, best_util)

                if alpha > beta:    # pruning of paths that will not occur if both players are rational
                    return best_util, best_move

            elif player == 'min':
                if curr_util < best_util:
                    best_util, best_move = curr_util, curr_move
                    beta = min(beta, best_util)

                if beta < alpha:    # pruning of paths that will not occur if both players are rational
                    return best_util, best_move

        return best_util, best_move

    # choose the best move for the player
    # initialize max_min_val for the player
    # return the best move that was found
    def choose_move(self, board):
        self.p_color = board.turn
        best_util, best_move = self.max_min_val('max', board, 0, -inf, inf)
        return best_move
