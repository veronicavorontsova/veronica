# homework3.py

# 3 PRINT FUNCTIONS
 
def say_goodbye(name):
	print("Goodbye", name)

def area_of_circle(radius):
	print(3.14*radius**2)

# 4 RETURN FUNCTIONS

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a*b

def divide(a, b):
	return a/b

# 5 CONDITIONALS

def max_and_min_temp(readings):
	return (min(readings), max(readings))

def is_weekend(day):
	Monday = 1
	Tuesday = 2
	Wednesday = 3
	Thursday = 4
	Friday = 5
	Saturday = 6
	Sunday = 7 
	if day == 6 or day == 7: 
		return True
	else:
		return False 

def fuel_efficiency(distance, fuel):
	return distance/fuel 

def encrypt(num):
	last_digit = num % 10
	digits = num//10 
	return last_digit*(10**len(str(digits))) + digits  

# 6 LOOPS

def power(x, y):
	one = 1
	for i  in range (y):
		one*=x
	return one  

def minimum(nums):
	minimum = nums[0]
	for num in nums: 
		if num < minimum:
			minimum = num 
	return minimum 

def maximum(nums):
	maximum = nums[0]
	for num in nums:
		if num > maximum:
			maximum = num
	return maximum 

def mini(nums):
# mini short for minimum 
	minimum = nums[0]
# start with index 1 because we already assigned index 0 
	i = 1
	while i < len(nums): 
		if nums[i] < minimum:
			minimum = nums[i]
		i +=1 
	return minimum 

def maxi(nums):
# maxi short for maximum
	maximum = nums[0]
	i = 1
	while i < len(nums):
		if nums[i] > maximum:
			maximum = nums[i]
		i +=1
	return maximum


def summation(num):
	string_num = str(num) 
	summ = int(string_num[0])
	i = 1
	while i < len(string_num):
		summ += int(string_num[i])
		i +=1
	return summ		

# my favorite function is the encrypt function
num = 9999991
result = encrypt(num)

print(f"The result of encrypting the number {num} is {result}")
