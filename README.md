# 🧠 ML Journey — From Python to Neural Networks

> A structured learning path to build a handwritten digit recognition neural network (MNIST) from scratch.
> **Goal:** Train a model that reads your own handwritten numbers using a webcam.

---

## 📁 Repo Structure

```
ml-journey/
│
├── phase1_python_basics/         # Python fundamentals for ML
├── phase2_numpy_pandas/          # Data manipulation & math arrays
├── phase3_visualization/         # Plotting data with Matplotlib
├── phase4_neural_networks/       # Neural network theory & concepts
├── phase5_mnist/                 # Final project — digit recognition
│
└── README.md                     # This file
```

---

## 🗺️ Learning Phases

### Phase 1 — Python Basics for ML `phase1_python_basics/`
> **Duration:** ~2 weeks · **Status:** 🔄 In Progress

The foundation. Python syntax, data types, and the building blocks used throughout ML code.

| File | Description |
|------|-------------|
| `01_variables.py` | Variables, data types (int, float, str, bool), f-strings |
| `02_lists.py` | Lists, indexing, slicing — like arrays in other languages |
| `03_loops.py` | for loops, while loops, list comprehensions |
| `04_functions.py` | Defining functions, parameters, return values |
| `05_dictionaries.py` | Key-value pairs — used heavily in ML configs |
| `06_file_io.py` | Reading and writing files (CSV, text) |

---

### Phase 2 — NumPy & Pandas `phase2_numpy_pandas/`
> **Duration:** ~3 weeks · **Status:** ⏳ Not Started

The backbone of all ML code. NumPy handles math on arrays (like matrices), Pandas handles datasets.

| File | Description |
|------|-------------|
| `01_numpy_basics.py` | Arrays, shapes, reshape, indexing |
| `02_numpy_math.py` | Matrix operations, dot products, broadcasting |
| `03_pandas_basics.py` | DataFrames, reading CSV, filtering data |
| `04_pandas_analysis.py` | Grouping, aggregating, cleaning data |

---

### Phase 3 — Visualization `phase3_visualization/`
> **Duration:** ~1 week · **Status:** ⏳ Not Started

See your data before modeling it. Matplotlib is the standard library for plotting in ML.

| File | Description |
|------|-------------|
| `01_line_plots.py` | Line charts — great for training loss curves |
| `02_scatter_plots.py` | Scatter plots — visualize data distributions |
| `03_image_display.py` | Display images (pixels) with Matplotlib |
| `04_mnist_preview.py` | Preview MNIST digit images before training |

---

### Phase 4 — Neural Network Theory `phase4_neural_networks/`
> **Duration:** ~3 weeks · **Status:** ⏳ Not Started

Understand what's happening under the hood before building. Covers the math and intuition behind neural nets.

| File | Description |
|------|-------------|
| `01_perceptron.py` | Build a single neuron from scratch |
| `02_activation_functions.py` | ReLU, Sigmoid, Softmax — visualized |
| `03_forward_pass.py` | Manual forward pass through a small network |
| `04_loss_functions.py` | What is loss? Cross-entropy explained |
| `05_backpropagation.py` | How the network learns (gradient descent) |

---

### Phase 5 — MNIST Digit Recognition 🎯 `phase5_mnist/`
> **Duration:** ~3–4 weeks · **Status:** ⏳ Not Started

The final project. Train a Convolutional Neural Network to recognize handwritten digits, then test it live with your webcam.

| File | Description |
|------|-------------|
| `01_load_dataset.py` | Load and explore the MNIST dataset |
| `02_preprocess.py` | Normalize images, prepare training data |
| `03_build_model.py` | Build the CNN architecture with Keras |
| `04_train_model.py` | Train the model, plot accuracy & loss |
| `05_evaluate_model.py` | Test accuracy on unseen data |
| `06_live_demo.py` | 🎥 Webcam demo — draw a digit, model guesses it |

---

## ⚙️ Setup

### Install all required libraries:
```bash
pip install numpy pandas matplotlib opencv-python mediapipe tensorflow keras scikit-learn
```

### Python version:
```
Python 3.9 or higher recommended
```

---

## 📈 Progress Tracker

- [x] Phase 1 — Python Basics
- [ ] Phase 2 — NumPy & Pandas
- [ ] Phase 3 — Visualization
- [ ] Phase 4 — Neural Network Theory
- [ ] Phase 5 — MNIST (final project)

---

## 🎯 End Goal

```
You draw a digit on paper  →  webcam captures it  →  neural network predicts the number
```

Built with: Python · NumPy · TensorFlow/Keras · OpenCV · MediaPipe

---

*Learning path guided by Claude (Anthropic) · Started June 2026*
