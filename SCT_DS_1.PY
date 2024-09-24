import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
np.random.seed(42)  # For reproducibility
data = {
    'age': np.random.randint(18, 70, size=1000),  # Ages between 18 and 70
    'gender': np.random.choice(['Male', 'Female'], size=1000)  # Randomly choosing Male or Female
}
df = pd.DataFrame(data)

# Set the style of seaborn
sns.set(style="whitegrid")

# Create a bar chart for gender distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='gender', data=df, palette='pastel')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Create a histogram for age distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['age'], bins=20, kde=True, color='blue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.axvline(df['age'].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean Age')
plt.legend()
plt.show()