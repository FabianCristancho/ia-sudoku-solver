# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:16:14 2021

@author: 
    Andres Felipe Chaparro Rosas
    Fabian Alejandro Cristancho Rincón
    Óscar Esteban Quiroz López
"""

with open("sudoku.txt") as sudokuFile:
    arraySudoku = [line.split(" ") for line in sudokuFile]
    
print(arraySudoku)