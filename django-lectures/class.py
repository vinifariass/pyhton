class Sample:
    pass


x = Sample()
print(type(x))


class Dog:
    # CLASS OBJECT ATTRIBUTE

    species = "Canis familiaris"

    # INSTANCE ATTRIBUTE
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"


my_dog = Dog("Buddy", 3)
print(my_dog)
other_dog = Dog("Max", 5)
print(other_dog)
print(my_dog.species)
print(other_dog.species)
print(my_dog.name)
print(other_dog.name)
print(my_dog.age)
print(other_dog.age)



