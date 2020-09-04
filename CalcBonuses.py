import itertools


def calc_bonuses(bonuses, n):
    it = itertools.islice(bonuses, n)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res


print(calc_bonuses([4, 2, 4, 5], 3))
