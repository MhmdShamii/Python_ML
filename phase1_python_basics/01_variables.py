# === VARIABLES ===
name = "Ali"          # String
age = 22              # Integer
height = 1.75         # Float
is_student = True     # Boolean

# Python figures out the type automatically!
print(type(name))     # → <class 'str'>
print(type(age))      # → <class 'int'>

# 1. String
message = "Hello, Python!"
print(message.upper())        # → HELLO, PYTHON!
print(message.lower())        # → hello, python!
print(len(message))           # → 15

# 2. Integer & Float (math works as expected)
x = 10
y = 3
print(x + y)    # → 13
print(x / y)    # → 3.3333...  (always float in Python 3!)
print(x // y)   # → 3          (integer division)
print(x ** 2)   # → 100        (power/exponent)
print(x % 3)    # → 1          (modulo)

# 3. Boolean
print(10 > 5)   # → True
print(10 == 5)  # → False
print(10 != 5)  # → True

# f-strings — way cleaner than string concatenation
name = "Ali"
score = 98.5
print(f"Student: {name}, Score: {score}")
# → Student: Ali, Score: 98.5

# You can even do math inside!
print(f"Double the score: {score * 2}")
# → Double the score: 197.0

# Create 3 variables: your name, your age, and your favorite number. Then print a sentence using all three with an f-string.

name = "mhmd shami"
age = 22
favorite_number = 28

print(f"My name is {name}, i am {age} years old, and my fav number is {favorite_number}.")