numbers = [1, 8, 3, 6, 5, 6, 7, 8]

##################################
def count(collection):
    counts = {}
    for elem in collection:
        if elem not in counts:
            counts[elem] = 0
        counts[elem] += 1
    return counts

# print(count(numbers))

##################################
def count_get(collection):
    counts = {}
    for elem in collection:
        counts[elem] = counts.get(elem, 0) + 1
    return counts

# print(count_get(numbers))

##################################
from collections import defaultdict


def count_defaultdict(collection):
    counts = defaultdict(int)
    for elem in collection:
        counts[elem] += 1
    return counts

# print(count_defaultdict(numbers))

##################################
from collections import Counter

# print(Counter(numbers))