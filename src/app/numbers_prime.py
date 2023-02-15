import random


def is_prime(x: int):
    if x == 2:
        return True
    else:
        return miller_rabin(x, 50)


def miller_rabin(n: int, k: int):  # miller-rabin
    if n < 2:
        return False

    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p

    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d / 2

    for i in range(k):
        x = pow(random.randint(2, n - 1), int(d), n)
        if x == 1 or x == n - 1:
            continue

        for r in range(1, s):
            x = (x * x) % n
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False

    return True


def get_next(n: int) -> int:
    n = n + 1
    x = lambda p: 0 if p == 1000000 else p if is_prime(p) else x(p + 1)
    return x(n)


def get_previous(n: int) -> int:
    n = n - 1
    x = lambda p: 0 if p == 2 else p if is_prime(p) else x(p - 1)
    return x(n)


def get_random_number() -> int:
    p = random.randint(2, 1000000)
    if is_prime(p):
        return p
    else:
        return get_previous(p)


def get_random_array(length: int) -> list[int]:
    return sorted((get_random_number() for i in range(length)))
