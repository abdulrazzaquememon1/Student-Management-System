import json
import os

FILE_NAME = "students.json"


# -------------------------------
# LOAD STUDENTS
# -------------------------------
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


# -------------------------------
# SAVE STUDENTS
# -------------------------------
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# -------------------------------
# ADD STUDENT
# -------------------------------
def add_student(students):
    print("\n========== ADD STUDENT ==========")

    student_id = input("Enter Student ID: ")

    # Check if ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")

    try:
        cgpa = float(input("Enter CGPA: "))
    except ValueError:
        print("Invalid CGPA.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department,
        "cgpa": cgpa
    }

    students.append(student)

    save_students(students)

    print("Student added successfully!")


# -------------------------------
# VIEW STUDENTS
# -------------------------------
def view_students(students):
    print("\n========== ALL STUDENTS ==========")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("------------------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Department:", student["department"])
        print("CGPA:", student["cgpa"])


# -------------------------------
# SEARCH STUDENT
# -------------------------------
def search_student(students):
    print("\n========== SEARCH STUDENT ==========")

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found!")
            print("------------------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Department:", student["department"])
            print("CGPA:", student["cgpa"])

            return

    print("Student not found.")


# -------------------------------
# UPDATE STUDENT
# -------------------------------
def update_student(students):
    print("\n========== UPDATE STUDENT ==========")

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            print("\nEnter new information.")
            print("Press Enter to keep the old value.\n")

            name = input(f"Name ({student['name']}): ")
            age = input(f"Age ({student['age']}): ")
            department = input(
                f"Department ({student['department']}): "
            )
            cgpa = input(f"CGPA ({student['cgpa']}): ")

            if name != "":
                student["name"] = name

            if age != "":
                student["age"] = age

            if department != "":
                student["department"] = department

            if cgpa != "":
                try:
                    student["cgpa"] = float(cgpa)

                except ValueError:
                    print("Invalid CGPA. Old CGPA kept.")

            save_students(students)

            print("Student updated successfully!")

            return

    print("Student not found.")


# -------------------------------
# DELETE STUDENT
# -------------------------------
def delete_student(students):
    print("\n========== DELETE STUDENT ==========")

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            save_students(students)

            print("Student deleted successfully!")

            return

    print("Student not found.")


# -------------------------------
# MAIN MENU
# -------------------------------
def main():

    students = load_students()

    while True:

        print("\n")
        print("==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":

            add_student(students)

        elif choice == "2":

            view_students(students)

        elif choice == "3":

            search_student(students)

        elif choice == "4":

            update_student(students)

        elif choice == "5":

            delete_student(students)

        elif choice == "6":

            print("\nThank you for using Student Management System.")
            break

        else:

            print("Invalid choice. Please enter 1-6.")


# -------------------------------
# START PROGRAM
# -------------------------------
if __name__ == "__main__":
    main()