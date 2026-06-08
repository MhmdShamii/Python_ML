# ── for loop ──────────────────────────────────────
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry

# ── range() — loop N times ─────────────────────────
for i in range(5):
    print(i)        # → 0 1 2 3 4

for i in range(2, 8):
    print(i)        # → 2 3 4 5 6 7

for i in range(0, 10, 2):
    print(i)        # → 0 2 4 6 8  (step of 2)

# ── enumerate() — index + value together ───────────
# You'll use this ALL the time in ML
scores = [88, 95, 72, 60]

for i, score in enumerate(scores):
    print(f"Student {i}: {score}")
# Student 0: 88
# Student 1: 95
# Student 2: 72
# Student 3: 60

# ── while loop ─────────────────────────────────────
epoch = 1
while epoch <= 5:
    print(f"Training epoch {epoch}...")
    epoch += 1
# This is literally how neural network training loops work!

# You have pixel values from a grayscale image:
pixels = [245, 13, 128, 0, 255, 67, 189, 34]

# 1. ✅ correct — just needs indent inside the for
for i, pixel in enumerate(pixels):
    print(f"pixel {i}: {pixel}")   # ← 4 spaces indent

# 2. ✅ correct logic — if needs to be indented inside for
count = 0
for i in pixels:
    if i > 127:          # ← 4 spaces (no parentheses needed in Python!)
        count = count + 1   # ← 8 spaces (inside both for AND if)
print(f"we have {count} pixels with value > 127")

# 3. ✅ perfect — no changes needed
normalized = []
for pixel in pixels:
    normalized.append(round(pixel / 255, 2))
print(normalized)