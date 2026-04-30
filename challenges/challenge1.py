# challenge1.py – Frequency Filter
# Read favorites.csv, ask for a minimum vote count, print filtered results.
# No starter hints – build this from scratch using what you learned in week1 and week2.

import csv

counts = {}

with open("../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"]
        if language in counts:
            counts[language] += 1
        else:
            counts[language] = 1

minimum = int(input("Minimum votes to display: "))

sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for language, count in sorted_counts:
    if count >= minimum:
        print(f"{language}: {count}")
