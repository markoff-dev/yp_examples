my_list = ['a', 'b', 'c', 'd', 'e', 'f']

# Плохо
for i in range(len(my_list)):
    print(i, my_list[i])

# Хорошо
for i, elem in enumerate(my_list):
    print(i, elem)