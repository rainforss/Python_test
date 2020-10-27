def count_primes(number):
    count = 0
    numlist = list(range(number + 1))
    for num in numlist:
        if notPrime(num):
            count += 1
    return number + 1 - count


def notPrime(number):
    if number < 2:
        return True
    if number == 2:
        return False
    if number > 2:
        denominator_list = list(range(2, number))

        for denominator in denominator_list:
            if number % denominator == 0:
                return True
    return False


import string


def ispangram(string, alphabet=string.ascii_lowercase):
    normalized = string.lower()
    alphabet = list(alphabet)
    for letter in normalized:
        if alphabet.count(letter) != 0:
            alphabet.remove(letter)
    return len(alphabet) == 0


print(ispangram("The quick brown fox jumps over the lazy "))

