class Matrix:
    """
    A custom Matrix data type built using Python OOP.
    Supports addition, scalar multiplication, matrix multiplication, and transpose.
    """

    def __init__(self, data):
        """
        Create a Matrix from a list of lists.

        Args:
            data (list): A 2D list of numbers e.g. [[1, 2], [3, 4]]
        """
        if not data or not data[0]:
            raise ValueError("Matrix data cannot be empty.")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __str__(self):
        """Print the matrix in a readable grid format."""
        rows = []
        for row in self.data:
            rows.append("| " + "  ".join(str(x) for x in row) + " |")
        return "\n".join(rows)

    def __repr__(self):
        return f"Matrix({self.data})"

    def __add__(self, other):
        """Add two matrices together (must be the same size)."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Cannot add {self.rows}×{self.cols} and {other.rows}×{other.cols} matrices. Sizes must match."
            )
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        """Subtract one matrix from another (must be the same size)."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Cannot subtract {self.rows}×{self.cols} and {other.rows}×{other.cols} matrices. Sizes must match."
            )
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, factor):
        """Multiply matrix by a scalar (a single number)."""
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] * factor)
            result.append(row)
        return Matrix(result)

    def __rmul__(self, factor):
        """Allows both A * 2 and 2 * A to work."""
        return self.__mul__(factor)

    def __matmul__(self, other):
        """
        Matrix multiplication using the @ operator (e.g. A @ B).
        Columns of A must equal rows of B.
        """
        if self.cols != other.rows:
            raise ValueError(
                f"Cannot multiply {self.rows}×{self.cols} by {other.rows}×{other.cols}. "
                f"Columns of first matrix must equal rows of second."
            )
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)

    def __eq__(self, other):
        """Check if two matrices are equal."""
        return self.data == other.data

    def transpose(self):
        """Flip rows and columns of the matrix."""
        result = []
        for j in range(self.cols):
            row = []
            for i in range(self.rows):
                row.append(self.data[i][j])
            result.append(row)
        return Matrix(result)

    def size(self):
        """Return the size of the matrix as a string e.g. '3×3'."""
        return f"{self.rows}×{self.cols}"

    @staticmethod
    def identity(n):
        """
        Create an n×n identity matrix (1s on diagonal, 0s elsewhere).

        Args:
            n (int): Size of the matrix

        Returns:
            Matrix: n×n identity matrix
        """
        data = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(1 if i == j else 0)
            data.append(row)
        return Matrix(data)

    @staticmethod
    def zeros(rows, cols):
        """Create a matrix filled with zeros."""
        return Matrix([[0] * cols for _ in range(rows)])
