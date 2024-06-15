# Angle conversions
from math import radians as rad
from math import degrees as deg

# Trigonometric functions
from math import sin, cos, tan
from math import asin, acos, atan
from math import sinh, cosh, tanh
from math import asinh, acosh, atanh

# Irrational and repeating numbers
pi = 3.1415926535897932
e = 2.7182818284590452
phi = 1.6180339887498948

third = 1 / 3

# Rounding
def floor(n: int | float) -> int:
    if round(n) > n:
        n -= 1
    
    return round(n)

def ceil(n: int | float) -> int:
    if round(n) < n:
        n += 1

    return round(n)

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

class Vector3():
    def __init__(self, x: int | float, y: int | float, z: int | float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def dist(self) -> float:
        return float(sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2)))

    def normalise(self) -> None:
        dist = self.dist()

        self.x /= dist
        self.y /= dist
        self.z /= dist

# Matrix
class Matrix():
    def __init__(self, matrix: list | tuple, width: int = None, height: int = None, placeholder: int = 0) -> None:
        self.matrix = list(matrix)

        # Makes the matrix the correct width
        if width != None:
            if self.getWidth() < width:
                for i, row in enumerate(self.matrix):
                    if len(row) < width:
                        self.matrix[i].extend([placeholder for _ in range(len(row) - width)])

        # Makes the matrix the correct height
        if height != None:
            matrixHeight = self.getHeight()
            if matrixHeight < height:
                for _ in range(height - matrixHeight):
                    self.matrix.append([placeholder for _ in range(width)])

    def mult(self, matrix):
        if self.getHeight() == matrix.getWidth():

            result = [
                    [
                        sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*matrix.matrix)
                    ]   for A_row in self.matrix
                ]
        else:
            raise Exception("Failed to multiply matrix")

        return Matrix(result)

    def getWidth(self) -> int:
        width = 0
        for row in self.matrix:
            rowWidth = len(row)
            if rowWidth > width:
                width = rowWidth

        return width

    def getHeight(self) -> int:
        return len(self.matrix)
