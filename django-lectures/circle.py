class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

        def area(self):
            return self.radius * self.radius * self.pi

        def set_radius(self, new_radius):
            self.radius = new_radius


myc = Circle(10)
print(myc.area())
myc.set_radius(20)
print(myc.area())


# INHERITANCE
class Animal:
    def __init__(self, name):
        self.name = name

    def whoAmI(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def whoAmI(self):
        print("I am a dog")


mya = Animal("Dog")
# SPECIAL METHODS
mylist = [1, 2, 3]
print(mylist)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    ## Two underscore special methods (string representation of the object)
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


mybook = Book("Python", "John Doe", 100)
print(mybook)

b = Book("Python", "John Doe", 100)
del b