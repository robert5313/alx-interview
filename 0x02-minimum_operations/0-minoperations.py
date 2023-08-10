#!/usr/bin/python3
'''Module task 0.'''


def minOperations(n):
    '''Given a text file with a single character 'H', the task is to use only two operations - Copy All and Paste - to obtain n 'H' characters in the file. The objective is to find the minimum number of operations required to achieve this.
    '''
    if not isinstance(n, int):
    	return 0


    pk = 0
    i = 2
    while (i <= n):
        if not (n % i):
            n = int(n / i)
            pk += i
            i = 1
        i += 1
    return pk
