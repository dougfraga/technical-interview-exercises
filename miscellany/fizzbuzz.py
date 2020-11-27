"""
Fizzbuzz rules

1. Multiple of 3: fizz
2. Multiple of 5: buzz
3. Multiple of 3 and 5: fizzbuzz
4. Other numbers: same number
"""
from functools import partial

multiple_of = lambda base, num: num % base == 0
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


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
