# while loop
a=1
while(a<=5):
    a=a+1
    print("Hello World!")

# single statement while block
a=0
while(a==0):a=a+1;print("Hello World!")

# for loop
# iterating over a list
fruits = ["mango", "apple", "banana", "melon"]
for fruit in fruits:
    print(fruit)
# iterating over a tuple
fruits = ("mango", "apple", "banana", "melon")
for fruit in fruits:
    print(fruit)
# iterating over a string
for char in "Hello":
    print(char)
# using the range function
for i in range(5):
    print(i)
# specifying start and end range
for i in range(2,5):
    print(i)
# specifying start, stop, step
for i in range(1,6,2):
    print(i)

# loop control statements
for num in range(1,6):
    if num==3:
        continue
    if num==5:
        break
    print(num)

# creating a simple function
def simplef():
    print("Hello World!")
# calling a function
simplef()
# creating and calling a function with parameters and argumemnts
def greet(name):
    print (f"Helo,{name}!")
greet("Alice")
# function with defult parameters
def greet(name="Allen"):
    print (f"Helo,{name}!")
greet("Alice")
# creating and calling a function that returns data
def add(a,b):
    return a+b
total=add(5,2)
print(total)
# keyword arguments
def sub(a,b):
    return a-b
total=sub(b=2,a=6)
print(total)
# list as a parameter
def func(list):
    for item in list:
        print(f"Processing: {item}")
list1=["house", "cat", "plant", "devices"]
func(list1)

# class, objects and init function
class Car:                                     # defining a class
    def __init__(self, brand, model, year):    # the init function
# instance attribute
        self.brand=brand
        self.model=model
        self.year=year
# function inside a class
def display(self):
    return f"{self.year} {self.brand} {self.model}"
# creating instances
car1 = Car("Toyoyta", "Corolla", 2024)
car2 = Car("Tesla", "Model 3", 2026)
# accessing
print(car1.brand)
print(car2.display())

# insertion sort
def insertion_sort(arr):
    for i in range (1,len(arr)):
        key=arr[i]
        j=i-1
        while j>= 0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1] = key
# usage
nums = [5,2,8,1,3,6]
insertion_sort(nums)
print("Sorted array:",nums)