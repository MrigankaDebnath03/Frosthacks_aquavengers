# import pandas as pd

# # Read the CSV file
# df = pd.read_csv(r'D:\Frosthacks\Predicted_Csv\predictions Rajasthan.csv')

# # Create a new column 'Range'
# df['Range'] = df['YEAR'].astype(str) + '-' + (df['YEAR'] + 4).astype(str)

# # Create a new column 'Drought Probability' and calculate based on 5-year average
# df['Drought Probability'] = 0

# for i in range(0, len(df), 5):
#     five_year_avg = df['ANNUAL'].iloc[i:i+5].mean()
#     if five_year_avg < 700:
#         df.loc[i:i+4, 'Drought Probability'] = 1

# # Save the updated DataFrame to a new CSV file
# df[['Range', 'Drought Probability']].to_csv(r'D:\Frosthacks\Drought hoga ya nahi\output_file.csv', index=False)

import os
import pandas as pd

# Specify the input and output folders
input_folder = r'D:\Frosthacks\Predicted_Csv'
output_folder = r'D:\Frosthacks\Drought hoga ya nahi'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        # Read the CSV file
        filepath = os.path.join(input_folder, filename)
        df = pd.read_csv(filepath)

        # Create a new column 'Range'
        df['Range'] = df['YEAR'].astype(str) + '-' + (df['YEAR'] + 4).astype(str)

        # Create a new column 'Drought Probability' and calculate based on 5-year average
        df['Drought Probability'] = 0

        for i in range(0, len(df), 5):
            five_year_avg = df['ANNUAL'].iloc[i:i+5].mean()
            if five_year_avg < 900:
                df.loc[i:i+4, 'Drought Probability'] = 1

        # Create the output filename
        output_filename = f'drought_predicted_{filename}'

        # Save the updated DataFrame to a new CSV file in the output folder
        output_filepath = os.path.join(output_folder, output_filename)
        df[['Range', 'Drought Probability']].to_csv(output_filepath, index=False)

print("Processing complete.")
