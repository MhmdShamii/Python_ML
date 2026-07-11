import matplotlib.pyplot as plt
import numpy as np

# 1. Plot your Phase 1 training simulator results!
#    Use these values:
epochs   = [1, 2, 3, 4, 5]
loss     = [0.8821, 0.7634, 0.6412, 0.5231, 0.4187]
accuracy = [0.4123, 0.5241, 0.6187, 0.7043, 0.8156]

#    Plot loss and accuracy side by side (subplot)
#    Add title, xlabel, ylabel, legend, grid to each

# plt.figure(figsize=(10, 4))
# plt.subplot(1, 2, 1)          # 1 row, 2 cols, plot 1
# plt.plot(epochs, loss, color="red", marker="o", label="loss")
# plt.title("Training Loss")
# plt.xlabel("Epoch")
# plt.ylabel("Loss")
# plt.legend()
# plt.grid(True)

# plt.subplot(1,2,2)
# plt.plot(epochs,accuracy,color="green",marker="o",label="accuracy")
# plt.title("Training accuracy")
# plt.xlabel("Epoch")
# plt.ylabel("accuracy")
# plt.legend()
# plt.grid(True)
# plt.show()

# 2. Create a bar chart showing the number of 
#    correct predictions per digit (make up the numbers):
digits      = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
correct     = [95, 98, 87, 82, 91, 78, 94, 96, 80, 88]

#    Add title: "MNIST Predictions per Digit"
#    xlabel: "Digit", ylabel: "Correct Predictions"

# plt.figure(figsize=(6,4))
# plt.bar(digits, correct, color=["blue", "orange", "green"])
# plt.title("MNIST Predictions per Digit")
# plt.xlabel("Digit")
# plt.ylabel("Correct Predictions")
# plt.show()

# 3. Plot a histogram of these pixel values:
pixels = np.random.randint(0, 256, size=1000)
#    bins=20, add title "Pixel Value Distribution"
#    This is exactly what you'll plot for MNIST images!

plt.figure(figsize=(7, 4))
plt.hist(pixels, bins=20, color="purple", edgecolor="black")
plt.title("Pixel Value Distribution")
plt.show()
