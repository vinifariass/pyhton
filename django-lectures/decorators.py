s = "GLOBAL VARIABLE"


def func():
    global s
    s = 50
    print(s)
    print(locals())
    print(globals())


func()
print(s)


def hello(name="jose"):
    print("The hello() function has been executed!")

    def greet():
        return "\t This is the greet() function inside hello!"

    def welcome():
        return "\t This is the welcome() function inside hello!"

    print(greet())
    print(welcome())
    print("I AM EXECUTING ANOTHER FUNCTION!")
    return greet()


hello()
result = hello()
print(result)


def other(func):
    print("Hello")
    return func()

print(other(hello))

def new_decorator(func):

    def wrap_func():
        print("CODE WOULD BE HERE, BEFORE EXECUTING THE FUNCTION")

        func()

        print("CODE WOULD BE HERE, AFTER EXECUTING THE FUNCTION")

    return wrap_func()

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")
