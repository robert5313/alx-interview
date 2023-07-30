#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Create a function for def pascal_triangle(n):
    """
    triangle = []
    for i in range(1, n + 1):
        level = []
        K = 1
        for j in range(1, i + 1):
            level.append(K)
            K = K * (i - j)
        triangle.append(level)
    return triangle
