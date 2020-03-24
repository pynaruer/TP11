class Complex:
    def __init__(self,re,im):
        self.__re = re
        self.__im = im

    def __add__(self,other):
        return Complex(self.__re + other.__re, self.__im + other.__im)

    def __sub__(self,other):
        return Complex(self.__re - other.__re, self.__im - other.__im)

    def __truediv__(self,other):
        return Complex(self.__re / other.__re, self.__im / other.__im)

    def __abs__(self):

    def __eq__(self, other):
        return Complex(self.__re == other.__re and self.__im == other.__im)

    def __ne__(self, other):
        return Complex(self.__re != other.__re)
