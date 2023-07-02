# Tuple is like a list but we can't modify a tuple once declared
tup = (1,2,3)
li = [1,2,3]

# String is also like tuple i.e immutable
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

String1 = "\110\145\154\154\157"
print("\nPrinting in Octal with the use of Escape Sequences: ")
print(String1) #prints Hello
 
# Using raw String to
# ignore Escape Sequences
String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ")
print(String1) #Prints \110\145\154\154\157
 
# Printing Geeks in HEX
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(String1) #Prints This is Geeks in HEX
 
# Using raw String to
# ignore Escape Sequences
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1) #Prints \x47\x65\x65\x6b\x73 in \x48\x45\x58


# List is mutable
# To print elements from the beginning to a range use: print(lst[: Index])
# To print elements from end-use: print(lst[:-Index])
# To print elements from a specific Index till the end use: print(lst[Index:])
# To print the whole list in reverse order, use: print(lst[::-1]) 
