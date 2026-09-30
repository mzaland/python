class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email  # This triggers the @property setter below

    # Email getter
    @property
    def email(self):
        return self._email

    # Email validation setter
    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format! Must contain @ and .")
        self._email = value

    def role_info(self):
        return "Generic Person"

    def __str__(self):
        return f"{self.name} ({self.email})"


class Student(Person):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id

    # Overriding role_info
    def role_info(self):
        return f"Student ID: {self.student_id}"

    def __str__(self):
        return f"Student: {self.name}, ID: {self.student_id}"


class Lecturer(Person):
    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.department = department

    # Overriding role_info
    def role_info(self):
        return f"Lecturer in Dept: {self.department}"

    def __str__(self):
        return f"Lecturer: {self.name}, Dept: {self.department}"


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []  # Composition: Course contains a list of Students

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"Course: {self.course_name}, Enrolled: {len(self.students)} students"


# Testing the Program


# 1. Create students and a lecturer
s1 = Student("Alice", "alice@gmail.com", "S101")
s2 = Student("Bob", "bob@outlook.com", "S102")
l1 = Lecturer("Dr. Smith", "smith@yahoo.com", "Computer Science")

# 2. Demonstrate Composition (Adding students to a course)
my_course = Course("Python Basics")
my_course.add_student(s1)
my_course.add_student(s2)

print("--- Course Info ---")
print(my_course)
print()

# 3. Create a polymorphic list of Person objects
people_list = [s1, l1, s2]

print("--- Polymorphic Print Loop ---")
for person in people_list:
    print(person)             # Uses the overridden __str__ method
    print(person.role_info()) # Uses the overridden role_info method
    print("-" * 20)
