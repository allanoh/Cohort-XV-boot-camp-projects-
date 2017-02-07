def FindPrime(number):
    """checks if the number is a prime number and returns true if it is."""

    if number <= 1:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False

    return True


