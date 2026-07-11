# import matplotlib.pyplot as plt
# import numpy as np

# # ── The simplest plot ──────────────────────────────
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# plt.plot(x, y)
# plt.show()          # ← opens a window with the chart

import matplotlib.pyplot as plt
import numpy as np

# ── 1. Line plot — great for training loss curves ──
epochs = [1, 2, 3, 4, 5]
loss   = [0.9, 0.75, 0.6, 0.45, 0.3]
acc    = [0.4, 0.55, 0.68, 0.78, 0.88]

plt.figure(figsize=(10, 4))   # width=10, height=4

# Loss curve
plt.subplot(1, 2, 1)          # 1 row, 2 cols, plot 1
plt.plot(epochs, loss, color="red", marker="o", label="loss")
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

# Accuracy curve
plt.subplot(1, 2, 2)          # 1 row, 2 cols, plot 2
plt.plot(epochs, acc, color="green", marker="o", label="accuracy")
plt.title("Training Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)

plt.tight_layout()            # prevents overlapping
plt.show()

# ── 2. Bar chart — compare categories ─────────────
species  = ["setosa", "versicolor", "virginica"]
counts   = [50, 50, 50]

plt.figure(figsize=(6, 4))
plt.bar(species, counts, color=["blue", "orange", "green"])
plt.title("Iris Species Count")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()

# ── 3. Scatter plot — see relationships ────────────
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df  = pd.read_csv(url)

plt.figure(figsize=(7, 5))
colors = {"setosa": "blue", "versicolor": "orange", "virginica": "green"}

for species, group in df.groupby("species"):
    plt.scatter(group["petal_length"], group["petal_width"],
                label=species, color=colors[species])

plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.legend()
plt.grid(True)
plt.show()

# ── 4. Histogram — see data distribution ──────────
plt.figure(figsize=(7, 4))
plt.hist(df["petal_length"], bins=20, color="purple", edgecolor="black")
plt.title("Petal Length Distribution")
plt.xlabel("Petal Length")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


