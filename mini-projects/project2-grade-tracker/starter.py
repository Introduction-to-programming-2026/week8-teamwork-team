# starter.py — Grade Tracker
# Project 2 | Easy | 25–30 minutes
#
# Run from this folder:
#   python starter.py

import csv

# ── Step 1: Set up storage variables ─────────────────────────────────────────
scores = []
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

highest = {"name": "", "score": -1}
lowest  = {"name": "", "score": 101}

# ── Step 2: Read the CSV ──────────────────────────────────────────────────────
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name  = row["name"]
        score = int(row["score"])

        # Append score to the scores list
        scores.append(score)

        # Update highest
        if score > highest["score"]:
            highest["name"] = name
            highest["score"] = score

        # Update lowest
        if score < lowest["score"]:
            lowest["name"] = name
            lowest["score"] = score

        # Determine letter grade
        if score >= 90:
            letter = "A"
        elif score >= 80:
            letter = "B"
        elif score >= 70:
            letter = "C"
        elif score >= 60:
            letter = "D"
        else:
            letter = "F"

        # Increment grade_counts
        grade_counts[letter] += 1

# ── Step 3: Calculate the average ────────────────────────────────────────────
average = round(sum(scores) / len(scores), 1)

# ── Step 4: Print the report ──────────────────────────────────────────────────
print("=== Quiz Grade Summary ===")
print(f"{'Average score:':<20} {average}")
print(f"{'Highest score:':<20} {highest['score']} ({highest['name']})")
print(f"{'Lowest score:':<20} {lowest['score']} ({lowest['name']})")
print()
print("Grade distribution:")
for letter, count in grade_counts.items():
    print(f"  {letter} : {count} students")

