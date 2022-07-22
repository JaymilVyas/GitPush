class person2:
    def __init__(self,name,surname,yob):
        self._name2=name
        self.__surname2=surname
        self.yob2=yob

jimmy=person2("Jaymil","Vyas",1989)
print(jimmy._name2)
print(jimmy._person2__surname2)
