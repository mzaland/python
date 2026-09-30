# String methods

# 1. __init__ (Setting up initial data)
def __init__(self, name): # constructor
    self.name = name

# 2. __str__ (Clean printing for normal users)
def __str__(self): # str stands for string
    return f"Student: {self.name}"

# 3. __repr__ (Technical layout for coders/debugging)
def __repr__(self): # repr stands for represent which is for developers not user
    return f"Student(name='{self.name}')"

# integer methods

# 4. __eq__ (Tells Python what makes two objects equal '==')
def __eq__(self, other): # eq checks the equality of the content not memory address
    return self.name == other.name

# 5. __lt__ (Tells Python how to check if one is less than another '<')
def __lt__(self, other):  # lt stands for less then like we have it math <
    return self.name < other.name

# 6. __len__ (Tells Python what number to return for len())
def __len__(self): # it counts the items passed like in a list
    return len(self.list_of_items)
