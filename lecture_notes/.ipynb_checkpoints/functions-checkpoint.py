# functions.py

# def function_name(some_input):
#    # python does stuff
#    return an_output

list1 = [40,80,10,30,50,20]

def minimum(list):
    return min(list)

print(minimum(list1))

list2 = [9390,9329,20]

print(minimum(list2))

def isprime(num):
    if num <= 0 or int!=type(num): 
        return "try again. choose a new number"
    else:
        if num == 1: 
            return "neither"
        elif num == 2:
            return "is a prime number"
        else: 
            if num % 2 ==0:
                return "composite number"
            else:
                for i in range(2, num):
                    if num % i ==0:
                        return "composite number"
                    else:
                        return "is a prime number"

print(isprime(3))