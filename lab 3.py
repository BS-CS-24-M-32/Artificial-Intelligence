# program 1
matching_numbers = []
for number in range(1500,2700):
    if number%7==0 and number%5==0:
        matching_numbers.append(number)
print("Numbers divisible by 7 and multiples of 5 are:")
print(matching_numbers)

# program 2
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter choice (1 or 2): ")
if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid choice!")

# program 3
import random
secret_number = random.randint(1, 9)
while True:
    guess = int(input("Guess a number between 1 to 9: "))

    if guess == secret_number:
        print("Well guessed!")
        break 

# program 4
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print() 

# program 5
word = input("Enter a word to reverse: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

# program 6
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1 
    else:
        odd_count += 1 
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

# program 7
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for item in datalist:
    print("Item:", item, " | Type:", type(item))

# program 8
for x in range(7):
    # Skip 3 and 6
    if x == 3 or x == 6:
        continue 
    print(x, end=" ")
print()

# program 9
a = 0
b = 1
while b <= 50:
    print(b, end=" ")
    a, b = b, a + b
print()

# program 10
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# program 11
# Get row and column counts from the user
m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))
grid = []
for i in range(m):
    row = []  
    for j in range(n):
        row.append(i * j)  
        
    grid.append(row)  
print(grid)

# program 12
lines = []
print("Enter lines of text (leave a line blank and press Enter to stop):")
while True:
    line = input()
    if line == "":
        break  
    lines.append(line.lower()) 
print("\nYour text in lowercase:")
for line in lines:
    print(line)

# program 13
user_input = input("Enter comma-separated binary numbers: ")
binary_list = user_input.split(",")
matching_numbers = []
for b in binary_list:
    decimal_value = int(b, 2)
    if decimal_value % 5 == 0:
        matching_numbers.append(b)

print("Output:", ",".join(matching_numbers))

# program 14
text = input("Enter a string: ")
letters_count = 0
digits_count = 0
for char in text:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1

print("Letters", letters_count)
print("Digits", digits_count)

# program 15
password = input("Enter your password to validate: ")

has_lower = False
has_upper = False
has_digit = False
has_special = False
special_characters = "$#@"
if len(password) < 6 or len(password) > 16:
    print("Invalid Password: Must be between 6 and 16 characters long.")
else:
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if has_lower and has_upper and has_digit and has_special:
        print("Valid Password!")
    else:
        print("Invalid Password: Missing required characters.")