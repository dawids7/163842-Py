1.
def find_numbers():
    numbers = []

    for num in range(1500, 2701):
        if num % 7 == 0 and num % 5 == 0:
            # If yes, add it to the list
            numbers.append(num)

    return numbers

result = find_numbers()
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700:")
print(result)

2.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temperature_celsius = 25
temperature_fahrenheit = 77

converted_to_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
converted_to_celsius = fahrenheit_to_celsius(temperature_fahrenheit)

print(f"{temperature_celsius} Celsius is equal to {converted_to_fahrenheit:.2f} Fahrenheit.")
print(f"{temperature_fahrenheit} Fahrenheit is equal to {converted_to_celsius:.2f} Celsius.")

3.
import random

def guess_number():
    target_number = random.randint(1, 9)

    while True:
        guess = int(input("Guess a number between 1 and 9: "))

        if guess == target_number:
            print("Well guessed!")
            break  # Exit the loop if the guess is correct
        else:
            print("Try again!")

guess_number()

4.
max_asterisks = 5

for i in range(max_asterisks + 1):
    print('* ' * i)

for i in range(max_asterisks - 1, 0, -1):
    print('* ' * i)

5.
word = input("Enter a word: ")

reversed_word = word[::-1]

print("Reversed word:", reversed_word)

6.
numbers = input("Enter a series of numbers separated by spaces: ")

numbers_list = numbers.split()

even_count = 0
odd_count = 0

for num in numbers_list:
    if int(num) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

7.
my_list = [1, 'hello', 3.14, True, [5, 6, 7]]

for item in my_list:
  print(f"Item: {item}, Type: {type(item)}")

8.
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i)

9.
a, b = 0, 1

print(a)

while b < 50:
    print(b)
    a, b = b, a + b

10.
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

11.
def generate_array(rows, columns):
    return [[i * j for j in range(columns)] for i in range(rows)]

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

result = generate_array(rows, columns)

for row in result:
    print(row)

12.
def print_lines():
    lines = []
    while True:
        line = input("Enter a line (blank line to terminate): ")
        if not line:
            break
        lines.append(line.lower())
    
    for line in lines:
        print(line)

print_lines()

13.
def divisible_by_5(binary_numbers):
    divisible_numbers = []
    for num in binary_numbers:
        decimal_num = int(num, 2)
        if decimal_num % 5 == 0:
            divisible_numbers.append(num)
    return divisible_numbers

binary_input = input("Enter comma separated 4-digit binary numbers: ").split(',')
divisible_numbers = divisible_by_5(binary_input)
print("Numbers divisible by 5:", ','.join(divisible_numbers))

14.
def count_digits_and_letters(string):
    num_digits = 0
    num_letters = 0
    for char in string:
        if char.isdigit():
            num_digits += 1
        elif char.isalpha():
            num_letters += 1
    return num_digits, num_letters

input_string = input("Enter a string: ")
digits, letters = count_digits_and_letters(input_string)
print("Number of digits:", digits)
print("Number of letters:", letters)

15.
import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    if not re.search("[$#@]", password):
        return False
    
    return True

password = input("Enter a password: ")
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")

16.
result = []

for num in range(100, 401):
    digits = [int(d) for d in str(num)]  # Convert number to list of digits
    if all(digit % 2 == 0 for digit in digits):
        result.append(str(num))

print(",".join(result))

17.
def print_pattern_A():
    for row in range(6):
        for col in range(7):
            if (col == 0 or col == 6) and row != 0 or (row == 0 or row == 3) and (col > 0 and col < 6):
                print("*", end="")
            else:
                print(end=" ")
        print()


print_pattern_A()

18.
def print_pattern_D():
    for row in range(7):
        for col in range(7):
            if (col == 0) or (col == 6 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 6)):
                print("*", end="")
            else:
                print(end=" ")
        print()


print_pattern_D()

19.
def print_pattern_E():
    for row in range(7):
        for col in range(7):
            if (col == 0) or (row == 0 or row == 3 or row == 6):
                print("*", end="")
            else:
                print(end=" ")
        print()


print_pattern_E()

20.
def print_pattern_G():
    pattern = ""
    for row in range(7):
        for col in range(6):
            if ((col == 0 or col == 6) and (row > 0 and row < 6)) or ((row == 0 or row == 6) and (col > 0 and col < 6)) or (row == 3 and (col > 1 and col < 6)) or (col == 5 and (row > 2 and row < 6)) or (col == 1 and (row > 4)):
                pattern += "*"
            else:
                pattern += " "
        pattern += "\n"
    print(pattern)


print_pattern_G()
