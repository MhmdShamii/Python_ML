import numpy as np
import pandas as pd

# ── NumPy part ──────────────────────────────────────
# 1. Create a (60, 784) array of random floats between 0-1
#    (simulating 60 flattened MNIST images)
#    Print its shape

# 2. Normalize it — but this time the values are already 0-1
#    so instead multiply by 255 to go BACK to pixel values
#    Print the max and min to confirm (should be close to 255 and 0)

# 3. Reshape one image (row 0) from (784,) back to (28, 28)
#    Print its shape

# ── Pandas part ─────────────────────────────────────
# 4. Create a DataFrame with 5 students:
#    name, age, grade (A/B/C), score (any numbers you like)

# 5. Print only students with score above 80

# 6. Add a new column called "passed" 
#    True if score >= 60, False otherwise

# 7. Print the average score

mnist_images = np.random.rand(60, 784)
print(mnist_images.shape)

mnist_images *= 255
print(mnist_images.max(), mnist_images.min())

reshaped_image = mnist_images[0].reshape(28, 28)
print(reshaped_image.shape)

dataframe = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [20, 21, 19, 22, 20],
    'grade': ['A', 'B', 'C', 'A', 'B'],
    'score': [85, 78, 92, 88, 76]
})

print(dataframe[dataframe["score"]>80])

dataframe["passed"] = dataframe['score'] >= 60
print(dataframe)

print(dataframe["score"].mean())