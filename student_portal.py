
"""
PROG211 - Object-Oriented Programming 1
Project: Student Learning Portal

This program allows users to register, display, and search
for student records using object-oriented programming.
"""


class Student:
    # Class attribute
    total_students = 0

    def __init__(self, student_id, name, course):
        # Instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course

        Student.total_students += 1

    # Instance method
    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")

    # Class method
    @classmethod
    def get_total_students(cls):
        return cls.total_students


class StudentPortal:
    def __init__(self):
        # Dictionary to store student objects
        self.students = {}

    # Add a student object to the dictionary
    def add_student(self, student):
        if student.student_id in self.students:
            print("Error: Student ID already exists.")
            return False

        self.students[student.student_id] = student
        print("Student registered successfully.")
        return True

    # Display all student records
    def display_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n========== STUDENT RECORDS ==========")

        for student in self.students.values():
            student.display_info()
            print("-------------------------------------")

    # Search for a student using their ID
    def find_student(self, student_id):
        return self.students.get(student_id)


# Function to add a student
def add_student_to_portal(portal):
    print("\n========== REGISTER STUDENT ==========")

    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in portal.students:
        print("Error: Student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    student = Student(student_id, name, course)
    portal.add_student(student)


# Function to display student records
def display_portal_records(portal):
    portal.display_students()


# Function to search for a student
def search_student_in_portal(portal):
    student_id = input("Enter student ID to search: ").strip()
    student = portal.find_student(student_id)

    if student is None:
        print("Student record not found.")
    else:
        print("\nStudent found:")
        student.display_info()


# Main function
def main():
    portal = StudentPortal()

    while True:
        print("\n=====================================")
        print("       STUDENT LEARNING PORTAL")
        print("=====================================")
        print("1. Add a student")
        print("2. Display all students")
        print("3. Search for a student")
        print("4. Display total students")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student_to_portal(portal)

        elif choice == "2":
            display_portal_records(portal)

        elif choice == "3":
            search_student_in_portal(portal)

        elif choice == "4":
            print(
                "Total student objects created:",
                Student.get_total_students()
            )

        elif choice == "5":
            print("Thank you for using the Student Learning Portal.")
            break

        else:
            print("Invalid option. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()
1