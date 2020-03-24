class Complex:
    def __init__(self,re,im):
        self.__re = re
        self.__im = im

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
        return (self.__re == other.__re) and (self.__im == self.__im)

    def __ne__(self, other):
        return (self.__re != other.__re) or (self.__im != other.__im)

    def __str__(self):
        return (str(self.__re) + str(self.__im) + " + i")

if __name__ == "__main__":
    c1 = Complex(1,2)
    c2 = Complex(3,4)
    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    print(c1 / c2)
    print(abs(c1))
    print(c1 == c2)
    print(c1 != c2)
