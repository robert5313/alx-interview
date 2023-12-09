#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(num_rounds, sets_of_numbers):
    """
    Determines the winner of a set of prime number removal games.

    Args:
        num_rounds (int): The number of rounds.
        sets_of_numbers (list of int): A list of integers where each integer n denotes
        a set of consecutive integers from 1 up to n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben" or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    # Check for invalid input
    if num_rounds <= 0 or sets_of_numbers is None:
        return None
    if num_rounds != len(sets_of_numbers):
        return None
    # Initialize scores and array of possible prime numbers
    ben_score = 0
    maria_score = 0
    # Create a list 'possible_primes' of length max(sets_of_numbers) + 1 with all elements
    # initialized to 1
    possible_primes = [1 for _ in range(max(sets_of_numbers) + 1)]
    # The first two elements of the list, possible_primes[0] and possible_primes[1], are set to 0
    # because 0 and 1 are not prime numbers
    possible_primes[0], possible_primes[1] = 0, 0
    # Use Sieve of Eratosthenes algorithm to generate array of prime numbers
    for i in range(2, len(possible_primes)):
        remove_multiples(possible_primes, i)
    # Play each round of the game
    for num in sets_of_numbers:
        # If the sum of numbers in the set is even, Ben wins
        if sum(possible_primes[0:num + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    # Determine the winner of the game
    if ben_score > maria_score:
        return "Ben"
    if maria_score > ben_score:
        return "Maria"
    return None


def remove_multiples(prime_list, prime_num):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers.

    Args:
        prime_list (list of int): An array of possible prime numbers.
        prime_num (int): The prime number to remove multiples of.

    Returns:
        None.

    Raises:
        None.
    """
    # This loop iterates over multiples of a prime number and marks them as
    # non-prime by setting their corresponding value to 0 in the input
    # list prime_list. Starting from 2, it sets every multiple of prime_num up to the
    # length of prime_list to 0. If the index i * prime_num is out of range
    # for the list prime_list, the try block will raise an IndexError exception, and the loop will
    # terminate using the break statement.
    for i in range(2, len(prime_list)):
        try:
            prime_list[i * prime_num] = 0
        except IndexError:
            break
