# 1. Syntax Error Fix
print("hi")  # Fixed the missing closing quotation mark

# 2. Runtime Error Fix
hello = "Hello, World!"
print(hello)  # Correctly prints the value of the variable 'hello'

# 3. Display a String Directly
print("Hello, World!")  # Directly displays the string

# 4. Display the Contents of a String Variable
greeting = "Hello, Python!"
print(greeting)  # Displays the contents of the string variable 'greeting'

# 5. Display a String with Single Quotes
print('Indian')  # Correctly displays a string using single quotes

# 6. Display a String with Double Quotes
print("Welcome to ABC")  # Correctly displays a string using double quotes

# 7. Read Two Numbers and Perform Operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_ = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else 'undefined'
reminder = num1 % num2 if num2 != 0 else 'undefined'
power = num1 ** num2
print(f"Sum: {sum_}, Difference: {difference}, Product: {product}, Quotient: {quotient}, Reminder: {reminder}, Power: {power}")

# 8. Check if num1 is an Integer
num1 = float(input("Enter a number: "))
is_integer = num1.is_integer()
print(f"Is num1 an integer? {is_integer}")

# 9. Convert to Integer
num1 = int(num1)
print(num1)  # Converts and prints num1 as an integer

# 10. Find Data Types
print(type(num1))
print(type(num2))

# 11. Read Float and Round to 2 Decimal Places
float_value = float(input("Enter a float value: "))
print(f"Rounded value: {round(float_value, 2)}")

# 12. Read Float and Print Absolute Value
float_value = float(input("Enter a float value: "))
print(f"Absolute value: {abs(float_value)}")

# 13. Store Different Types of Values
string_var = "Hello"
numeric_var = 123
complex_var = 1 + 2j
list_var = [1, 2, 3]
dict_var = {"key": "value"}
set_var = {1, 2, 3}
tuple_var = (1, 2, 3)

# 14. Find Data Type for Variables
print(type(string_var))
print(type(numeric_var))
print(type(complex_var))
print(type(list_var))
print(type(dict_var))
print(type(set_var))
print(type(tuple_var))

# 15. Count Letters in a String
greeting = "Welcome to Python Programming"
letter_count = len(greeting.replace(" ", ""))
print(f"Number of letters: {letter_count}")

# 16. Combine First and Last Name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
greeting_message = f"Hello, {full_name}!"
print(greeting_message)

# 17. Display String with Space
print(first_name + " " + last_name)  # Displays first and last names separated by a space

# 18. Display First Two Characters
name = first_name + " " + last_name
print(name[:2])  # Displays the first two characters of the full name

# 19. Display Last Three Characters
print(name[-3:])  # Displays the last three characters of the full name

# 20. Display 3rd Character to Last Character
print(name[2:])  # Displays from the 3rd character to the end of the full name

# 21. Display 3rd to 5th Character
print(name[2:5])  # Displays characters from the 3rd to the 5th

# 22. Create and Modify a List
food = ["Apple", "Banana"]
food.append("Cherry")
food.extend(["Date", "Elderberry"])
print(food)  # Displays the modified list

# 23. Count Number of Items in List
print(len(food))  # Counts the number of items in the 'food' list

# 24. Print the First Two Items Using Slicing Notation
print(food[:2])  # Prints the first two items in the list

# 25. Print the Last Item Using Index Notation
print(food[-1])  # Prints the last item in the list

# 26. Debug: Check if Number is Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# 27. Debug: Convert Centigrade to Fahrenheit
c = float(input("Enter temperature in Centigrade: "))
f = 9 * (c / 5) + 32
print("Temperature in Fahrenheit is: ", f)

# 28. Debug: Sum and Average of Numbers
count = int(input("Enter the count of numbers: "))
summ = 0
for i in range(count):
    x = int(input("Enter an integer: "))
    summ += x
avg = summ / count
print("The average is: ", avg)

# 29. Prove Mutability
# Strings are Immutable
s = "hello"
try:
    s[0] = 'H'
except TypeError as e:
    print(e)  # Strings do not support item assignment

# Lists are Mutable
l = [1, 2, 3]
l[0] = 10
print(l)  # Lists support item assignment
