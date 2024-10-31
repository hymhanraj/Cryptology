#String Operations in Python 

# 1. Find the length of the string
str="hello_world!!"
print("str : ",str,"len(str) :",len(str)) 

# 2. Slice the string as per your choice
print ("str [1:2] : ",str[1:2]) 

# 3. Concatenate two strings 
str_2="goodbye"
print("str_1 : ",str,",str_2 ","str_1+str_2 : ",str + str_2)

# 4. Convert in to lower case in to uppercase character 
print("str :",str,"upper(str) :",str.upper())
str=str.upper()

# 5. Convert upper case into lower case characters
print("str :",str,"lower(str) :",str.lower())

# 6. convert the character into Unicode ( Ascii values)
print("str :",str_2,"ascii :")
for i in str:
    print(ord(i)," ")

# 7. convert Unicode into character
uni=72
print("unicode :",uni,"character :",chr(uni))

# 8. Check whether the given "substring" exists in the string
sub="hell"

print("str : ",str,"sub_str : ",sub,"is sub_str a substring of str :")
if sub in str:
    print("True")
else:
    print("False")

# 9. Replace the character 'k' with 'h'
str = "kali"
str_replaced = str.replace('k', 'h')
print("str : ", str, "str_replaced : ", str_replaced)

# 10. Pad the string with "x" at the end
str_padded = str.ljust(10, 'x')  # Pad with 'x' to make the length 10
print("str : ", str, "str_padded : ", str_padded)

# 11. Remove leading and trailing whitespace or specified characters from the string
str_with_whitespace = "   hello_world   "
str_trimmed = str_with_whitespace.strip()  # Remove leading and trailing whitespace
print("str_with_whitespace : '", str_with_whitespace, "'", "str_trimmed : '", str_trimmed, "'")

# 12. Split the given string into groups of five characters
def split_in_groups(s, group_size):
    return [s[i:i+group_size] for i in range(0, len(s), group_size)]

str_to_split = "abcdefghijklmnop"
groups = split_in_groups(str_to_split, 5)
print("str_to_split : ", str_to_split, "groups : ", groups)

# 13. Count the total number of words
str_with_words = "This is a sample string with several words."
word_count = len(str_with_words.split())
print("str_with_words : ", str_with_words, "word_count : ", word_count)

# 14. Find the frequency of each character in the string
from collections import Counter

str_for_freq = "aabbcc"
char_frequency = Counter(str_for_freq)
print("str_for_freq : ", str_for_freq, "char_frequency : ", char_frequency)

# STDIN and File operators
import os

# 15. Get the file name from the user
file_name = input("Enter the file name: ")

# 16. Check if the file exists or not
if os.path.exists(file_name):
    print("File exists.")
else:
    print("File does not exist.")

# Looping and File handling
# 17. Read the contents from the file
try:
    with open(file_name, 'r') as file:
        contents = file.read()
        print("File contents:\n", contents)
except FileNotFoundError:
    print("File not found.")

# 18. Reverse the contents from the file
try:
    with open(file_name, 'r') as file:
        contents = file.read()
        reversed_contents = contents[::-1]
        print("Reversed contents:\n", reversed_contents)
except FileNotFoundError:
    print("File not found.")

# 19. Write into the file
text_to_write = "This is some new text."
with open(file_name, 'w') as file:
    file.write(text_to_write)
print("Text written to file.")

# Math operations
import random

# 20. Convert Frequency into percentage
# Frequency already calculated in question 14

total_chars = sum(char_frequency.values())
percentages = {char: (count / total_chars) * 100 for char, count in char_frequency.items()}
print("Character percentages: ", percentages)

# 21. Perform modular arithmetic operation
a, b = 10, 3
modular_result = a % b
print("a % b : ", modular_result)

# 22. Find the prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

number_to_check = 7
print(f"{number_to_check} is prime: ", is_prime(number_to_check))
print("Prime numbers in range 1 to 20: ", prime_numbers_in_range(1, 20))

# 23. Check if the given two numbers are co-prime or not
def are_coprime(x, y):
    from math import gcd
    return gcd(x, y) == 1

num1, num2 = 14, 15
print(f"Are {num1} and {num2} co-prime? ", are_coprime(num1, num2))

# 24. Find the factors for the given number
def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

number = 28
factors = find_factors(number)
print(f"Factors of {number}: {factors}")

# 25. Generate 10 random numbers
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("Random numbers: ", random_numbers)

# 26. Explore: Miller-Rabin Test (pen and paper method)
# Note: Miller-Rabin Test is typically more complex and is usually implemented via code.
# Here's a simplified Python implementation for illustration:

def miller_rabin(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    def check(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not check(a):
            return False
    return True

number_to_test = 37
print(f"{number_to_test} is probably prime: ", miller_rabin(number_to_test))
