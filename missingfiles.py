# Import the pandas library
import os
import pandas as pd

# Specify the path to the folder containing the csv files
folder_path = r"D:\Frosthacks\Predictions_csv"

# Loop through all the files in the folder that end with .csv
for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        # Read the csv file into a pandas dataframe
        df = pd.read_csv(os.path.join(folder_path, file))
        
        # Replace all the NA values in the 'ANNUAL' column with 1000
        df['ANNUAL'] = df['ANNUAL'].fillna(1000)
        
        # Save the modified dataframe to the same csv file
        df.to_csv(os.path.join(folder_path, file), index=False)
