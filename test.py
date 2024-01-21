import pandas as pd
from spi.gamma import spi_gamma

# Load the CSV file into a Pandas DataFrame
file_path = 'D:\Frosthacks\Predicted_Csv\predictions west bengal.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Replace 'YOUR_AREA' with the actual area of the Indian State
area_of_state = 137,500,332,776,000  # Replace with the actual area

# Calculate SPI values
df['SPI'] = spi_gamma(df['ANNUAL'].values, scale=1, data_start_year=df['YEAR'].min(), calibration_year_initial=df['YEAR'].min(), calibration_year_final=df['YEAR'].max(), distribution="pearson3")

# You can also multiply SPI values by the area to get the total precipitation deficit or surplus
df['Total_Precipitation_Deficit'] = df['SPI'] * area_of_state

# Print the DataFrame with SPI values and total precipitation deficit
print(df[['YEAR', 'ANNUAL', 'SPI', 'Total_Precipitation_Deficit']])
