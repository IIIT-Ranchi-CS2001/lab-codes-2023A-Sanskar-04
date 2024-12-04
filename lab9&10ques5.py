import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = 'election_data.csv'

election_data = [
    ['State', 'Party', 'Seats_Won', 'Total_Seats', 'Voter_Turnout (%)'],
    ['Madhya Pradesh', 'BJP', 163, 230, 72.1],
    ['Madhya Pradesh', 'INC', 66, 230, 72.1],
    ['Madhya Pradesh', 'BSP', 0, 230, 72.1],
    ['Madhya Pradesh', 'Others', 1, 230, 72.1],
    ['Rajasthan', 'BJP', 115, 200, 74.2],
    ['Rajasthan', 'INC', 69, 200, 74.2],
    ['Rajasthan', 'BSP', 2, 200, 74.2],
    ['Rajasthan', 'Others', 13, 200, 74.2]
]

try:
    if not os.path.exists(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(election_data)
        print(f"File '{file_name}' created and data written successfully.")
    else:
        print(f"File '{file_name}' already exists.")
except IOError as e:
    print(f"Error writing to file '{file_name}': {e}")
except Exception as e:
    print(f"Unexpected error during file creation/writing: {e}")

try:
    df = pd.read_csv(file_name)
    print("Data successfully read into DataFrame.")
    df['Seats_Percentage'] = (df['Seats_Won'] / df['Total_Seats']) * 100
    print("DataFrame with Seats_Percentage column:\n", df)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_name}' is empty.")
except pd.errors.ParserError:
    print(f"Error: There was an issue parsing the file '{file_name}'.")
except KeyError as e:
    print(f"Error: Missing expected column '{e}' in the file '{file_name}'.")
except Exception as e:
    print(f"Unexpected error during data reading or calculation: {e}")

try:
    max_seats_per_state = df.loc[df.groupby('State')['Seats_Won'].idxmax()]
    print("Party with the highest number of seats in each state:\n", max_seats_per_state[['State', 'Party', 'Seats_Won']])
except KeyError as e:
    print(f"Error: Missing expected column '{e}' while processing the data.")
except Exception as e:
    print(f"Unexpected error during processing data: {e}")

try:
    plt.figure(figsize=(10, 6))
    sns.barplot(x='State', y='Seats_Won', hue='Party', data=df)
    plt.title('Number of Seats Won by Each Party in Each State')
    plt.xlabel('State')
    plt.ylabel('Seats Won')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
except ValueError as e:
    print(f"Error: There was a problem with the data used for plotting: {e}")
except Exception as e:
    print(f"Unexpected error during plotting: {e}")
