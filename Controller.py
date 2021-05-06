# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:53:17 2021

@author: tgome
"""
from View import View
from Model import Model
#producto cartesiano entre las listas


class Controller:
    def __init__(self):
        print("What's created Controller")
        nrows, ncols, n_mines = self.initialize()
        self.model = Model(nrows, ncols, n_mines)
        self.view = View()
        self.view.display(self.model.board)

    def initialize(self):
        #size_x = input("Ingrese la cantidad de filas -->")
        #size_y = input("Ingrese la cantidad de columnas -->")
        #n_mines = input("Ingrese la cantidad de minas -->")
        #return int(size_x), int(size_y), int(n_mines)
        return 4,4,5

    def play(self):
        pos = input("> ")
        row,col = pos.split()
        return int(row), int(col)
