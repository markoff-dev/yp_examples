def cache3(func):
    cache = {'count': 0, 'res': None}

    def exe():
        if 1 <= cache['count'] < 3:
            cache['count'] += 1
            return cache['res']

        cache['count'] = 1
        cache['res'] = func()
        return cache['res']

    return exe


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1

print(heavy())
print(heavy())
print(heavy())
