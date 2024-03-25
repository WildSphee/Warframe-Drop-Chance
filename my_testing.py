import random
from collections import Counter

import matplotlib.pyplot as plt

d = {"w": 6.1 / 100, "x": 6.1 / 100, "y": 9.3 / 100, "z": 6.1 / 100}


def simulate_run(drop_table: dict) -> int:
    "insert a drop table, creates a simulated run until all drops are received"

    combine = sum(drop_table.values())
    drop_table["empty"] = 1 - combine

    runs = 0
    while len(drop_table.keys()) > 1:
        runs += 1
        choice = random.choices(
            list(drop_table.keys()), weights=list(drop_table.values()), k=1
        )[0]
        if choice != "empty":
            del drop_table[choice]
    return runs


result_counter = Counter()
for _ in range(10000):
    nd = d.copy()
    result = simulate_run(nd)
    result_counter[result] += 1

print(f"{result_counter=}")


# Separate the keys and values for plotting
results = list(result_counter.keys())
counts = list(result_counter.values())

# Create a bar chart
plt.bar(results, counts)
plt.title("Citrine Drop Chance")
plt.xlabel("Runs")
plt.ylabel("Frequency")

plt.savefig("citrine_drop_chance.png")
