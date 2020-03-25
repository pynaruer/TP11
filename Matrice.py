import numpy as np

class Matrice:
    def __init__(self,data):
        self.__data = data

    def __str__(self):
        return str(self.__data)

    def __add__(self, other):
        return Matrice(self.__data + other.__data)

    def __iadd__(self, other):
        self.__data += other.__data

    def __sub__(self, other):
        return Matrice(self.__data - other.__data)

    def __isub__(self, other):
        self.__data -= other.__data

    def __mul__(self, other):
        return Matrice(np.dot(self.__data,other.__data))

    def __imul__(self, other):
        self.__data *= other.__data


m1 = Matrice(np.array([[1,0],[0,1]]))
m2 = Matrice(np.array([[1,1],[1,1]]))
print(m1)
print(m2)
print(m1 + m2)
print(m1 * m2)
