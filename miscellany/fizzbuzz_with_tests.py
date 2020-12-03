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


def assert_equal(result, expected):
    from sys import _getframe
    msg = 'Fail: expected {}, but received {} at line {}'

    if not result == expected:
        line = _getframe().f_back.f_lineno
        print(msg.format(result, expected, line))


if __name__ == '__main__':
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(4), '4')

    assert_equal(robot(3), 'fizz')
    assert_equal(robot(6), 'fizz')
    assert_equal(robot(9), 'fizz')

    assert_equal(robot(5), 'buzz')
    assert_equal(robot(10), 'buzz')
    assert_equal(robot(20), 'buzz')

    assert_equal(robot(15), 'fizzbuzz')
    assert_equal(robot(30), 'fizzbuzz')
    assert_equal(robot(45), 'fizzbuzz')
