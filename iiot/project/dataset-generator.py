import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def label_generator(temperature):
	label = 0 if 20 <= temperature <= 40 else 1

	return label

# Set the seed for reproducibility
np.random.seed(44)

# Define the mean and standard deviation of the normal distribution
mu = 35  # Mean temperature
sigma = 7  # Standard deviation

# Generate 1000 random temperatures from the normal distribution
normal_distribution = np.random.normal(mu, sigma, 1000)

# Round the temperatures to integers and clip them to the desired range (10 to 60)
temperatures = np.clip(np.round(normal_distribution).astype(int), 10, 60)

# Create timestamps, one second apart
start_time = datetime.now().replace(microsecond=0)
timestamps = [start_time + timedelta(seconds=i) for i in range(1000)]

# Labeling the data
labels = map(label_generator, temperatures)

# Create the DataFrame
data = pd.DataFrame({'temperature': temperatures, 'timestamp': timestamps, 'label': labels})

# Save the DataFrame to a CSV file
data.to_csv('data.csv', index=False)

print(data.head(20))

