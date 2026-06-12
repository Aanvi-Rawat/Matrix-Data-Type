# 🧮 Matrix — Custom Data Type in Python

A custom `Matrix` data type built from scratch using Python OOP concepts.  
No external libraries. Just pure Python.

Built as a learning project while studying **operator overloading** and **dunder methods** in OOP.

---

## 📁 Project Structure

```
matrix-dt/
│
├── matrix.py               # The Matrix class (main file)
│
├── examples/
│   └── basic_usage.py      # Examples showing all features
│
├── tests/
│   └── test_matrix.py      # Tests for all operations
│
└── README.md
```

---

## 🚀 Getting Started

No installs needed. Just clone and run.

```bash
git clone https://github.com/your-username/matrix-dt.git
cd matrix-dt
python examples/basic_usage.py
```

---

## ✨ Features

| Operation | Symbol | Example |
|---|---|---|
| Addition | `+` | `A + B` |
| Subtraction | `-` | `A - B` |
| Scalar Multiply | `*` | `A * 3` or `3 * A` |
| Matrix Multiply | `@` | `A @ B` |
| Transpose | `.transpose()` | `A.transpose()` |
| Identity Matrix | `.identity(n)` | `Matrix.identity(3)` |
| Zero Matrix | `.zeros(r, c)` | `Matrix.zeros(2, 3)` |
| Size | `.size()` | `A.size()` |
| Equality | `==` | `A == B` |

---

## 📖 Usage

```python
from matrix import Matrix

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

# Print nicely
print(A)
# | 1  2 |
# | 3  4 |

# Addition
print(A + B)
# | 6   8  |
# | 10  12 |

# Scalar multiplication
print(A * 2)
# | 2  4 |
# | 6  8 |

# Matrix multiplication
print(A @ B)
# | 19  22 |
# | 43  50 |

# Transpose
C = Matrix([[1, 2, 3], [4, 5, 6]])
print(C.transpose())
# | 1  4 |
# | 2  5 |
# | 3  6 |

# Identity matrix
print(Matrix.identity(3))
# | 1  0  0 |
# | 0  1  0 |
# | 0  0  1 |
```

---

## 🧪 Running Tests

```bash
python tests/test_matrix.py
```

---

## 🧠 Concepts Covered

- Classes and objects
- `__init__`, `__str__`, `__repr__`
- Operator overloading (`__add__`, `__sub__`, `__mul__`, `__matmul__`)
- `__rmul__` for reverse operand support
- `__eq__` for equality checks
- Static methods (`@staticmethod`)
- Error handling with `ValueError`

---

## 📌 Requirements

- Python 3.6+
- No external libraries
