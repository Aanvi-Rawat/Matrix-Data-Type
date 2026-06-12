import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from matrix import Matrix

def test_creation():
    A = Matrix([[1, 2], [3, 4]])
    assert A.rows == 2
    assert A.cols == 2
    print("✅ test_creation passed")

def test_addition():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    result = A + B
    assert result == Matrix([[6, 8], [10, 12]])
    print("✅ test_addition passed")

def test_subtraction():
    A = Matrix([[5, 6], [7, 8]])
    B = Matrix([[1, 2], [3, 4]])
    result = A - B
    assert result == Matrix([[4, 4], [4, 4]])
    print("✅ test_subtraction passed")

def test_scalar_multiplication():
    A = Matrix([[1, 2], [3, 4]])
    assert A * 2 == Matrix([[2, 4], [6, 8]])
    assert 3 * A == Matrix([[3, 6], [9, 12]])
    print("✅ test_scalar_multiplication passed")

def test_matrix_multiplication():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    result = A @ B
    assert result == Matrix([[19, 22], [43, 50]])
    print("✅ test_matrix_multiplication passed")

def test_transpose():
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    result = A.transpose()
    assert result == Matrix([[1, 4], [2, 5], [3, 6]])
    print("✅ test_transpose passed")

def test_identity():
    I = Matrix.identity(3)
    assert I == Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print("✅ test_identity passed")

def test_zeros():
    Z = Matrix.zeros(2, 3)
    assert Z == Matrix([[0, 0, 0], [0, 0, 0]])
    print("✅ test_zeros passed")

def test_size_mismatch_addition():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[1, 2, 3]])
    try:
        _ = A + B
        print("❌ test_size_mismatch_addition failed (no error raised)")
    except ValueError:
        print("✅ test_size_mismatch_addition passed")

def test_size_mismatch_matmul():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[1, 2], [3, 4], [5, 6]])
    try:
        _ = A @ B
        print("❌ test_size_mismatch_matmul failed (no error raised)")
    except ValueError:
        print("✅ test_size_mismatch_matmul passed")

if __name__ == "__main__":
    print("Running tests...\n")
    test_creation()
    test_addition()
    test_subtraction()
    test_scalar_multiplication()
    test_matrix_multiplication()
    test_transpose()
    test_identity()
    test_zeros()
    test_size_mismatch_addition()
    test_size_mismatch_matmul()
    print("\nAll tests done!")
