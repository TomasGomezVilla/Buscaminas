# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:53:25 2021

@author: tgome
"""
import numpy as np
from itertools import product

class View:
    def __init__(self, nrows, ncols, n_mines):
        print("What's created View")
        self.board = np.zeros([nrows,ncols])
        self.initialize (self.board, n_mines)

    def initialize(self, board, n_mines):
        nrows,ncols = board.shape
        pos= np.arange (nrows*ncols) #lista de # del 0 hasta (no inclusivo) el valor que se le ingresa
        selected_pos = np.random.choice(pos, n_mines, replace=False)
        I= (selected_pos/ncols).astype(int)
        J= selected_pos-I*ncols
        for i,j in zip(I,J): board[i,j]=1
        return board

    def display(self):
      print(self.board)



