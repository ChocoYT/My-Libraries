from My_Library import math

myVector = math.Vector3(1, 1, 0)
myVector.normalise()

print(myVector.xyz)

myVector.rotateY(math.rad(45))

print(myVector.xyz)

'''

[a b c]
[d e f]
[g h i]

   *

  [j]
  [k]
  [l]

   =

[aj + bk + cl]
[dj + ek + fl]
[gj + hk + il]

- Dimensions = Height of A, Width of B
- Height of A = Width of B

- Dimensions = Width of A

'''
