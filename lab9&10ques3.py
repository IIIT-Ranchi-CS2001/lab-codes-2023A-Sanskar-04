try:
    # Read the election data CSV file
    df = pd.read_csv("election_data.csv")

    # Group by state and find the party with the maximum seats
    max_seats_per_state = df.loc[df.groupby("State")["Seats_Won"].idxmax()]
    print(
        "Party with the highest number of seats in each state:\n",
        max_seats_per_state[["State", "Party", "Seats_Won"]],
    )
except FileNotFoundError:
    print("Error: The file 'election_data.csv' does not exist.")
except Exception as e:
    print(f"Error reading the file or processing data: {e}")
