import requests
import csv

# Step 1: Download the dataset
url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)

# Save the dataset locally as a CSV file
csv_file = "taxi_zone_lookup.csv"
with open(csv_file, 'w') as file:
    file.write(response.text)

# Step 2: Read the downloaded CSV file and calculate facts
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    data = list(reader)  # Convert CSV data to a list of dictionaries

    # a. Total Number of Records
    total_records = len(data)

    # b. Find Unique Boroughs in sorted order (ascending)
    boroughs = sorted(set(row['Borough'] for row in data))

    # c. Number of Records for Brooklyn Borough
    brooklyn_records = sum(1 for row in data if row['Borough'] == 'Brooklyn')

# Step 3: Save the facts in a file
output_file = "/root/taxi_zone_output.txt"  # Adjust the path if needed
with open(output_file, 'w') as file:
    file.write(f"Total Number of Records: {total_records}\n")
    file.write(f"Unique Boroughs (sorted): {boroughs}\n")
    file.write(f"Number of Records for Brooklyn Borough: {brooklyn_records}\n")

print("Facts saved to", output_file)
