from Matrix3D import Matrix3D
from Solver import Solver
from Vector import Vector3D

filename = 'sle3D.txt'
a = Matrix3D()
b = Vector3D()

a.read_from_file(filename)
b.read_from_file(filename)

a.print()
b.print()
print()

s = Solver(a, b)
print(s.solve())
