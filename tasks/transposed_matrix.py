"""
Транспонированная матрица
Краткий пример кода, который демонстрирует работу с матрицами и функцией zip
"""

import random

n = int(input())

matrix1 = [[random.randint(1,9) for _ in range(n)] for _ in range(n)]

print('\nМатрица1:')
for i in matrix1:
    print(' '.join(map(str, i)))

rotated = [list(row)[::-1] for row in zip(*matrix1)]

print('\nМатрица2:')
for i in rotated:
    print(' '.join(map(str, i)))






