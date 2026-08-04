# Given a list of ints, return True if the array contains a sequence of 1,2,3 anywhere in the list.
# 
# For example:
# arrayCheck([1, 1,2,3,1]) → True
# arrayCheck([1, 1,2,4,1]) → False
# arrayCheck([1,1,2,1,2,3]) → True

def arrayCheck(nums):
    # CODE GOES HERE
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

print(arrayCheck([1, 1,2,3,1]))
print(arrayCheck([1, 1,2,4,1]))
print(arrayCheck([1,1,2,1,2,3]))


def stringBits(str):
    result = ""
    for i in range(len(str)):
        if i%2 == 0:
            result += str[i]
    return result
## -- Problem 2 --
# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

# For example:

# stringBits("Hello") -> 'Hlo'
# stringBits("Hi") -> 'H'
# stringBits("Heeololeo") -> 'Hello'

def stringBits(str1):

    result = ""

    for i in range(len(str1)):
        if i%2 == 0:
            result += str1[i]
    return result