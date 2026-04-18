import pandas as pd


data = {
    'Fruit': ['Apple', 'Banana', 'Orange', 'Avocado', 'Guava'],
    'Protein (g per 100g)': [0.3, 1.1, 0.9, 2.0, 2.6]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Fruit Protein Table:")
print(df)

# Find the fruit with the highest protein content
max_protein = df[df['Protein (g per 100g)'] == df['Protein (g per 100g)'].max()]
print("\nFruit with the highest protein content:")
print(max_protein)
