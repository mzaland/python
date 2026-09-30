import os # the python operating system module

FILENAME = "students.txt"

if not os.path.exists(FILENAME): # this is not supposed to be but just for the  exception handling
    print("Error: File does not exist.")
else:
    with open(FILENAME, "r") as f:
        lines = f.readlines() # reads the file and saves it into a list
    print("Records:\n" + "".join(lines) + f"Total: {len(lines)}")

    # Search for ID '3' (ali)
    print("Found:", [l.strip() for l in lines if l.startswith("3")])

with open(FILENAME, "a") as f:
    f.write("6\tjan\n")  # Appends student 6 using a tab space
