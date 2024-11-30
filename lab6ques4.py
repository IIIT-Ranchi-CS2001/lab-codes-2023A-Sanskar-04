import matplotlib.pyplot as plt

mp_data = {"BJP": 163, "INC": 66, "BSP": 0, "Others": 1}
raj_data = {"INC": 69, "BJP": 115, "BSP": 2, "Others": 13}

mp_labels = list(mp_data.keys())
mp_sizes = list(mp_data.values())
raj_labels = list(raj_data.keys())
raj_sizes = list(raj_data.values())

mp_percentages = [size / sum(mp_sizes) * 100 for size in mp_sizes]
raj_percentages = [size / sum(raj_sizes) * 100 for size in raj_sizes]

mp_explode = [
    0.1 if i == mp_sizes.index(max(mp_sizes)) else 0 for i in range(len(mp_sizes))
]
raj_explode = [
    0.1 if i == raj_sizes.index(max(raj_sizes)) else 0 for i in range(len(raj_sizes))
]

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

axs[0].pie(
    mp_sizes,
    labels=mp_labels,
    autopct=lambda p: f"{p:.1f}%",
    explode=mp_explode,
    startangle=90,
)
axs[0].set_title("Madhya Pradesh Seat Share")

axs[1].pie(
    raj_sizes,
    labels=raj_labels,
    autopct=lambda p: f"{p:.1f}%",
    explode=raj_explode,
    startangle=90,
)
axs[1].set_title("Rajasthan Seat Share")

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(mp_labels))
bar_width = 0.4
ax.bar(x, mp_sizes, width=bar_width, label="Madhya Pradesh", align="center")
ax.bar(
    [p + bar_width for p in x],
    raj_sizes,
    width=bar_width,
    label="Rajasthan",
    align="center",
)

ax.set_xticks([p + bar_width / 2 for p in x])
ax.set_xticklabels(mp_labels)
ax.set_xlabel("Parties")
ax.set_ylabel("Seats Won")
ax.set_title("Party-wise Seat Share in Assembly Elections 2023")
ax.legend()

plt.tight_layout()
plt.show()
