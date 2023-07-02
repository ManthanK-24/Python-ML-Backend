# Tuple is like a list but we can't modify a tuple once declared
tup = (1,2,3)
li = [1,2,3]

# String is also like a tuple i.e immutable
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

#filter 
# A list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result)) #[1, 3, 5, 13]

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result)) #[0, 2, 8]


#map
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result)) #[2, 4, 6, 8]

#lambda
# This function can have any number of arguments but only one expression, which is evaluated and returned.
mx = lambda a, b : a if(a > b) else b
print(mx(1, 2))

# Immutable objects like tuples and strings can be deleted completely only

var = {"Geeks", "for", "Geeks"}
type(var) # set
#key in s	#containment check
#key not in s	#non-containment check
#s1 == s2	#s1 is equivalent to s2
#s1 != s2	#s1 is not equivalent to s2
#s1 <= s2	#s1 is subset of s2
#s1 < s2	#s1 is proper subset of s2
#s1 >= s2	#s1 is superset of s2
#s1 > s2	#s1 is proper superset of s2
#s1 | s2	#the union of s1 and s2
#s1 & s2	#the intersection of s1 and s2
#s1 – s2	#the set of elements in s1 but not s2
#s1 ˆ s2	#the set of elements in precisely one of s1 or s2

