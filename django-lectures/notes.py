if 1 < 2:
    print("first block")
    if 20 < 3:
        print("second block")

if 1 < 2:
    print("hello")
else:
    print("last")


x = 0
while x < 5:
    print(f"the current value of x is {x}")
    x += 1
else:
    print("x is not less than 5")


seq = [1, 2, 3, 4, 5]

for item in seq:
    print(item)

d = {"sam": 1, "frank": 2, "dan": 3}

for k in d:
    print(k)

x = [1, 2, 3, 4]
output = []
for num in x:
    output.append(num * 2)
print(output)

[num * 2 for num in x]


def my_func(name="default"):
    print(f"my function has been run! {name}")


my_func()
my_func("adam")


def hello():
    return "hello"


def addNum(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "Sorry! I need integers!"


result = addNum("1", 2)
print(result)

# Lambda Expression

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even_bool(num):
    return num % 2 == 0


filtered_list = filter(lambda num: num % 2 == 0, my_list)


# Filter
filtered_list = filter(even_bool, my_list)
print(list(filtered_list))


# Map
def mult_by2(num):
    return num * 2

    lambda num: num * 2


mapped_list = map(mult_by2, my_list)
print(list(mapped_list))

tweet = "Go Sports! #Sports"
result = tweet.strip("#")