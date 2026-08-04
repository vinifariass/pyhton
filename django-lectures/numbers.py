a =5
print(a )

a = a*5

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)
mystring = "hello"
print(mystring)

mylist =  ['a','b','c','d']
print(mylist[0])
mylist.append('e')
mylist.pop()
print(mylist)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[0][0])

first_col = [row[0] for row in matrix]
print(first_col)

for num in mylist:
    print(num)

for num in mylist:
    print(num)


    # Dictionary

    my_stuff = {'key1':'value1', 'key2':'value2','key3':{'123':[1,2,'grabMe']}}
    print(my_stuff['key3']['123'][2])

    #Boolean

    True or False

    #Tuples - immutable sequence of objects

    my_tuple = (1,2,3)
    print(my_tuple[0])

    #sets - unordered collection of unique elements

    my_set = set()
    my_set.add(1)
    my_set.add(2)
    my_set.add(3)
    print(my_set)

    #list comprehension

    my_list = [1,2,3,4,5]

s = 'django'
#print 'd'
print(s[0])
#print 'o'
print(s[-1])

#print 'djan'
print(s[:4])
#print 'jan'
print(s[4:])
#print 'go'
print(s[4:6])

#list comprehensions

my_list = [x for x in 'word']
print(my_list)

my_list = [x for x in range(0,11)]
print(my_list)

my_list = [x**2 for x in range(0,11)]
print(my_list)


#using keys and indexing, grabd the 'hello' string from the following dictionaries

d = {'simple_key':'hello'}
print(d['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Use print formatting to print the following string
print("Hello my dog's name is {a} and he is {b} years old".format(a='Rex', b=4))