import pandas as pd

# Read the election data CSV file
try:
    df = pd.read_csv("election_data.csv")

    # Calculate the percentage of seats won by each party
    df["Seats_Percentage"] = (df["Seats_Won"] / df["Total_Seats"]) * 100
    print("DataFrame with Seats_Percentage column:\n", df)
except FileNotFoundError:
    print("Error: The file 'election_data.csv' does not exist.")
except Exception as e:
    print(f"Error reading the file or calculating: {e}")
