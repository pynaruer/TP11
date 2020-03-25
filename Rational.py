class Rational:
    def __init__(self,num,denum):
        self.__num = num
        self.__denum = denum

    def __str__(self):
        return (f"resultat: {self.__num} / {self.__denum}")

    def __add__(self, other):
        if self.__denum == other.__denum:
            return Rational(self.__num + other.__num,self.__denum)
        else:
            num = self.__num * other.__denum + other.__num * self.__denum
            denum = self.__denum * other.__denum
            return Rational(num,denum)

    def __sub__(self, other):
        if self.__denum == other.__denum:
            return Rational(self.__num - other.__num,self.__denum)
        else:
            num = self.__num * other.__denum - other.__num * self.__denum
            denum = self.__denum * other.__denum
            return Rational(num,denum)

    def __mul__(self, other):
        return Rational(self.__num*other.__num,self.__denum*other.__denum)

    def __truediv__(self, other):
        return Rational(self.__num*other.__denum,self.__denum*other.__num)

if __name__ == "__main__":
    r1 = Rational(1,2)
    r2 = Rational(3,4)
    print(r1 + r2)
    print(r1 - r2)
    print(r1 * r2)
    print(r1 / r2)
