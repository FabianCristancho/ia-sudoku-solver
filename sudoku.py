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
    

# print sudoku
def printsudoku():
    print("\n\n\n\n\n")
    for i in range(len(arraySudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(arraySudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(arraySudoku[i][j])+" "
        print(line)

# ------------------------------- Validaciones -------------------------------------------
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


# Verifica si los elementos del sudoku son numéricos
def verifyArrayNumbers(arraySudoku):
    for i in arraySudoku:
        for j in i:
            try:
                int(j)
            except ValueError:
                return False
    return True


# Validación general del sudoku
def validateSudoku(arraySudoku):
    return verifyLenSudoku(arraySudoku) and verifyArrayNumbers(arraySudoku)

printsudoku()
print(validateSudoku(arraySudoku))
    



