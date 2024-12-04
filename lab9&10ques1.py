import os
import csv

# Election data to write into the CSV file
election_data = [
    ["State", "Party", "Seats_Won", "Total_Seats", "Voter_Turnout (%)"],
    ["Madhya Pradesh", "BJP", 163, 230, 72.1],
    ["Madhya Pradesh", "INC", 66, 230, 72.1],
    ["Madhya Pradesh", "BSP", 0, 230, 72.1],
    ["Madhya Pradesh", "Others", 1, 230, 72.1],
    ["Rajasthan", "BJP", 115, 200, 74.2],
    ["Rajasthan", "INC", 69, 200, 74.2],
    ["Rajasthan", "BSP", 2, 200, 74.2],
    ["Rajasthan", "Others", 13, 200, 74.2],
]

# Check if the file exists
file_name = "election_data.csv"

try:
    if not os.path.exists(file_name):
        with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(election_data)
        print(f"File '{file_name}' created and data written successfully.")
    else:
        print(f"File '{file_name}' already exists.")
except Exception as e:
    print(f"Error writing to file: {e}")
