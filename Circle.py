class Circle:
    def __init__(self,radius):
        self.__radius = radius

    def __add__(self, other):
        return Circle(self.__radius + other.__radius)

    def __lt__(self, other):
        return self.__radius < other.__radius

    def __gt__(self, other):
        return self.__radius > other.__radius

    def __str__(self):
        return str(self.__radius)

if __name__== '__main__':
   c1 = Circle(2)
   c2 = Circle(3)
   c3 = c1 + c2
   c4 = c1 < c2
   c5 = c2 > c3
   print(c3)
   print(c4)
   print(c5)
