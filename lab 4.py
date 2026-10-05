# Initialize an empty stack
stack = []

# 1. Push
stack.append("Page 1")
stack.append("Page 2")
stack.append("Page 3")
print("Stack after pushes:", stack)

# 2. Peek
top_item = stack[-1]
print("Top item (Peek):", top_item)  

# 3. Pop
popped_item = stack.pop()
print("Popped item:", popped_item)   
print("Stack after pop:", stack)      

from collections import deque

# Initialize an empty queue
queue = deque()

# 1. Enqueue
queue.append("Customer A")
queue.append("Customer B")
queue.append("Customer C")
print("Queue after enqueues:", list(queue))  

# 2. Dequeue
served_customer = queue.popleft()
print("Served customer:", served_customer)   
print("Queue after dequeue:", list(queue))    

# Create an empty stack that can hold any type
mixed_stack = []

# Push different types of data onto the stack
mixed_stack.append(100)          # Integer
mixed_stack.append(45.67)        # Float
mixed_stack.append("Hello")      # String
mixed_stack.append(True)         # Boolean

print("Initial Mixed Stack:", mixed_stack)

# Pop
print("\n--- Popping Items ---")
while len(mixed_stack) > 0:
    item = mixed_stack.pop()
    print(f"Popped: {item:<8} | Type: {type(item).__name__}")

from collections import deque

# Create an empty queue that can hold any type
mixed_queue = deque()

# Enqueue
mixed_queue.append("User_01")    # String
mixed_queue.append(12)           # Integer
mixed_queue.append(98.6)         # Float
mixed_queue.append(False)        # Boolean

print("Initial Mixed Queue:", list(mixed_queue))

# Dequeue 
print("\n--- Dequeuing Items ---")
while len(mixed_queue) > 0:
    item = mixed_queue.popleft()
    print(f"Dequeued: {item:<8} | Type: {type(item).__name__}")

# Binary search
print()
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        # Find the middle position
        mid = (low + high) // 2
        
        # Check if the middle element is our target
        if sorted_list[mid] == target:
            return mid  # Found it! Return its index position
        
        # If target is smaller, ignore the right half
        elif sorted_list[mid] > target:
            high = mid - 1
            
        # If target is larger, ignore the left half
        else:
            low = mid + 1

    return -1  # Target was not found in the list

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target_number = 70

result = binary_search(my_list, target_number)

if result != -1:
    print(f"Success! Element found at index: {result}")
else:
    print("Element not found in the list.")

# Example with user input
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if sorted_list[mid] == target:
            return mid 
        elif sorted_list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Ask the user to type a number
user_input = input("Enter a number to search for: ")

try:
    target_number = int(user_input)
    
    result = binary_search(my_list, target_number)

    if result != -1:
        print(f"Success! Element {target_number} found at index: {result}")
    else:
        print(f"Element {target_number} was not found in the list.")

except ValueError:
    print("Invalid Input! Please run the program again and type a whole number (e.g., 50).")

# Reversing a string using stack
stack = []

# Input
string = input("Enter a string: ")

# 1. Push 
for char in string:
    stack.append(char)
 
# 2. Pop 
reversed_string = ""
while stack:
    popped_item = stack.pop()
    reversed_string += popped_item

print("The reversed string is:", reversed_string)
