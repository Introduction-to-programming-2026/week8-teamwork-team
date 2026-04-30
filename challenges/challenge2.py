# challenge2.py – Two-Column Report
# Read favorites.csv, find the most common problem per language, print a table.

import csv

# nested dict: {language: {problem: count}}
data = {}

with open("../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"]
        problem = row["problem"]

        if language not in data:
            data[language] = {}

        if problem in data[language]:
            data[language][problem] += 1
        else:
            data[language][problem] = 1

# Print table
print(f"{'Language':<10} | Most Common Problem")
print(f"{'-'*10}-+--------------------")

for language, problems in data.items():
    most_common = max(problems, key=problems.get)
    print(f"{language:<10} | {most_common}")
