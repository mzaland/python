# 1. List of 10 student scores
scores = [55, 82, 90, 60, 45, 82, 70, 95, 60, 88]

# 2. Minimum, maximum, and average
min_score = min(scores)
max_score = max(scores)
avg_score = sum(scores) / len(scores)


# 3. List comprehension (scores >= 60)
passed_scores = [s for s in scores if s >= 60]

# 4. Convert to set (Removes duplicates)
unique_scores = set(scores)

# 5. Dictionary mapping IDs to names
student_dict = {"S01": "Ali", "S02": "Ahmad", "S03": "Khan"}

# 6. Search for student by ID
search_id = "S02"
student_found = student_dict.get(search_id, "Not Found")

# 7. Use zip() and enumerate() to pair IDs with scores and sort them the enumerate gives the ranking to the people
student_ids = ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10"]
records = list(zip(student_ids, scores))

# Sort student records by score (item[1] is the score)
sorted_records = sorted(records, key=lambda item: item[1])

# --- Print Outputs ---
print(f"Min: {min_score}, Max: {max_score}, Avg: {avg_score}")
print(f"Passed: {passed_scores}")
print(f"Set Result: {unique_scores}")
print(f"Search {search_id}: {student_found}")

print("\n--- Sorted Records with enumerate() ---")
for index, record in enumerate(sorted_records, start=1):
    print(f"Rank {index}: ID {record[0]} scored {record[1]}")
