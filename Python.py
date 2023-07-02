# Tuple is like a list but we can't modify, tuple once declared
tup = (1,2,3)
li = [1,2,3]

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])
 
# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " + "3rd and 2nd last character: ")
print(String1[3:-2])

# Python Program to Update
# character of a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a character of the String
## As Python strings are immutable, they don't support item updation directly
### There are following two ways
#1
list1 = list(String1)
list1[2] = 'p'
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)

#2
String3 = String1[0:2] + 'p' + String1[3:]
print(String3)
