#!/usr/bin/python3
""" Prime Game """


def is_winner(x, nums):
    # Initialize counters for Maria and Ben wins
    maria_wins_count = 0
    ben_wins_count = 0

    # Iterate over each number in the nums list
    for num in nums:
        # Create a set of rounds from 1 to the current number
        rounds_set = list(range(1, num + 1))
        
        # Generate a set of prime numbers within the range of 1 to the current number
        primes_set = primes_in_range(1, num)

        # If there are no prime numbers, increment Ben's win count and continue to the next number
        if not primes_set:
            ben_wins_count += 1
            continue

        # Variable to keep track of whose turn it is (Maria or Ben)
        is_maria_turns = True

        # Loop until there are no more prime numbers in the set
        while primes_set:
            # Remove the smallest prime number from the set
            smallest_prime = primes_set.pop(0)
            
            # Remove all multiples of the smallest prime from the rounds set
            rounds_set.remove(smallest_prime)
            
            # Filter out numbers from the rounds set that are divisible by the smallest prime
            rounds_set = [x for x in rounds_set if x % smallest_prime != 0]

            # Alternate turns between Maria and Ben
            is_maria_turns = not is_maria_turns

        # Update the win counts based on the result of the game
        if is_maria_turns:
            ben_wins_count += 1
        else:
            maria_wins_count += 1

    # Compare the win counts and determine the winner
    if maria_wins_count > ben_wins_count:
        return "Maria"
    elif maria_wins_count < ben_wins_count:
        return "Ben"
    else:
        return None

def is_prime(n):
    # Check if a number is prime
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    # Generate a list of prime numbers within a given range
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes

