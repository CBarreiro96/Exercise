#!/usr/bin/python3
"""
================================== Game Triqui =================================================
**** Information
- \t ------> Tabulator
- \n ------> Sapce
"""


class Triqui:
    """
    Implement class triqui
    """

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.mat = [] * (m + 1) # Create empty vector


    def printRowMatrix(self, message="Matrix whithout name:"):
        print("\n", message)
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                print(self.mat[i][j], "\t", end="")
            print()

    def play(self, row, column, piece):
        # If the position is zero, you can game
        if self.mat[row][column] == 0:
            self.mat[row][column] = piece
        else:
            print("square occupied")

    def evaluate_RowTriqui(self, piece):
        for i in range(1,self.m + 1):
            if self.mat[i][1] == piece and self.mat[i][2] == piece and self.mat[i][3] == piece:
                print("triqui en" + piece)
            else:
                pass

triqui=Triqui(3, 3)
triqui.printRowMatrix("Triqui")
