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
    

# Verifica que todas las filas tengan una longitud de 9
def verifyColumnLen(arraySudoku):
    for i in arraySudoku:
        if(len(i)!=9):
            return False
    return True

# Verifica que el sudoku sea de 9x9
def verifyLenSudoku(arraySudoku):
    if(len(arraySudoku)==9):
        if(verifyColumnLen(arraySudoku)):
            return True
    return False

# Validación de formato longitud de sudoku
print(verifyLenSudoku(arraySudoku))


    



