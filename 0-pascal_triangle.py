#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""
def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    triangle = []  # Initialize an empty list to hold the rows of the triangle
    for i in range(n):  # Loop through each level of the triangle
        row = [1] * (i + 1)  # Start with a row of 1's (length i + 1)
        for j in range(1, i):  # Loop through the indices of the current row
            # Calculate the value based on the two values above it in the previous row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)  # Add the constructed row to the triangle

    return triangle  # Return the completed triangle
