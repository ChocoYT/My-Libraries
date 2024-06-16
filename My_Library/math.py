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

        self._update()

    def dist(self) -> float:
        return float(sqrt((self.x ** 2) + (self.y ** 2)))

    def normalise(self):
        dist = self.dist()

        self.x /= dist
        self.y /= dist

        return Vector2(self.x, self.y)

    def rotate(self, angle: int | float) -> None:
        oldAngle = matrices.dim2.rot.angle

        matrices.dim2.rot.angle = angle
        matrices.dim2.rot.update()

        matrix = Matrix([
            [self.x],
            [self.y],
            [1],
        ])
        rotatedMatrix = matrices.dim2.rot.matrix.mult(matrix)

        matrices.dim2.rot.angle = oldAngle
        matrices.dim2.rot.update()

        self.x, self.y, z = rotatedMatrix.matrix
        self._update()

    def _update(self) -> None:
        self.xx = self.x, self.x
        self.yy = self.y, self.y

        self.xy = self.x, self.y

class Vector3():
    def __init__(self, x: int | float, y: int | float, z: int | float) -> None:
        self.x = x
        self.y = y
        self.z = z

        self._update()

    def dist(self) -> float:
        return float(sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2)))

    def normalise(self) -> None:
        dist = self.dist()

        self.x /= dist
        self.y /= dist
        self.z /= dist
        
        return Vector3(self.x, self.y, self.z)

    def rotateX(self, angle: int | float) -> None:
        oldAngle = matrices.dim3.rotX.angle

        matrices.dim3.rotX.angle = angle
        matrices.dim3.rotX.update()

        matrix = Matrix([
            [self.x],
            [self.y],
            [self.z],
            [1],
        ])
        rotatedMatrix = matrices.dim3.rotX.matrix.mult(matrix)

        matrices.dim3.rotX.angle = oldAngle
        matrices.dim3.rotX.update()

        self.x, self.y, self.z, w = rotatedMatrix.matrix
        self._update()

    def rotateY(self, angle: int | float) -> None:
        oldAngle = matrices.dim3.rotY.angle

        matrices.dim3.rotY.angle = angle
        matrices.dim3.rotY.update()

        matrix = Matrix([
            [self.x],
            [self.y],
            [self.z],
            [1],
        ])
        rotatedMatrix = matrices.dim3.rotY.matrix.mult(matrix)

        matrices.dim3.rotY.angle = oldAngle
        matrices.dim3.rotY.update()

        self.x, self.y, self.z, w = rotatedMatrix.matrix
        self._update()

    def rotateZ(self, angle: int | float) -> None:
        oldAngle = matrices.dim3.rotZ.angle

        matrices.dim3.rotZ.angle = angle
        matrices.dim3.rotZ.update()

        matrix = Matrix([
            [self.x],
            [self.y],
            [self.z],
            [1],
        ])
        rotatedMatrix = matrices.dim3.rotZ.matrix.mult(matrix)

        matrices.dim3.rotZ.angle = oldAngle
        matrices.dim3.rotZ.update()

        self.x, self.y, self.z, w = rotatedMatrix.matrix
        self._update()

    def _update(self) -> None:
        self.xx = self.x, self.x
        self.xy = self.x, self.y
        self.xz = self.x, self.z
        self.xxx = self.x, self.x, self.x
        self.xxy = self.x, self.x, self.y
        self.xxz = self.x, self.x, self.z
        self.xyx = self.x, self.y, self.x
        self.xyy = self.x, self.y, self.y
        self.xyz = self.x, self.y, self.z
        self.xzx = self.x, self.z, self.x
        self.xzy = self.x, self.z, self.y
        self.xzz = self.x, self.z, self.z

        self.yx = self.y, self.x
        self.yy = self.y, self.y
        self.yz = self.y, self.z
        self.yxx = self.y, self.x, self.x
        self.yxy = self.y, self.x, self.y
        self.yxz = self.y, self.x, self.z
        self.yyx = self.y, self.y, self.x
        self.yyy = self.y, self.y, self.y
        self.yyz = self.y, self.y, self.z
        self.yzx = self.y, self.z, self.x
        self.yzy = self.y, self.z, self.y
        self.yzz = self.y, self.z, self.z

        self.zx = self.z, self.x
        self.zy = self.z, self.y
        self.zz = self.z, self.z
        self.zxx = self.z, self.x, self.x
        self.zxy = self.z, self.x, self.y
        self.zxz = self.z, self.x, self.z
        self.zyx = self.z, self.y, self.x
        self.zyy = self.z, self.y, self.y
        self.zyz = self.z, self.y, self.z
        self.zzx = self.z, self.z, self.x
        self.zzy = self.z, self.z, self.y
        self.zzz = self.z, self.z, self.z

# Matrix
class Matrix():
    def __init__(self, matrix: list | tuple, width: int = None, height: int = None, placeholder: int = 0) -> None:
        self.matrix = list(matrix)

        # Makes the matrix the correct width
        if (width != None) and (self.getWidth() < width):
            for i, row in enumerate(self.matrix):
                if len(row) < width:
                    self.matrix[i].extend([placeholder for _ in range(len(row) - width)])

        # Makes the matrix the correct height
        matHeight = self.getHeight()
        if (height != None) and (matHeight < height):
            for _ in range(height - matHeight):
                self.matrix.append([placeholder for _ in range(width)])

    def mult(self, matrix):
        aWidth = self.getWidth()
        bHeight = matrix.getHeight()

        if aWidth == bHeight:

            # Creates an empty matrix for adding numbers
            result = Matrix([], aWidth, bHeight).matrix

            # Simplify B for multiplying purposes
            for row, nums in enumerate(matrix.matrix):

                product = 1
                for num in nums:
                    product *= num
        
                matrix.matrix[row] = product

            # Adds the multiplied numbers to it
            for aY, aRow in enumerate(self.matrix):
                for aX, aNum in enumerate(aRow):

                    result[aY][aX] += aNum * matrix.matrix[aX]

            # Adds the lists together
            for row, nums in enumerate(result):
                for i, num in enumerate(nums):
                    if row != 0:
                        result[0][i] += num
            result = result[0]
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

class matrices:

    class dim2:

        class Rot():
            def __init__(self) -> None:
                self.angle = 0

                self.update()

            def update(self):
                self.matrix = Matrix([
                    [cos(self.angle), -sin(self.angle), 0],
                    [sin(self.angle),  cos(self.angle), 0],
                    [0,                0,               1],
                ])
        rot = Rot()

    class dim3:
        class RotX():
            def __init__(self) -> None:
                self.angle = 0

                self.update()

            def update(self):
                self.matrix = Matrix([
                    [1, 0,                0,               0],
                    [0, cos(self.angle), -sin(self.angle), 0],
                    [0, sin(self.angle),  cos(self.angle), 0],
                    [0, 0,                0,               1],
                ])
        rotX = RotX()

        class RotY():
            def __init__(self) -> None:
                self.angle = 0

                self.update()

            def update(self):
                self.matrix = Matrix([
                    [cos(self.angle),  0, sin(self.angle), 0],
                    [0,                1, 0,               0],
                    [-sin(self.angle), 0, cos(self.angle), 0],
                    [0,                0,               0, 1],
                ])
        rotY = RotY()

        class RotZ():
            def __init__(self) -> None:
                self.angle = 0

                self.update()

            def update(self):
                self.matrix = Matrix([
                    [cos(self.angle), -sin(self.angle), 0, 0],
                    [sin(self.angle),  cos(self.angle), 0, 0],
                    [0,               0,                1, 0],
                    [0,               0,                0, 1],
                ])
        rotZ = RotZ()
