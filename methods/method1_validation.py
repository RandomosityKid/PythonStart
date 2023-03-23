class Person:
    def __init__(self, age):
        self._age = age
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print("Invalid age, cannot be negative number")
            self._age = 0
        else:
            self._age = value
            print("AgeSet: ", self._age)
        
        
person = Person(30)
print("1st age: ", person.age)
person.age = 40
print("2nd age: ", person.age)
person.age = -10
print("3rd age: ", person.age)