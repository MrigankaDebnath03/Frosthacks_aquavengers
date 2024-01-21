<<<<<<< HEAD
import csv

# # Function to filter and create a new CSV with only 'YEAR' and 'ANNUAL' columns
# def filter_csv_columns(input_csv, output_csv):
#     # Define the columns to keep
#     columns_to_keep = ['YEAR', 'ANNUAL']
    
#     with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
#          open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
#         reader = csv.DictReader(infile)
#         writer = csv.DictWriter(outfile, fieldnames=columns_to_keep)
        
#         # Write the header
#         writer.writeheader()
        
#         # Write rows with only the specified columns
#         for row in reader:
#             filtered_row = {key: row[key] for key in columns_to_keep}
#             writer.writerow(filtered_row)

# # Replace 'input.csv' and 'output.csv' with the paths to your actual CSV files
# filter_csv_columns('D:\Frosthacks\Dataset\ARUNACHAL PRADESH.csv', 'D:\Frosthacks\Predictions_csv\ARUNACHAL PRADESH.csv')

import os

# Get the file name from the input path

input_csv = r"D:\Frosthacks\Dataset\WEST UTTAR PRADESH.csv"
columns_to_keep = ['YEAR', 'ANNUAL']

file_name = os.path.basename(input_csv)

# Construct the output path by joining the output folder and the file name
output_csv = os.path.join("D:\Frosthacks\Predictions_csv", file_name)

with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=columns_to_keep)
    
    # Write the header
    writer.writeheader()
    
    # Write rows with only the specified columns
    for row in reader:
        filtered_row = {key: row[key] for key in columns_to_keep}
        writer.writerow(filtered_row)
=======
import csv

# # Function to filter and create a new CSV with only 'YEAR' and 'ANNUAL' columns
# def filter_csv_columns(input_csv, output_csv):
#     # Define the columns to keep
#     columns_to_keep = ['YEAR', 'ANNUAL']
    
#     with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
#          open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
#         reader = csv.DictReader(infile)
#         writer = csv.DictWriter(outfile, fieldnames=columns_to_keep)
        
#         # Write the header
#         writer.writeheader()
        
#         # Write rows with only the specified columns
#         for row in reader:
#             filtered_row = {key: row[key] for key in columns_to_keep}
#             writer.writerow(filtered_row)

# # Replace 'input.csv' and 'output.csv' with the paths to your actual CSV files
# filter_csv_columns('D:\Frosthacks\Dataset\ARUNACHAL PRADESH.csv', 'D:\Frosthacks\Predictions_csv\ARUNACHAL PRADESH.csv')

import os

# Get the file name from the input path

input_csv = r"D:\Frosthacks\Dataset\WEST UTTAR PRADESH.csv"
columns_to_keep = ['YEAR', 'ANNUAL']

file_name = os.path.basename(input_csv)

# Construct the output path by joining the output folder and the file name
output_csv = os.path.join("D:\Frosthacks\Predictions_csv", file_name)

with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=columns_to_keep)
    
    # Write the header
    writer.writeheader()
    
    # Write rows with only the specified columns
    for row in reader:
        filtered_row = {key: row[key] for key in columns_to_keep}
        writer.writerow(filtered_row)
>>>>>>> 44fe529aa4d178b868509939f45d54665a8befcb
