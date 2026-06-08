# # ── Creating a dictionary ──────────────────────────
# student = {
#     "name": "Mhmd",
#     "age": 22,
#     "score": 98.5,
#     "passed": True
# }

# # ── Accessing values ───────────────────────────────
# print(student["name"])     # → Mhmd
# print(student["score"])    # → 98.5

# # ── Adding & updating ──────────────────────────────
# student["city"] = "Sidon"      # add new key
# student["score"] = 100         # update existing key
# print(student)

# # ── Removing ───────────────────────────────────────
# del student["city"]            # remove a key
# print(student)

# # ── Check if key exists ────────────────────────────
# if "name" in student:
#     print("name exists!")

# # ── Useful methods ─────────────────────────────────
# print(student.keys())          # → dict_keys(['name', 'age', 'score', 'passed'])
# print(student.values())        # → dict_values(['Mhmd', 22, 100, True])
# print(student.items())         # → all key-value pairs


# # Model configuration — you'll write this in Phase 5!
# model_config = {
#     "input_size": 784,       # 28x28 pixels flattened
#     "hidden_layers": [128, 64],
#     "output_size": 10,       # digits 0-9
#     "learning_rate": 0.001,
#     "epochs": 20,
#     "batch_size": 32
# }

# print(f"Training for {model_config['epochs']} epochs")
# print(f"Learning rate: {model_config['learning_rate']}")

# # Storing results per epoch
# results = {
#     "epoch": [],
#     "loss": [],
#     "accuracy": []
# }

# # Simulating adding training results
# results["epoch"].append(1)
# results["loss"].append(0.85)
# results["accuracy"].append(0.72)

# print(results)
# # {'epoch': [1], 'loss': [0.85], 'accuracy': [0.72]}


# model_config = {
#     "learning_rate": 0.001,
#     "epochs": 20,
#     "batch_size": 32
# }

# # Loop over keys and values together
# for key, value in model_config.items():
#     print(f"{key}: {value}")

# # learning_rate: 0.001
# # epochs: 20
# # batch_size: 32


# 1. Create a dictionary for a neural network layer with:
#    - "name"        → "hidden_layer_1"
#    - "neurons"     → 128
#    - "activation"  → "relu"
#    - "dropout"     → 0.2
#    Then print each key and value using a loop

neural_network_layer ={
    "name": "hidden_layer_1",
    "neurons": 128,
    "activation": "relu",
    "dropout": 0.2
}

for key, value in neural_network_layer.items():
    print(f"{key}: {value}")


# 2. You have this dictionary of label names
#    (you'll use this exact thing in MNIST!):
labels = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
}
#    a. Print the label for digit 7
#    b. Loop through and print: "0 → zero", "1 → one" ... etc

print(labels[7])
for key, value in labels.items():
    print(f"{key}-> {value}")

# 3. Create an empty dictionary called 'training_log'
#    Add 3 entries to it with keys "epoch_1", "epoch_2", "epoch_3"
#    Each value should be a dictionary with "loss" and "accuracy":
#    Example: {"loss": 0.9, "accuracy": 0.65}
#    Then print the accuracy of epoch_2

training_log= {
    "epoch_1":{
        "loss" :0.2,
        "accuracy":0.4
    }, 
    "epoch_2":{
        "loss" :0.1,
        "accuracy":0.5
    }, 
    "epoch_3":{
        "loss" :0.05,
        "accuracy":0.6
    }, 
}
print(training_log["epoch_2"]["accuracy"])