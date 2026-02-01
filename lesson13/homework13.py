import numpy as np

print("===== NUMPY MATRIX & VECTOR TASKS =====")

# 1. Create a vector with values ranging from 10 to 49
v = np.arange(10, 50)
print("\n1) Vector 10..49:\n", v)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
m = np.arange(9).reshape(3, 3)
print("\n2) 3x3 matrix 0..8:\n", m)

# 3. Create a 3x3 identity matrix
identity = np.eye(3)
print("\n3) Identity matrix:\n", identity)

# 4. Create a 3x3x3 array with random values
arr3d = np.random.random((3, 3, 3))
print("\n4) 3x3x3 random array:\n", arr3d)

# 5. Create a 10x10 array with random values and find min & max
arr10 = np.random.random((10, 10))
print("\n5) 10x10 random array:\n", arr10)
print("Min value:", arr10.min())
print("Max value:", arr10.max())

# 6. Create a random vector of size 30 and find mean
v30 = np.random.random(30)
print("\n6) Random vector (30):\n", v30)
print("Mean value:", v30.mean())

# 7. Normalize a 5x5 random matrix
m5 = np.random.random((5, 5))
normalized = (m5 - m5.min()) / (m5.max() - m5.min())
print("\n7) Original 5x5 matrix:\n", m5)
print("Normalized matrix:\n", normalized)

# 8. Multiply a 5x3 matrix by a 3x2 matrix
A = np.random.random((5, 3))
B = np.random.random((3, 2))
product = A @ B
print("\n8) 5x3 * 3x2 product:\n", product)

# 9. Dot product of two 3x3 matrices
A = np.random.random((3, 3))
B = np.random.random((3, 3))
dot_product = np.dot(A, B)
print("\n9) Dot product (3x3 · 3x3):\n", dot_product)

# 10. Transpose of a 4x4 matrix
M4 = np.random.random((4, 4))
print("\n10) 4x4 matrix:\n", M4)
print("Transpose:\n", M4.T)

# 11. Determinant of a 3x3 matrix
M3 = np.random.random((3, 3))
det = np.linalg.det(M3)
print("\n11) 3x3 matrix:\n", M3)
print("Determinant:", det)

# 12. Matrix product A(3x4) and B(4x3)
A = np.random.random((3, 4))
B = np.random.random((4, 3))
print("\n12) A(3x4) · B(4x3):\n", A @ B)

# 13. Matrix-vector product
M = np.random.random((3, 3))
v = np.random.random((3, 1))
print("\n13) Matrix-vector product:\n", M @ v)

# 14. Solve Ax = b
A = np.random.random((3, 3))
b = np.random.random((3, 1))
x = np.linalg.solve(A, b)
print("\n14) Solution of Ax=b:\n", x)

# 15. Row-wise and column-wise sums
M = np.random.random((5, 5))
print("\n15) 5x5 matrix:\n", M)
print("Row sums:", M.sum(axis=1))
print("Column sums:", M.sum(axis=0))

print("\n===== DONE =====")
