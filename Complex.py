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

    def __truediv__(self,other):
        return Complex(self.__re / other.__re, self.__im / other.__im)

    def __abs__(self):
        return Complex((self.__re**2)**(1/2),(self.__im**2)**(1/2))

    def __eq__(self, other):
        return Complex(self.__re == other.__re and self.__im == other.__im)

    def __ne__(self, other):
        return Complex(self.__re != other.__re)

if __name__ == "__main__":
    c1 = Complex(1,2)
    c2 = Complex(2,1)
    c3 = Complex(-3,5)
    cadd = c1 + c2
    csub = c1 - c2
    cdiv = c1/c2
    c3abs = abs(c3)
    print("cadd(",str(cadd.getRe()),",",str(cadd.getIm()),")")
    print("csub(",str(csub.getRe()),",",str(csub.getIm()),")")


