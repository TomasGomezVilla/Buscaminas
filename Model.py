# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:52:33 2021

@author: tgome
"""
#croquis de los objetos
import numpy as np

class Model:
    def __init__(self, nrows, ncols, n_mines):
        print("What's created Model")
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

    def check (self, row, col):
        if self.board[row,col] == 1:
            return True
        else:
            return False
    ##manejo de errores: expepciones -

    def initialize2(self):
        #Pimera parte del código

        size_x = input( "Ingrese la cantidad de columnas -->")
        size_y = input ( "Ingrese la cantidad de filas -->")
        size_x= int (size_x)
        size_y= int (size_y)
        shape = [size_y, size_x]
        board = np.zeros (shape)

        n_mines = input ("Ingrese la cantidad de minas -->")
        n_mines = int (n_mines)

        #mine_rand_col = np.random.randint (0, size_x, n_mines)
        #mine_rand_row = np.random.randint (0, size_y, n_mines)
        #con este código las posiciones se repiten, ya que saca el resultado al azar, está la posibiliad por lo tanto de que se repita la posición

        col_idx = np.arange (size_x)
        row_idx = np.arange (size_y)
        pos_idx = np.arange (size_x*size_y)
        #print (pos_idx)
        positions = []

        for col,row in product (col_idx, row_idx) :  #corre 2 listas al mismo tiempo - misma dim
            positions.append ([row, col])

            #print(positions)

        selected_pos_idx = np.random.choice (pos_idx, n_mines, replace = False)  #selecciona n elementos de lista de índices

        for pos_idx in selected_pos_idx:
            row,col = positions [pos_idx]
            board [row,col] =1
        return board

        #se pueden hacer cambios para optimizar el uso de la memoría
