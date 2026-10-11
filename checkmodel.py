import pickle
import pandas as pd

with open("gg.pkl", "rb") as f:
    given = pickle.load(f)

print(given[0])
df = pd.DataFrame(given)
print(df.head())
print(df.columns.tolist())