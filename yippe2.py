class Person():
    def __init__(self,person):
        self.person=person
    def talk(self):
        print(f"Blah Blah Blah my names {self.person}")# or for simpler conetext just say print("Blah Blah Blah")
person=Person("Tom Blair")
#print(person.person)
person.talk()
bob=Person("Bob Smith")
bob.talk()
