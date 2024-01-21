import numpy as np
import pandas as pd
from scipy.stats import gamma, norm

def calculate_spi(rainfall_values):
    # Step 2: Calculate cumulative rainfall
    cumulative_rainfall = np.cumsum(rainfall_values)

    # Step 3: Fit a gamma distribution to the cumulative rainfall series
    shape, loc, scale = gamma.fit(cumulative_rainfall)

    # Step 4: Calculate cumulative probability using the gamma distribution CDF
    cumulative_probability = gamma.cdf(cumulative_rainfall, shape, loc, scale)

    # Step 5: Transform cumulative probability to standard normal distribution
    transformed_values = norm.ppf(cumulative_probability)

    return transformed_values

# Read data from CSV file
file_path = R'D:\Frosthacks\Predicted_Csv\predictions west bengal.csv'  # Update with the correct file path
rainfall_data = pd.read_csv(file_path)

# Extract 'ANNUAL' column as an array
annual_rainfall_values = rainfall_data['ANNUAL'].values

# Calculate SPI values
spi_values = calculate_spi(annual_rainfall_values)

# Display the results
print("Yearly Rainfall:", annual_rainfall_values)
print("SPI Values:", spi_values)
