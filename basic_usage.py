from matrix import Matrix

# ── Creating Matrices ────────────────────────────────────────
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print("A =")
print(A)

print("\nB =")
print(B)

print(f"\nSize of A: {A.size()}")

# ── Addition ─────────────────────────────────────────────────
print("\nA + B =")
print(A + B)

# ── Subtraction ──────────────────────────────────────────────
print("\nA - B =")
print(A - B)

# ── Scalar Multiplication ────────────────────────────────────
print("\nA * 3 =")
print(A * 3)

print("\n2 * B =")
print(2 * B)

# ── Matrix Multiplication ────────────────────────────────────
print("\nA @ B =")
print(A @ B)

# ── Transpose ────────────────────────────────────────────────
C = Matrix([[1, 2, 3],
            [4, 5, 6]])

print("\nC =")
print(C)

print("\nTranspose of C =")
print(C.transpose())

# ── Identity Matrix ──────────────────────────────────────────
print("\n3×3 Identity Matrix =")
print(Matrix.identity(3))

# ── Zero Matrix ──────────────────────────────────────────────
print("\n2×3 Zero Matrix =")
print(Matrix.zeros(2, 3))

# ── Equality ─────────────────────────────────────────────────
X = Matrix([[1, 2], [3, 4]])
Y = Matrix([[1, 2], [3, 4]])
print(f"\nAre X and Y equal? {X == Y}")
