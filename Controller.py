# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:53:17 2021

@author: tgome
"""
from View import View
from Model import Model
import numpy as np
from itertools import product #producto cartesiano entre las listas


class Controller:
    def __init__(self): 
        print("What's created Controller")
        nrows, ncols, n_mines = self.initialize()
        self.view = View(nrows, ncols, n_mines)
        self.model = Model()
        self.view.display()

    def initialize(self):
        size_x = input("Ingrese la cantidad de filas -->")
        size_y = input("Ingrese la cantidad de columnas -->")
        n_mines = input("Ingrese la cantidad de minas -->")
        return int(size_x), int(size_y), int(n_mines)


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
