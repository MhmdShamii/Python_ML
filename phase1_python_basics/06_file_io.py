# ── Writing a file ─────────────────────────────────
# with open("phase1_python_basics/results.txt", "w") as f:
#     f.write("Training Results\n")
#     f.write("Epoch 1: loss=0.9\n")
#     f.write("Epoch 2: loss=0.7\n")

# # ── Reading a file ─────────────────────────────────
# with open("phase1_python_basics/results.txt", "r") as f:
#     content = f.read()
#     print(content)

# # ── Reading line by line ───────────────────────────
# with open("phase1_python_basics/results.txt", "r") as f:
#     for line in f:
#         print(line.strip())    # .strip() removes the \n at the end

# # Without 'with' — you must remember to close the file manually
# with open("phase1_python_basics/file.txt", "w") as f:
#     f.write("Hello, world!\n")

# f = open("phase1_python_basics/file.txt", "r")
# content = f.read()
# f.close()              # easy to forget!

# With 'with' — closes automatically, even if an error occurs
# with open("phase1_python_basics/file.txt", "r") as f:
#     content = f.read()
# file is already closed here ✅

# open("phase1_python_basics/file.txt", "w")   # write  — creates file, overwrites if exists
# open("phase1_python_basics/file.txt", "a")   # append — adds to end, keeps existing content
# open("phase1_python_basics/file.txt", "r")   # read   — read only (default)

# import csv

# # Writing a CSV (spreadsheet-style data)
# training_log = [
#     {"epoch": 1, "loss": 0.9, "accuracy": 0.65},
#     {"epoch": 2, "loss": 0.7, "accuracy": 0.78},
#     {"epoch": 3, "loss": 0.5, "accuracy": 0.85},
# ]

# with open("phase1_python_basics/training_log.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["epoch", "loss", "accuracy"])
#     writer.writeheader()
#     writer.writerows(training_log)

# # Reading it back
# with open("phase1_python_basics/training_log.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(f"Epoch {row['epoch']}: loss={row['loss']}, accuracy={row['accuracy']}")


# 1. Write a function called save_log(filename, data)
#    that takes a filename and a list of strings,
#    and writes each string on a new line
#    Test it with:

def save_log(fileName, data):
    with open(fileName,'w')as f:
        for data in data :
            f.write(f"{data}\n")

save_log("phase1_python_basics/my_log.txt", ["Epoch 1: loss=0.9", "Epoch 2: loss=0.7", "Epoch 3: loss=0.5"])

# 2. Write a function called read_log(filename)
#    that reads the file back and prints each line
#    Test: read_log("phase1_python_basics/my_log.txt") should print:
#    Epoch 1: loss=0.9
#    Epoch 2: loss=0.7
#    Epoch 3: loss=0.5
def read_log(fileName):
    with open(fileName,'r')as f:
        content = f.read()
        print(content)

read_log("phase1_python_basics/my_log.txt")

# 3. Write a function called save_config(config, filename)
#    that saves a dictionary to a text file like this:
#    learning_rate: 0.001
#    epochs: 20
#    batch_size: 32
#    Test with:
config = {"learning_rate": 0.001, "epochs": 20, "batch_size": 32}

def save_config(config, fileName):
    with open(fileName,"w") as f:
        for key,value in config.items():
            f.write(f"{key}: {value} \n")

save_config(config, "phase1_python_basics/config.txt")