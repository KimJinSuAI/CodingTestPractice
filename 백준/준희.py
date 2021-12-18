class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    @property
    def age(self):
        return self.__age
I = Person("james",15)
print(I.name)
print(I.age)