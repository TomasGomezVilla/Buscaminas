# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:59:30 2021

@author: tgome
"""
#Pimera parte del código
import numpy as np
from itertools import product #producto cartesiano entre las listas

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
print (board)
