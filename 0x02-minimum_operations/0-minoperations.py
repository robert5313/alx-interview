#!/usr/bin/python3
'''Given a text file with a single character 'H', the task is to use only two operations - Copy All and Paste - to obtain n 'H' characters in the file. The objective is to find the minimum number of operations required to achieve this.
'''


def minOperations(n):
    i = 0
    minOperations = 2
    while n > 1:
        while n % minOperations == 0:
            i += minOperations
            n /= minOperations
        minOperations += 1
    return i
