#!/usr/bin/python3
"""Module for 2D Matrix rotation """

def rotate_2d_matrix(matrix):
    """function that takes a matrix and rotates it 90 degrees"""
    n = len(matrix)

    for row in range(n // 2):
        for column in range(row, n - row - 1):
            curr_value = matrix[row][column]
            matrix[row][column] = matrix[n - 1 - column][row]
            matrix[n - 1 - column][row] = matrix[n - 1 - row][n - 1 - column]
            matrix[n - 1 - row][n - 1 - column] = matrix[column][n - 1 - row]
            matrix[column][n - 1 - row] = curr_value
