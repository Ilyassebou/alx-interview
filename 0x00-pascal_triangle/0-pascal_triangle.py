#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    tri = []

    if n <= 0:
        return []

    for i in range(n):
        if (i == 0):
            tri.append([1])
        else:
            row = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    row.append(1)
                else:
                    row.append(tri[i - 1][j - 1] +
                                   tri[i - 1][j])

            tri.append(row)

    return (tri)
