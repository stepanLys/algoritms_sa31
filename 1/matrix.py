# -*- coding: utf-8 -*-

import numpy as np

first_matrix = np.random.random_integers(0, 10, (8, 8))
second_matrix = np.random.random_integers(0, 10, (8, 8))

for i in range(len(first_matrix)):
    for j in range(len(first_matrix[i])):
        if j % 2 != 0: first_matrix[i][j] = 0

print(first_matrix.itemsize*first_matrix.size)
# print(first_matrix)

# first_matrix = np.compress(2, first_matrix)

print(np.multiply(first_matrix,second_matrix))
print('Multiply\n' + str(first_matrix.dot(second_matrix)))
try:
    print('Divide\n' + str(first_matrix.dot(np.linalg.inv(second_matrix))))
except ValueError:
    print('Matrices must be square and of equal dimension')

try:
    print('Sum\n' + str(first_matrix + second_matrix))
except ValueError:
    print('Matrices must be of equal dimension')

try:
    print('Subtraction\n' + str(first_matrix - second_matrix))
except ValueError:
    print('Matrices must be of equal dimension')
