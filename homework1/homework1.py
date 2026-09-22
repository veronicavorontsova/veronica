# File: homework1.py

# --- Variables and Data Types ---

a = 10
print (a)
print (type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print (b)
print (type(b)) # b is a float, a number with decimals

c = 3j
print (c)
print (type(c)) # c is a complex number, a number with a real and imaginary part 

d = "hello"
print (d)
print (type(d)) # d is a string, a sequence of characters

e = [1, 2 , 3]
print (e)
print (type(e)) # e is a list, a collection of items

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print (f)
print (type(f)) # f is a dictionary, a collection of key-value pairs

g = (1, 2)
print (g)
print (type(g)) # g is a tuple, a collection of items that cannot be changed 

h = ["apple", "banana", "strawberry"]
print (h)
print (type(h)) # h is a list, a collection of items 

i = True
print (i)
print (type(i)) # i is a boolean, a value that can be either True or False 

j = None
print (j)
print (type(j)) # j is a NoneType, a special type that represents the absence of a value 

k = [True, "blue", 12]
print (k)
print (type(k)) # k is a list, a collection of items

l = str(14)
print (l)
print (type(l)) # l is a string, a sequence of characters 

m = 1e4
print (m)
print (type(m)) # m is a float, a number with decimals 

# Questions:
# 1) I found 9 different data types!
# 2) The data types I found are: int, float, complex, str, list, dict, tuple, bool, NoneType
# 3) b and m are both floats; d and l are both strings; e, h and k are all lists
# 4) The data type of l is a string. 
# It's not an integer because of the quotation marks around 14 and the function str(). 
# str() converts the integer 14 into a string. 
# 5) range is another data type:
n = range (10)
print (n)
print (type(n)) # n is a range, a sequence of numbers 

# --- Booleans ---

print (10 > 9) # True, 10 is greater than 9
print (10 == 9) # False, 10 is not equal to 9
print (10 <=9 ) # False, 10 is not less than or equal to 9 
print (bool("abc")) # True, non-empty string is True
print (bool(123)) # True, non-zero number is True
print (bool(["apple", "cherry", "banana"])) # True, non-empty list is True
print (bool(True)) # True, True is True
print (bool(False)) # False, False is False
print (bool(0)) # False, 0 is False
print (bool("")) # False, empty string is False
print (bool(" ")) # True, non-empty string is True; the space is a character 
print (bool(())) # False, empty tuple is False 
print (bool([])) # False, empty list is False
print (bool({})) # False, empty dictionary is False
print (bool(True and False)) # False, True and False is False
print (bool(True and True)) # True, True and True is True
print (bool(False and False)) # False, False and False is False
print (bool(True or False)) # True, True or False is True
print (bool(True or True)) # True, True or True is True
print (bool(False or False)) # False, False or False is False
print (bool(not(False))) # True, not False is True
print (bool(not(True))) # False, not True is False 

# Questions:
# 1) I saw the pattern that empty values/arguments and incorrect mathematical statements are False. 
# If it's non-empty and mathematically correct, it's True. 
# Additionally, contradicting statements like True and False are False.
# 2) I was most surprised about print (bool(0)) being False. Even though 0 is a number, it's considered empty by Python so it's False.
print (bool(2*5>2*4))
# 3)  print (bool(2*5>2*4)) is True because 2*5 is 10 and 2*4 is 8 and 10 is greater than 8, so the statement is mathematically correct. 
print (bool())
# 4) print (bool()) is False because it's an empty tuple. 

# --- Operators ---

# -- Arithmetic Operators --
print (10 + 5) # 15, performs addition
print (10 - 5) # 5, performs subtraction
print (2*4) # 8, performs multiplication
print (6/3) # 2.0, performs division
print (5%2) # 1, gives back the remainder
print (3**2)  # 9, takes to the power of (3 to the power of 2)
print (15//2) # 7, performs floor division; gives back the whole number of the division

# -- Comparison Operators --
print (5==2) # False, checks if a number is equal to another number
print (10 !=10) # False, checks if a number is not equal to another number 
print (2<5) # True, checks if a number is less than another number
print (12>5) #True, checks if a number is greater than another number 
print (5<=6) # True, checks if a number is less than or equal to another number
print (1>=10) # False, checks if a number is greater than or equal to antoher number 

# -- Assignments Operators --
x = 5
x += 5 # adds 5 to x, so x is now 10 
print(x) 
x -= 4 # subtracts 4 from x, so x is now 6
print (x) 
x *= 3 # multiplies x by 3, so x is now 18
print (x)

# -- Logical Operators --
# 1) and operator returns True if both statements are True; will return False is at least one statement is False 
print (True and True) # returns True
print (True and False) # returns False 
print (False and False) # returns False
# 2) or operator returns True if at least one statement is True; will return False if both statements are False
print (True or True) # returns True
print (True or False) # returns True
print (False or False) # returns False
# 3) not operator returns the opposite of the statement 
print (not False) # returns True 
print (not True) # returns False

# More Questions: 
# 1) / is the division operator while // is the floor division operator 
# 2) % is the operator that returns the remainder of a division operation while // is the floor divison 
# meaning it excludes the remainder and returns a whole number
# 3) To calculate the remainder when dividing two numbers you would use the % operator. 
print (56%6) # returns the remainder of 56 divided by 6 which is 2
# 4) Assignment operators are used to assign a variable to a value and/or reassign a variable to a new value using arithmetic operations. 

# --- Strings ---
my_string = "hello" 
print(my_string) # prints hello
print(my_string[0]) # prints h, the first character of the string
print(my_string[1]) # prints e, the second character of the string
print(my_string[2]) # prints l, the third character of the string
print(my_string[3]) # prints l, the fourth character of the string
print(my_string[4]) # prints o, the fifth character of the string
print(my_string[-1]) # prints o, the last character of the string
print(my_string[1:3]) # prints el, the second and fourth characters of the string
print(my_string[0:5:2]) # prints hlo
print(len(my_string))  # prints 5, the length of the string
print(my_string + "goodbye") # prints hellogoodbye, connects the words "hello" and "goodbye" together
print(my_string * 7) # prints hellohellohellohellohellohellohello, repeats the string (the word "hello") 7 times

# Questions:
# 1) Slicing is taking a string apart and selecting only a portion of its characters. For lines 156-163, I sliced the string. 
# 2)
name = "Oski"
print ("Hello, my name is", name) # prints Hello, my name is Oski; 
# prints the string "Hello, my name is" and prints the value of the variable name to the end of it. 
# 3)
name = "Oski"
print(f"Hello, my name is {name}") # print Hello, my name is Oski;
# prints the string "Hello, my name is" and prints the value of the variable name to the end of it.
# 4) The first print statement uses a comma to seperate the string and the variable, 
# while the second print statement uses an f-string to connect the string and variable together. 

# --- Terminal Commands ---

# cd
# Changes directories. Use it to move from one folder to another. 
# Example: cd Desktop 

# ls 
# Lists the files and folders in your current directory.
# Example: ls 

# ls -a
# Lists all files and folders in your current directory, including hidden files and folders.
# Example: ls -a

# mkdir 
# Creates a new directory 
# Example: mkdir python_decal_f26

# cat 
# Displays the contents of a file 
# Example: cat homework1.py

# pwd
# Shows the current directory you are in, and your pathway
# Example: pwd

# cd ..
# Returns you to the previous directory that you were in
# Example: cd ..

# cd . 
# Keeps you in the current directory 
# Example: cd . 

# cd ~
# Takes you back to your home directory 
# Example: cd ~

# cp 
# Copies files and directories from one location to another
# Example: cp homework1.py homework1duplicate.py

# mv
# Moves or renames files and directories 
# Example: mv homework1.py ~/Desktop/homework1duplicate.py

# rm 
# Permanently deletes files and directories
# Example: rm homework1duplicate.py

# clear
# Clears terminal screen 
# Example: clear 

# grep
# Searches for the lines with a specific string/text pattern in a file or multiple files 
# Example: grep "Oski" homework1.py

# Questions:
# 1) touch = creates a blank new file; 
# rm -rf = dangerous way of permanently deleting a folder and everything inside it;
# head [filename] = gives you the first 10 lines of a file 
# 2)  ls lists the files and folders in your current directory, 
# while ls-a (-a means all) lists the same thing as ls but includes hidden files and folders
# 3) A hidden file is a file or folder that is kept invisible so it's not accidentally deleted or changed. 
# A hidden file has a period at the start of it. 
# 4) -f means force, so it runs a command without asking for your confirmation first (makes it more risky); 
# -r means recursive, so it applies the command to the folder and everything inside the folder;
# -o means output, so it outputs the results of the command into a file rather than on the screen 
# Ex: you can use -f with rm to remove a file or directory without confirmation,
# Ex: you can use -r with rm to delete a folder and everything inside it
# Ex: you can use -o with curl to download the source code of a website and save it into a file
# curl = command that transfers data to or from a network server 