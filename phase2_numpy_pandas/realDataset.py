# import pandas as pd

# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# df = pd.read_csv(url)

# print(df.shape)       # → (150, 5)
# print(df.head())      # → first 5 rows
# print(df.info())      # → column types
# print(df.describe())  # → statss


import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# 1. How many flowers of each species are there?
print(df["species"].value_counts())

# 2. Filter — show only "virginica" species
print(df[df["species"] == "virginica"])

# 3. What is the average petal_length per species?
print(df.groupby("species")["petal_length"].mean())

# 4. Add a new column "big_flower"
#    True if petal_length > 4.0, False otherwise

df["big_flower"] = df["petal_length"] > 4

print(df)

# 5. Sort the entire dataframe by petal_length
#    from biggest to smallest
#    Hint: df.sort_values("petal_length", ascending=False)
df.sort_values("petal_length",ascending=False)
print(df)

# 6. Print only the first 3 columns (drop species and petal_width)
#    Hint: df[["sepal_length", "sepal_width", "petal_length"]]

print(df[["sepal_length", "sepal_width", "petal_length"]])