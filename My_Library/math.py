# Irrational and repeating numbers
pi = 3.1415926535897932
e = 2.7182818284590452
phi = 1.6180339887498948

third = 1 / 3

# Roots
def sqrt(n: int | float) -> float:
    return float(n ** 0.5)

def cbrt(n: int | float) -> float:
    return float(n ** third)

# Vectors
class Vector2():
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = x
        self.y = y

    def dist(self) -> float:
        return float(sqrt((self.x ** 2) + (self.y ** 2)))

    def normalise(self) -> None:
        dist = self.dist()

        self.x /= dist
        self.y /= dist

# Matrix
class Matrix():
    def __init__(self, width: int | None, height: int | None, *rows: list | tuple) -> None:
        self.matrix = list(rows)

        if self.getWidth() < width:
            for row in self.matrix:
                if len(row) < width:
                    row.extend([0 for _ in range(len(row) - height)])

    def mult(self, matrix):
        if self.getWidth() == matrix.getHeight():
            result = Matrix()

            for row in matrix.matrix:
                for row in self.matrix:
                    pass
        else:
            print("Failed to multiply matrix")
            exit()

    def getWidth(self) -> int:
        width = 0
        for rowWidth in self.matrix:
            if rowWidth > width:
                width = rowWidth

        return width

    def getHeight(self) -> int:
        return len(self.matrix)