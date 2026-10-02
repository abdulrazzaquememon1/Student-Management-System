# Student Management System

A Python-based console application for managing student records. The system allows users to add, view, search, update, and delete student information.

## Features

- Add a new student
- View all students
- Search for a student by ID
- Update student information
- Delete a student
- Prevent duplicate Student IDs
- Store student records in a JSON file
- Basic input and error handling

## Technologies Used

- Python
- JSON
- File Handling
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Exception Handling

## Project Structure

```text
Student-Management-System/
│
├── student_management.py
├── students.json
└── README.md
```

## Requirements

- Python 3.x
- No external Python libraries are required

## How to Run

Open the project folder in VS Code and open the terminal.

Run:

```bash
python student_management.py
```

The application will display the following menu:

```text
==============================
   STUDENT MANAGEMENT SYSTEM
==============================
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
==============================
Enter your choice:
```

## Student Information

Each student record contains:

- Student ID
- Name
- Age
- Department
- CGPA

## Main Operations

### 1. Add Student

Allows the user to enter a new student's information.

The system checks whether the Student ID already exists before adding the student.

### 2. View Students

Displays all student records currently stored in the system.

### 3. Search Student

Allows the user to search for a student using their Student ID.

### 4. Update Student

Allows the user to modify information of an existing student.

The user can press Enter to keep the existing value.

### 5. Delete Student

Removes a student record using the Student ID.

### 6. Exit

Closes the application.

## Data Storage

The application uses a JSON file named:

```text
students.json
```

Student records are saved to this file so that the data is available when the program is started again.

Example:

```json
{
    "id": "101",
    "name": "Ali",
    "age": "20",
    "department": "Software Engineering",
    "cgpa": 3.5
}
```

## Error Handling

The application handles common situations such as:

- Duplicate Student ID
- Invalid CGPA input
- Student ID not found
- Empty student list

## What I Learned

This project helped me practice important Python programming concepts, including:

- Functions
- Lists
- Dictionaries
- Loops
- Conditional statements
- File handling
- JSON data storage
- Exception handling
- CRUD operations

## Future Improvements

Possible future improvements include:

- Graphical User Interface (GUI)
- SQLite or MySQL database
- User authentication
- Attendance management
- Course and grade management
- CSV/PDF report generation
- Sorting and filtering
- Search by name or department

## Conclusion

The Student Management System is a simple Python application that demonstrates how basic programming concepts can be combined to build a complete record-management system.

The project provides practical experience with Python, data structures, file handling, JSON storage, validation, and CRUD operations.
