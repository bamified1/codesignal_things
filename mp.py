import functools


def math_practice(numbers):
    return functools.reduce(lambda x, y: (y[0], x[1]+y[1]) if x[0] % 2 == 0 else (y[0], x[1]*y[1]),
                            enumerate(numbers))[0]


print(math_practice([2, 8, 15]))
[[0] * x for x in reduce(lambda x, y: x+y, )]