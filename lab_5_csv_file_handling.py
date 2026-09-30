import csv
import os

FILENAME = "gradebook.csv"
OUTPUT_FILE = "results.csv"

# 1. Create original CSV file (with punctuation/spaces in names)
data = [
    {"student_id": "101", "name": "Ahmad Khan", "midterm": "85", "final": "90"},
    {"student_id": "102", "name": "Ali Batayt", "midterm": "60", "final": "55"},
    {"student_id": "103", "name": "Wali Ahmad", "midterm": "45", "final": "50"},
    {"student_id": "104", "name":"Mohammdullah", "midterm": "95", "final": "90"}
]
with open(FILENAME, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

# 2. Read with DictReader, 3. Calculate metrics, 4. Filter by Threshold
THRESHOLD = 60
passed_students = []

with open(FILENAME, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Calculate average
        mid = float(row["midterm"])
        fin = float(row["final"])
        row["average"] = (mid + fin) / 2

        # Check passing threshold
        if row["average"] >= THRESHOLD:
            print(f"Passed: {row['name']} (Avg: {row['average']})")
            passed_students.append(row)

# 5. Write calculated results to a new file
with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["student_id", "name", "midterm", "final", "average"])
    writer.writeheader()
    writer.writerows(passed_students)
