# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:53:25 2021

@author: tgome
"""
import numpy as np

class View:
    def __init__(self, nrows, ncols):
        print("What's created View")
        self.board = np.zeros([nrows,ncols])

    def display(self):
        print(self.board)
    
    def update_position(self, row, col, val): 
        self.board [row,col] = val
        
        

    def display2(self):
        nrows,ncols = self.board.shape
        print (end="  ")

        for j in range(ncols):
            print(j, end=" ")
        print()

        for i in range(nrows):
            print(i, end=" ")
            for j in range (ncols):
                print("x ",end="")
            print()  #tiene por defecto el valor \n, que le da Enter

