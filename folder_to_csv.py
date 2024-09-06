import os
import csv
import re

def extract_first_number_to_csv(folders, csv_filename):
    data = []

    for folder in folders:
        for filename in os.listdir(folder):
            if filename.endswith(".txt"):
                filepath = os.path.join(folder, filename)
                with open(filepath, 'r') as file:
                    content = file.read()
                    match = re.search(r'\d+', content)
                    if match:
                        data.append([match.group()])

    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["First Number"])
        writer.writerows(data)

if __name__ == "__main__":
    folders = ["test"]
    extract_first_number_to_csv(folders, "test_true.csv")