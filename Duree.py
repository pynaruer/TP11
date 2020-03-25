class Duree:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        return (str(self.__hour)+"h"+str(self.__minute)+"m"+str(self.__second)+"s")

    def __add__(self, other):
        second = self.__second + other.__second
        minute = self.__minute + other.__minute + (second//60)
        hour = self.__hour + other.__hour   + (minute//60)
        return Duree(hour,minute%60,second%60)

heure1 = Duree(1,10,10)
heure2 = Duree(2,20,20)
print(heure1)
print(heure1+heure2)
