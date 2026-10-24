import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [1000, 1500, 1200, 1800]
}

df = pd.DataFrame(data)

print(df)
print("Total Sales:", df["Sales"].sum())