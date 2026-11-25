
# PROG211 Student Learning Portal

## 1. Project Overview

The Student Learning Portal is a console-based Python application
developed for the PROG211 Object-Oriented Programming 1 assignment.
It demonstrates how student records can be managed using
object-oriented programming concepts.

## 2. Problem Statement

Managing student information manually can be time-consuming.
This application provides a basic way to register, search for,
and display student records.

## 3. Objectives

- Demonstrate classes and objects in Python.
- Use attributes and methods to represent student information.
- Store multiple student objects in a dictionary.
- Add, display, and search for student records.
- Demonstrate an instance method and a class method.
- Apply modular and reusable programming practices.

## 4. Technologies Used

- Python 3
- Git
- GitHub

## 5. Classes and Methods

### Student

Represents an individual student.

Attributes:
- student_id
- name
- course

Methods:
- display_info(): displays a student's details.
- get_total_students(): a class method that returns the number
  of Student objects created.

### StudentPortal

Manages student records using a dictionary.

Methods:
- add_student(): adds a student and prevents duplicate IDs.
- display_students(): displays all registered students.
- find_student(): searches for a student by ID.

## 6. Data Structure

A dictionary stores student objects. Each student ID is used as
a key, and the corresponding Student object is the value.

## 7. How to Run the Application

1. Install Python 3.
2. Open a terminal in the project directory.
3. Run:

   python student_portal.py

4. Follow the menu to add, display, or search for students.

## 8. Example Usage

Example student details:

- Student ID: ST001
- Name: Mohamed
- Course: Software Engineering

- Student ID: ST002
- Name: Fatmata
- Course: Computer Science

After adding the records, select option 2 to display all students.

## 9. Digital Public Goods (DPG) Principles

This project demonstrates modular code and reusable programming
components. Publishing the source code publicly supports access
and reuse.

Further work is needed to improve accessibility, documentation,
privacy safeguards, and compliance with applicable DPG standards.
The application uses sample data and should not be used to store
sensitive student information.

## 10. Limitations and Future Improvements

- Records are stored in memory and are lost when the program exits.
- The application currently uses a text-based interface.
- Future improvements could include file or database storage,
  stronger validation, and an accessible graphical interface.

## 11. Author

PROG211 Individual Assignment
