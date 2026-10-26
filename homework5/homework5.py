# homework5.py
'''
1) Git is the software that allows you to write code and track/save your changes, while GitHub is the online platform where you upload and send your code to. 
2) The terminal visually displays the output of the commands and instructions that are put into the command line.
3) A local repository is only on your computer and works offline, while a remote repository is shared with other computers along with your computer through networks like GitHub. 
4) Version control tracks and manages any changes that are done to your project files. 
5) The staging area is where you git add the changes you want to commit/save. 
6) git add starts tracking your changes and moves them to the staging area where they are prepared to be saved.
7) git commit saves the tracked changes that are in the staging area.
8) git push uploads local commits to GitHub or another remote server. 
9) git status tells you the state of your working directory and the staging area (what files are in it) 
10) git pull 
11) pwd shows your current working directory.
12) ls shows all the files in your current working directory.
13) cd allows you to move directories. 
14) nano allows you to edit a file. 
15) touch creates a new file.
16) mv moves a file or directory to another location and also renames it. 
17) rm permanently deletes a file.
18) cat shows the contents of a file. 
'''

# 2.2 A DIRECTORY TREE
'''
Questions 

1) pwd will tell you the current working directory.
2) ls will list all the files in your current working directory.
3) cd .. to move back to python_decal/, then cd brianna_repo, and then git pull to get the latest changes. 
4) mv homework.py ../judy_decal/homework/
5) cd ../judy_decal/homework
6) cat homework.py
7) git add . ; git commit -m "done with homework" ; git push origin main 
8) git pull origin main and then git push origin main. 
9) ~/recent/

'''
# 3 HOMEWORK 3 REVIEW 

# 3.1 DATA TYPES

def checkDataType(input):
    if type(input) == int:
        return 'int'
    if type(input) == float:
        return 'float'
    if type(input) == bool:
        return 'bool'
    if type(input) == str:
        return 'str'
    if type(input) == list:
        return 'list'
    if type(input) == dict:
        return 'dict'

print(checkDataType(3.14))
print(checkDataType(True)) 

# 3.2 CONDITIONALS

def evenOrOdd(int):
    if int%2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(evenOrOdd(7))
print(evenOrOdd(10))

# 4 LOOPS 

def sumWithLoop(nums):
    summation = 0
    for i in nums:
        summation = summation + i 
    return summation 

numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

# 5.1 LISTS

def duplicateList(list):
    duplicates = []
    for i in list:
        duplicates.append(i)
        duplicates.append(i)
    return duplicates 

list = ["a","b","c"]

print(duplicateList(list))

# 5.2 DEBUGGING

def square(num): 
    return num * num 

# a colon was missing after def square(num) which is why there was an error in the function 

# my favorite function from this problem set: 

print(duplicateList(["hello", "my", "name", "is", "veronica"]))