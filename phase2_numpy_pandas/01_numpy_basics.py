import numpy as np

# pixels = np.array([100, 200, 150, 80])
# print(pixels / 255)

# # ── 1D array ───────────────────────────────────────
# a = np.array([1, 2, 3, 4, 5])
# print(a)            # → [1 2 3 4 5]
# print(a.shape)      # → (5,)
# print(a.dtype)      # → int64

# # ── 2D array (matrix) ──────────────────────────────
# image = np.array([[255, 128, 64],
#                   [32,  16,  8],
#                   [200, 100, 50]])

# print(image.shape)  # → (3, 3)
# print(image.ndim)   # → 2
# print(image.size)   # → 9  (total elements)

# # ── Indexing ───────────────────────────────────────
# print(image[0])         # → first row:     [255 128  64]
# print(image[0][1])      # → row 0, col 1:  128
# print(image[0, 1])      # → same thing:    128
# print(image[:, 0])      # → first column:  [255  32 200]
# print(image[0:2, 0:2])  # → top-left 2x2:  [[255 128] [32 16]]

# # ── Math — no loops! ───────────────────────────────
# print(image + 10)       # adds 10 to every element
# print(image * 2)        # multiplies every element by 2
# print(image / 255)      # normalizes every element to 0.0-1.0

# # ── Useful array creators ──────────────────────────
# print(np.zeros((3, 3)))       # 3x3 of zeros
# print(np.ones((2, 4)))        # 2x4 of ones
# print(np.arange(0, 10, 2))    # → [0 2 4 6 8]
# print(np.linspace(0, 1, 5))   # → [0.   0.25 0.5  0.75 1.  ]

# # ── Stats ──────────────────────────────────────────
# print(np.sum(image))    # sum of all elements
# print(np.mean(image))   # average
# print(np.max(image))    # → 255
# print(np.min(image))    # → 8
# print(np.std(image))    # standard deviation


# # 1. Create a 5x5 matrix of random integers between 0 and 255
# #    (simulating a tiny grayscale image)
# #    Print its shape, size, and dtype
# #    Hint: np.random.randint(0, 256, size=(5, 5))

# image = np.random.randint(0, 255, size=(5, 5))

# print(image)

# print(image.shape)
# print(image.size)
# print(image.dtype)

# # 2. From that matrix:
# #    - Print the entire first row
# #    - Print the entire last column  ← hint: matrix[:, -1]
# #    - Print the center 3x3 section  ← hint: matrix[1:4, 1:4]

# print(image[0])
# print(image[:, -1])
# print(image[1:4,1:4])

# # 3. Normalize the entire matrix to 0.0–1.0 (divide by 255)
# #    Then confirm:
# #    print(normalized.max())   # → 1.0  (maybe, depends on random values)
# #    print(normalized.min())   # → 0.0  (maybe)

# normalized = image /255

# print(normalized)
# print(normalized.max())
# print(normalized.min())

# # 4. Create this matrix manually:
# #    [[1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9]]
# #    Print sum of each ROW    → [ 6 15 24]
# #    Print sum of each COLUMN → [12 15 18]
# #    Hint: np.sum(matrix, axis=1) vs np.sum(matrix, axis=0)

# matrix =[[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]

# print(np.sum(matrix,axis=1))
# print(np.sum(matrix,axis=0))


# # import numpy as np

# # # A 1D array of numbers 1 to 12
# # a = np.arange(1, 13)
# # print(a)          # → [ 1  2  3  4  5  6  7  8  9 10 11 12]
# # print(a.shape)    # → (12,)

# a = np.arange(1, 13)
# print(a)          # → [ 1  2  3  4  5  6  7  8  9 10 11 12]
# print(a.shape)    # → (12,)

# # Reshape into 3 rows, 4 columns
# b = a.reshape(2, 6)
# print(b)
# print(b.flatten())    # → (3, 4)

# 1. Create a 1D array of numbers 1–12
#    Reshape it into a 3x4 matrix
#    Then reshape again into a 2x6 matrix
#    Then flatten it back to 1D
# array1 = np.arange(1,13)
# print(array1)
# array1 = array1.reshape(3,4)
# print(array1)
# array1 = array1.reshape(2,6)
# print(array1)
# print(array1.flatten())

# 2. Simulate a mini neural network layer:
#    inputs  = np.random.rand(1, 4)    ← random array shape (1, 4)
#    weights = np.random.rand(4, 3)    ← random array shape (4, 3)
#    result  = inputs @ weights        ← matrix multiply
#    Print the shape of result         ← should be (1, 3)
# inputs  = np.random.rand(1, 4)
# weights = np.random.rand(4, 3)
# print(inputs)
# print(weights)
# result  = inputs @ weights 
# print(result)
# print(result.shape)


# # 3. You have model output probabilities for one MNIST image:
# probs = np.array([0.02, 0.01, 0.05, 0.03, 0.01, 0.02, 0.01, 0.80, 0.03, 0.02])
# #                  0     1     2     3     4     5     6     7     8     9
# #    a. What digit did the model predict? (use argmax)
# #    b. What is the confidence? (the max value)
# #    c. Print: "Predicted: 7 with 80.0% confidence"

# print( f"Predicted: {probs.argmax()} with {probs.max()}% confidence")

arr = np.random.rand(5,784)

print(arr[0])