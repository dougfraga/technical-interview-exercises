"""
Fizzbuzz rules

1. Multiple of 3: fizz
2. Multiple of 5: buzz
3. Multiple of 3 and 5: fizzbuzz
4. Other numbers: same number
"""
from functools import partial


def multiple_of(base, num):
    return num % base == 0


multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)


def robot(n):
    say = str(n)

    if multiple_of_3(n) and multiple_of_5(n):
        say = 'fizzbuzz'
    elif multiple_of_3(n):
        say = 'fizz'
    elif multiple_of_5(n):
        say = 'buzz'

    return say
