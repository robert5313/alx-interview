#!/usr/bin/python3
""" Making changes """

def makeChange(coins, total):
    """ Given a pile of coins of different values, determine the fewest
        number of coins needed to meet a given amount total.
        Return: fewest number of coins needed to meet total
    """

    if total <= 0:
        return 0
    list_check = 0
    test = 0
    coins.sort(reverse=True)
    for i in coins:
        while list_check < total:
            list_check += i
            test += 1
        if list_check == total:
            return test
        list_check -= i
        test -= 1
    return -1
