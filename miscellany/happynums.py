def happy(n):
    next_ = sum(int(char) ** 2 for char in str(n))
    return n in (1, 7) if n < 10 else happy(next_)


assert all(happy(n) for n in (1, 10, 97, 100, 130))
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))
