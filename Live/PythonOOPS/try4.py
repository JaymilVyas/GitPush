import try2
print(try2)

obj3=try2.person2("Jaymil","Vyas",1989)
print(obj3.yob2)

class person3:
    _name4="Jimmy"
    __surname4="Vyas"
    yob=1993

    def _age(self,cy):
        return cy-self.yob
    def __age1(self,cy):
        return cy-self.yob
obj=person3()
print(obj._age(2022))
print(obj._person3__age1(2022))

class employee(person3):
    _name4 = "Kian"
    __surname4 = "Jaymil"
    yob = 2021

obj1=employee()
print(obj1._age(2022))
print(obj1._person3__age1(2055))
print(obj1)
print(obj1.yob)
print(obj1._name4)
print(obj1._employee__surname4)