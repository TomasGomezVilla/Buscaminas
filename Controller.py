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
        self.view = View(nrows, ncols)


    def initialize(self):
        size_x = input("Ingrese la cantidad de filas --> ")
        size_y = input("Ingrese la cantidad de columnas --> ")
        n_mines = input("Ingrese la cantidad de minas --> ")
        return int(size_x), int(size_y), int(n_mines)
        #return 4,4,5

    def display(self):
        self.view.display()


    def play(self):
        pos = input("> ")
        row,col = pos.split()

        row = int (row)
        col = int (col)
        explosion=self.model.check(row, col)
        if explosion:
            self.view.update_position (row, col, val=2)
            return self.exit()
        else:
            self.view.update_position (row, col, val=1)
            return True

    def exit(self):
        print("Game Over")
        return False
