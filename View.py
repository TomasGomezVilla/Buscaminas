# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:53:25 2021

@author: tgome
"""


class View:
    def __init__(self):
        print("What's created View")

    def display(self,board):
        nrows,ncols = board.shape
        print (end="  ")
        
        for j in range(ncols):
            print(j, end=" ")
        print()

        for i in range(nrows):
            print(i, end=" ")
            for j in range (ncols):
                print("x ",end="")
            print()  #tiene por defecto el valor \n, que le da Enter
