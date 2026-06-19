class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError()
        if self.rows == 1:
            return self.data[0][0]
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

        det = 0
        for col in range(self.cols):
            minor = [row[:col] + row[col+1:] for row in self.data[1:]]
            minor_matrix = Matrix(minor)
            det += ((-1) ** col) * \
                self.data[0][col] * minor_matrix.determinant()

        return det

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError()

        other_transposed = list(zip(*other.data))

        result = []
        for row in self.data:
            new_row = list(map(
                lambda col: sum(a * b for a, b in zip(row, col)),
                other_transposed
            ))
            result.append(new_row)
        return Matrix(result)

    def transpose(self):
        return Matrix(list(map(list, zip(*self.data))))

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
print("Матрица 1:")
print(m1)
print(f"Определитель: {m1.determinant()}")
print("\nРезультат умножения:")
print(m1 * m2)
print("\nТранспонированная:")
print(m1.transpose())
