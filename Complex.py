class Complex:
    def __init__(self,re,im):
        self.__re = re
        self.__im = im

    def getRe(self):
        return self.__re

    def getIm(self):
        return self.__im

    def __add__(self,other):
        return Complex(self.__re + other.__re, self.__im + other.__im)

    def __sub__(self,other):
        return Complex(self.__re - other.__re, self.__im - other.__im)

    def __mul__(self, other):
        return Complex(self.__re*other.__re, self.__im*other.__im)

    def __truediv__(self,other):
        return Complex(self.__re / other.__re, self.__im / other.__im)

    def __abs__(self):
        return Complex(abs(self.__re), abs(self.__im))

    def __eq__(self, other):
        return Complex(self.__re == other.__re and self.__im == other.__im)

    def __ne__(self, other):
        return Complex(self.__re != other.__re)

    def __str__(self):
        return str(self.__re) + str(self.__im)

if __name__== '__main__':
   c1 = Complex(2, 5)
   c2 = Complex(3, 7)
   c3 = c1 + c2
   c4 = c1 - c2
   c5 = c1 * c2
   c6 = c1 / c2
   c7 = abs(c1)
   c8 = c1 == c2
   c9 = c1 != c2
   print(c3)
   print(c4)
   print(c5)
   print(c6)
   print(c7)
   print(c8)
   print(c9)
