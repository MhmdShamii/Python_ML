# # ── Basic function ─────────────────────────────────
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Mhmd"))   # → Hello, Mhmd!

# # ── Multiple parameters ────────────────────────────
# def add(a, b):
#     return a + b

# print(add(3, 5))       # → 8

# # ── Default parameters ─────────────────────────────
# def power(base, exponent=2):   # exponent defaults to 2
#     return base ** exponent

# print(power(3))        # → 9   (uses default exponent=2)
# print(power(3, 3))     # → 27  (overrides default)

# # ── Multiple return values ─────────────────────────
# # Python can return more than one value — very useful in ML!
# def min_max(numbers):
#     return min(numbers), max(numbers)

# low, high = min_max([4, 1, 9, 2, 7])
# print(low, high)       # → 1 9


# # This is EXACTLY the kind of function you'll write for MNIST
# def normalize(pixels):
#     """Takes a list of pixel values (0-255), returns them scaled to 0.0-1.0"""
#     return [round(p / 255, 2) for p in pixels]

# def count_bright(pixels, threshold=127):
#     """Count pixels above a brightness threshold"""
#     return sum(1 for p in pixels if p > threshold)

# def summarize(pixels):
#     """Print a summary of pixel data"""
#     print(f"Total pixels : {len(pixels)}")
#     print(f"Brightest    : {max(pixels)}")
#     print(f"Darkest      : {min(pixels)}")
#     print(f"Average      : {round(sum(pixels) / len(pixels), 2)}")

# # Use them:
# pixels = [245, 13, 128, 0, 255, 67, 189, 34]

# print(normalize(pixels))
# print(count_bright(pixels))
# summarize(pixels)


# Write 3 functions:

# 1. celsius_to_fahrenheit(c)
#    Formula: (c * 9/5) + 32
#    Test: celsius_to_fahrenheit(100) → 212.0

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(100))
# 2. normalize(pixels)
#    Takes a list, divides each value by 255, rounds to 2 decimals
#    Test: normalize([0, 128, 255]) → [0.0, 0.50, 1.0]

def normalize(pixels):
    return[round(pixel/255,2) for pixel in pixels]

print(normalize([0, 128, 255]))

# 3. summarize_scores(scores)
#    Takes a list of exam scores and prints:
#    "Highest: 100"
#    "Lowest : 45"
#    "Average: 77.57"
#    Test with: [88, 95, 72, 60, 100, 45, 83]

def summarize_scores(scores):
    print(f"Highest: {max(scores)}")
    print(f"Lowest : {min(scores)}")
    print(f"average: {round(sum(scores)/len(scores),2)}")
    
summarize_scores([88, 95, 72, 60, 100, 45, 83])