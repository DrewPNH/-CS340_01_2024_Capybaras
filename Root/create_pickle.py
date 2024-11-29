import pickle
import pandas as pd

# Create the sample dataset
data = {
    "ID": [1, 2, 3, 4, 5, 6],
    "x": [10.0, 12.5, 14.0, 16.5, 18.0, 20.5],
    "y": [20.0, 25.0, 30.0, 35.0, 40.0, 45.0],
    "z": [15.0, 18.0, 21.0, 24.0, 27.0, 30.0],
    "Category": ["A", "B", "C", "A", "B", "C"]
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Save as a pickle file
pickle_file = "data.pkl"
with open(pickle_file, "wb") as f:
    pickle.dump(df, f)

print(f"Pickle file '{pickle_file}' created successfully!")
