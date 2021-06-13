from datetime import datetime


def dec(arg):
    print(arg)

    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            res = func(*args, **kwargs)
            print(datetime.now() - start)
            return res

        return wrapper

    return outer


@dec('name')
def one(n, p):
    l = []
    for i in range(n):
        if i % p == 0:
            l.append(i)
    return l


@dec('name')
def two(n, p, h, k):
    l = []
    for i in range(n):
        if i % p == 0:
            l.append(i)
    return l

# one(10, 2)