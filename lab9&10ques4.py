import matplotlib.pyplot as plt
import seaborn as sns

try:
    # Read the election data CSV file
    df = pd.read_csv("election_data.csv")

    # Create a bar chart using seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x="State", y="Seats_Won", hue="Party", data=df)

    # Customize the plot
    plt.title("Number of Seats Won by Each Party in Each State")
    plt.xlabel("State")
    plt.ylabel("Seats Won")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.show()

except FileNotFoundError:
    print("Error: The file 'election_data.csv' does not exist.")
except Exception as e:
    print(f"Error reading the file or plotting data: {e}")
