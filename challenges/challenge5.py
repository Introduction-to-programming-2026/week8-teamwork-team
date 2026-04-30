student_id,language,score
1,Python,5
2,C,3
3,Scratch,4
2,Python,5
4,,3
5,Java,2
6,Python,6
7,C,1
,Scratch,4
8,Python,3
# challenge5.py – Data Cleaner
# Read a messy CSV, detect problems, write a cleaned version, print a report.
# Create your own messy_data.csv with intentional errors to test against.

import csv

VALID_LANGUAGES = {"Python", "C", "Scratch"}
VALID_SCORES = range(1, 6)  # 1–5

removed = []
cleaned = []

with open("messy_data.csv", "r") as file:
    reader = csv.DictReader(file)
    seen_ids = set()

    for row in reader:
        student_id = row["student_id"].strip()
        language = row["language"].strip()
        score_str = row["score"].strip()

        # Blank row check
        if not student_id and not language and not score_str:
            removed.append((row, "blank row"))
            continue

        # Missing student ID
        if not student_id:
            removed.append((row, "missing student ID"))
            continue

        # Duplicate student ID
        if student_id in seen_ids:
            removed.append((row, f"duplicate student ID: {student_id}"))
            continue

        # Unknown language
        if language not in VALID_LANGUAGES:
            removed.append((row, f"unknown language: '{language}'"))
            continue

        # Out-of-range score
        try:
            score = int(score_str)
            if score not in VALID_SCORES:
                removed.append((row, f"out-of-range score: {score}"))
                continue
        except ValueError:
            removed.append((row, f"invalid score: '{score_str}'"))
            continue

        seen_ids.add(student_id)
        cleaned.append({"student_id": student_id, "language": language, "score": score})

# Write cleaned file
with open("cleaned_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["student_id", "language", "score"])
    writer.writeheader()
    writer.writerows(cleaned)

# Print report
print("=== Cleaning Report ===")
print(f"Rows kept:    {len(cleaned)}")
print(f"Rows removed: {len(removed)}")
print("\nRemoved rows:")
for row, reason in removed:
    print(f"  {dict(row)} → {reason}")

print("\nSaved to cleaned_data.csv")
