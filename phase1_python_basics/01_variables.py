# Lesson 1 — Variables & Data Types
# =====================================
# Run this file: python 01_variables.py

# --- Strings ---
name = "Ali"
print(type(name))         # <class 'str'>
print(name.upper())       # ALI
print(len(name))          # 3

# --- Integers & Floats ---
age = 22
height = 1.75

print(age + 1)            # 23
print(height * 2)         # 3.5
print(10 / 3)             # 3.3333 (always float in Python 3)
print(10 // 3)            # 3      (integer division)
print(2 ** 8)             # 256    (used a lot in ML for layer sizes)
print(10 % 3)             # 1      (modulo)

# --- Booleans ---
is_student = True
print(is_student)         # True
print(10 > 5)             # True
print(10 == 5)            # False
print(10 != 5)            # True

# --- f-strings (clean string formatting) ---
score = 98.5
print(f"Name: {name}, Age: {age}, Score: {score}")
print(f"Next year I'll be {age + 1}")

# ─────────────────────────────────────────
# 🧪 CHALLENGE: Fill in the blanks below
# Create your own name, age, favorite_number
# and print: "My name is ___, I am ___ years old,
#             and my favorite number is ___."
# ─────────────────────────────────────────

your_name = "..."         # replace with your name
your_age = 0              # replace with your age
favorite_number = 0       # replace with your favorite number

print(f"My name is {your_name}, I am {your_age} years old, and my favorite number is {favorite_number}.")
