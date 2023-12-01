import csv
import pandas as pd
import numpy as np

# Function to add Laplace noise to the dataset
def add_laplace_noise(data, scale):
    noise = np.random.laplace(0, scale, data.shape)
    noisy_data = data + noise
    return noisy_data

# Read the dataset from 'OversampledSwipeData.csv'
dataset = pd.read_csv('OversampledSwipeData.csv', index_col=0)

# Specify the percentage of data to add noise to (e.g., 60%)
noise_percentage = 0.7
sensitivity = 1.0  
privacy_budget = 1.0  

# Create a mask to randomly select the subset of data to add noise
mask = np.random.choice([True, False], size=len(dataset), p=[noise_percentage, 1 - noise_percentage])

# Add Laplace noise to the selected subset of the dataset
noise_scale = 0.1
noisy_data = dataset.copy()
noisy_subset = add_laplace_noise(noisy_data.loc[mask], noise_scale)
noisy_data.loc[mask] = noisy_subset.astype(noisy_data.dtypes)  # Cast to the same data type


noisy_data.to_csv('NoisyOversampledSwipeData.csv')

