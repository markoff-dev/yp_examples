from datetime import datetime


def dec(func):
    def wrapper():
        start = datetime.now()
        res = func()
        print(datetime.now() - start)
        return res

    return wrapper


@dec
def one(n, p):
    l = []
    for i in range(n):
        if i % p == 0:
            l.append(i)
    return l

@dec
def two(n, p, h, k):
    l = []
    for i in range(n):
        if i % p == 0:
            l.append(i)
    return l


one()