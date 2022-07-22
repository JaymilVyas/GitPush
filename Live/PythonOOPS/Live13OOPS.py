class Person:
    def __init__(self, name, surname, emailid, year_of_birth):
        self.name1 = name
        self.surname1 = surname
        self.emailid1 = emailid
        self.year_of_birth1 = year_of_birth

    def age(self, current_year):
        return current_year - self.year_of_birth1

Jaymil = Person("Jaymil", "Vyas", "jaymilvyas@gmail.com", 1989)
Jimmy = Person("Jimmy", "Vyas", "Jimmy@gmail.com", 1994)
Breezana = Person("Breezana", "Vyas", "breezanavyas@gmail.com", 1993)
print(Jaymil.name1)
print(Jimmy.year_of_birth1)
print(Breezana.emailid1)
print(type(Jimmy))
print(Jimmy.name1 + " " + Jimmy.surname1)
print(Jaymil.age(2022))

class person:
    def age(self,current_year,year_of_birth):
        return current_year-year_of_birth

    def email_id_input(self,email_id):
        print("take and mail id from a person and print it ",email_id)

    def ask_name(self):
        name=input("tell me your name ")
        return name

    def ask_dob(self):
        dob=input("tell me your date of birth ")
        return dob

Jimmy=person()
Vyas=person()
Person1=person()
Person2=person()

Jimmy.email_id_input("jimmy@gmail.com")
print(Jimmy.ask_name())
