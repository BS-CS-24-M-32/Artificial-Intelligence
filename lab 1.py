#different types of simple printing
print("Hello World!")
print(9)
print(5.5)
print(4,5,8)
print("apple", "banana", "fork")

#multi-line printing
print("""
This is line 1.
This is line 2.
This is line 3.
""")

# Custom separator (sep)
print("apple", "banana", "cherry", sep=", ")  

# Custom line ending (end) to keep the next print on the same line
print("Hello ", end="")
print("World!")  

# input and output
# 1. Standard text input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 2. Numerical input (requires conversion)
age = int(input("Enter your age: "))
years_to_one_hundred = 100 - age
print(f"You will turn 100 in {years_to_one_hundred} years.")

# 3. Floating point input
price = float(input("Enter the item price: "))
print("The final price is:", price)

# 4. Bool input
is_student = input("Are you a student? (yes/no): ")
print("Student status:", is_student)

#variable printing and different data types/type casting
# 1. String (str) - Text data
name = "Alice"
print(name, type(name))  
# string indices
print(name[3])
print(name[-3])
# string slicing
print(name[0:2])
print(name[3:-1])

# 2. Integer (int) - Whole numbers
age = 25
print(age, type(age))  

# 3. Float (float) - Decimal numbers
pi = 3.1415
print(pi, type(pi))  

# 4. Boolean (bool) - True or False
is_active = True
print(is_active, type(is_active)) 
# 5. List (list) - Ordered, mutable collection
scores = [85, 90, 78]
print(scores, type(scores))  

# 6. Dictionary (dict) - Key-value pairs
user = {"name": "Bob", "id": 101}
print(user, type(user))  

# 7. Complex
x = complex(1,2)
print(x, type(x))
y = 2+4J
print(y, type(y))

#creating lists
# str list
fruits = ["apple", "banana", "cherry", "mango"]
# Standard list print
print(fruits)
# Unpacked print
print(*fruits) 
# int list
int_list = [2,5,6,7]
print(int_list)
# float list
float_list = [2.3,5.7,2.5]
print(float_list)
# hybrid list
hybrid_list = ["red", 5, 2.4]
print(hybrid_list)
# empty list
empty_list = []
print (empty_list)
# list indices
print(fruits[2])
print(fruits[-1])
# list slicing
print(fruits[0:2])
print(fruits[0:-1])
print(fruits[:2])
print(fruits[:])

#multiple statements on a single line
a=1;b=2;c=3;print(a,b,c)

# conditional statements + indentation
# simple if + all relational operators
age = 20
if age >= 18:
    print("You are eligible to vote.") 
if age > 18:
    print("You are eligible to vote.")  
if age == 18:
    print("You are eligible to vote.") 
if age != 18:
    print("You are not eligible to vote.") 
if age < 18:
    print("You are not eligible to vote.") 
if age <= 17:
    print("You are not eligible to vote.") 
# if else
score = 45
if score >= 50:
    print("You passed!")
else:
    print("You failed.")  
# if else if
temperature = 25

if temperature > 30:
    print("It's hot outside.")
elif temperature >= 15:
    print("The weather is pleasant.") 
elif temperature > 0:
    print("It's cold outside.")
else:
    print("It's freezing!")
# nested if
has_ticket = True
is_vip = False

if has_ticket:
    if is_vip:
        print("Welcome to the front row!")
    else:
        print("Welcome to the general seating.")  
else:
    print("Please purchase a ticket first.")
# ternary operator
age = 16
status = "Adult" if age >= 18 else "Minor"
print(status) 
# match case
http_code = 404

match http_code:
    case 200:
        print("Success")
    case 404:
        print("Page Not Found")  
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status Code")  

# escape sequences
# new line
print("Hello\nWorld")
# horizontal tab
print("Name\tAge")
# backslash
print("C:\\Users\\Admin")
# single quote
print('It\'s a good day')
# double quotes
print("He said, \"Hi!\"")
# backspace
print("Python\bIsFun")
# carriage return
print("12345\rHello")