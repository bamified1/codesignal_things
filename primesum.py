import functools


def primes_sum(a, b):
    lst = [*range(a, b+1)]

    for n in lst:
        for i in range(2, int(b**0.5) + 1):
            if n == 1:
                lst.remove(n)
            if (n % i) == 0:
                lst.remove(n)
    return sum(lst)


def primes_sum2(a, b):
    return sum(list(sorted(set(range(a, b+1)).difference(set((p*f) for p in range(2, int(b**0.5) + 1)
                                                             for f in range(2, int(b/p) + 1))))))


def primes_sum3(a, b):
    return sum([n*f for i in [*range(a, b+1)]] for n in range(2, int(b**0.5) + 1)
               for f in range(2, int(b/n) + 1) if n % f == 0)


print(primes_sum3(1, 7))
