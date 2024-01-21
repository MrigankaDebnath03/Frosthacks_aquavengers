<<<<<<< HEAD
import csv
from collections import defaultdict

# Function to split the CSV by the first column
def split_csv_by_first_column(input_csv):
    # Read the input CSV and store data by the first column
    with open(input_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        csv_data = defaultdict(list)
        for row in reader:
            csv_data[row[0]].append(row)
    
    # Write each group to a separate CSV file
    for key, rows in csv_data.items():
        output_csv = f'{key}.csv'
        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        print(f'Created file: {output_csv}')

# Replace 'input.csv' with the path to your CSV file
split_csv_by_first_column('rainfall in india 1901-2015.csv')
=======
import csv
from collections import defaultdict

# Function to split the CSV by the first column
def split_csv_by_first_column(input_csv):
    # Read the input CSV and store data by the first column
    with open(input_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        csv_data = defaultdict(list)
        for row in reader:
            csv_data[row[0]].append(row)
    
    # Write each group to a separate CSV file
    for key, rows in csv_data.items():
        output_csv = f'{key}.csv'
        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        print(f'Created file: {output_csv}')

# Replace 'input.csv' with the path to your CSV file
split_csv_by_first_column('rainfall in india 1901-2015.csv')
>>>>>>> 44fe529aa4d178b868509939f45d54665a8befcb
