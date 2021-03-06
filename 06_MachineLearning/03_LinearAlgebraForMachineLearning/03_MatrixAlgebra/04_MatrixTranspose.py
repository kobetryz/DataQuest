# page 23 in the hand written notes for context

import numpy as np

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

transpose_a = np.transpose(matrix_a)
transpose_b = np.transpose(matrix_b)

trans_ba = np.dot(transpose_b, transpose_a)
trans_ab = np.dot(transpose_a, transpose_b)

product_ab = np.dot(matrix_a, matrix_b)
product_ba = np.dot(matrix_b, matrix_a)

print('\nproduct_ab\n', product_ab)
print('\trans_ba\n', trans_ba)

print('\nproduct_ba\n', product_ba)
print('\ntrans_ab\n',trans_ab)