# Что быстрее напечатать одну длинную строку или много коротких?

import time

output_str = 'a' * 10000
start_time = time.time()
for _ in range(10000):
    print(output_str)
end_time = time.time()
many_print_time = end_time - start_time


long_str = (output_str + '\n') * 10000
start_time = time.time()
print(long_str)
end_time = time.time()
long_print_time = end_time - start_time

print(f'Many prints exec time: {many_print_time}')
print(f'Long print exec time: {long_print_time}')


