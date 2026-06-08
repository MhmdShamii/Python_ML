# Creating a list
pixels = [255, 128, 64, 0, 200]
names  = ["cat", "dog", "bird"]
mixed  = [1, "hello", True, 3.14]   # Python allows mixed types

# ── Indexing (starts at 0, like most languages) ──
print(pixels[0])    # → 255   (first)
print(pixels[-1])   # → 200   (last — Python trick!)
print(pixels[-2])   # → 0     (second from last)

# ── Slicing ──
print(pixels[1:3])  # → [128, 64]   (index 1 up to but NOT including 3)
print(pixels[:2])   # → [255, 128]  (from start to index 2)
print(pixels[2:])   # → [64, 0, 200] (from index 2 to end)

# ── Useful methods ──
pixels.append(99)       # add to end      → [255, 128, 64, 0, 200, 99]
pixels.remove(128)      # remove by value → [255, 64, 0, 200, 99]
print(len(pixels))      # length          → 5
print(sum(pixels))      # sum all values  → useful in ML!
print(max(pixels))      # → 255
print(min(pixels))      # → 0


# You have this list of exam scores:
scores = [88, 95, 72, 60, 100, 45, 83]

# 1. Print the first and last score
print(scores[0])
print(scores[-1])
# 2. Print the highest and lowest score
print(max(scores))
print(min(scores))
# 3. Use a list comprehension to create a new list
#    where each score is divided by 100
#    (this is exactly what we do to normalize data in ML!)

divided = [x/100 for x in scores]

print(divided)