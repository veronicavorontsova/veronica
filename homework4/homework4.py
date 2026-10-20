# homework4.py

# LISTS

fav_foods = ["pizza", "grapes", "cookies", "yogurt", "steak"]

print(fav_foods[1])

print(fav_foods[-1])

fav_foods.append("cheese")

fav_foods.insert(0, "apple")

fav_foods.remove("grapes")
# or fav_foods.pop(2)

print(len(fav_foods))

for food in fav_foods:
    print(food.upper())

# I encountered this error: "NameError: name 'upper' is not defined"
# I originally wrote: print(upper(food)) instead of print(food.upper())

print(fav_foods[0:6:5])

if "potato" in fav_foods:
    print("A potato!")
else:
    print("No potato!")

# 3.2 SLICING AND STRIDING 

numbers = list(range(0, 21))
print(numbers)

# I encountered this error: "NameError: name 'numebrs' is not defined"
# I originally wrote: numebrs = range(0, 21) instead of numbers which was a spelling mistake

# 1

def get_first_15(nums):
    return nums[0:15]

print(get_first_15(numbers))
step1 = get_first_15(numbers)

# 2

def get_every_5th(nums):
    return nums[::5]

print(get_every_5th(step1))
step2 = get_every_5th(step1)

# 3

def reverse_and_stride(nums):
    numss = nums[::-1]
    return numss[::3]

print(reverse_and_stride(step2))
step3 = reverse_and_stride(step2)

# 3.3 NESTED LISTS 

NUMBERS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(NUMBERS[2])

print(NUMBERS[1][1])

NUMBERS.append([10, 11, 12])

def sum_nested(nums):
    total = 0
    for num in nums:
        total = total + sum(num)
    return total

print(sum_nested(NUMBERS))

print(sum_nested([[1, 2], [3, 4], [5, 6]]))

# 3.4 CREATE A 5x5 LIST 

def create_5x5_list():
    list = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1 
        list.append(row)
    return list 

print(create_5x5_list())

def multiples_of_3_in_5x5_list(fiveby5_list):
    list = []
    for i in fiveby5_list:
        row = []
        for j in i:
            if j % 3 == 0:
                row.append("?")
            else:
                row.append(j)
        list.append(row)
    return list 

print(multiples_of_3_in_5x5_list(create_5x5_list()))

def sum_of_questions(fiveby5_with_questions):
    total = 0
    for i in fiveby5_with_questions:
        for j in i:
            if j == "?":
                total += 1
    return total 

print(sum_of_questions(multiples_of_3_in_5x5_list(create_5x5_list())))

# 4 DICTIONARIES 

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])

ages["Mira"] = 100 

print(ages)

ages["Milana"] = 52

print(ages)

ages.pop("Mariam")

print(ages)

for name_and_age in ages:
    print(name_and_age, ages[name_and_age])

# favorite function of mine:
print(create_5x5_list())