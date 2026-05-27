import csv

FILE_NAME = "students.csv"

# Load students from file
def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    except FileNotFoundError:
        pass

    return students


# Save students to file
def save_students(students):

    with open(FILE_NAME, "w", newline="") as file:

        fieldnames = ["name", "age", "marks", "subject"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(students)


# Add student
def add_student(students):

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")
    subject = input("Enter Subject: ")

    student = {
        "name": name,
        "age": age,
        "marks": marks,
        "subject": subject
    }

    students.append(student)

    save_students(students)

    print("Student Added Successfully!")


# View students
def view_students(students):

    if not students:
        print("No records found")
        return

    for i, student in enumerate(students, start=1):

        print(f"\nStudent {i}")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("Subject:", student["subject"])


# Search student
def search_student(students):

    name = input("Enter student name to search: ")

    found = False

    for student in students:

        if student["name"].lower() == name.lower():

            print("\nStudent Found")
            print(student)

            found = True
            break

    if not found:
        print("Student not found")


# Update student
def update_student(students):

    name = input("Enter student name to update: ")

    for student in students:

        if student["name"].lower() == name.lower():

            student["age"] = input("Enter new age: ")
            student["marks"] = input("Enter new marks: ")
            student["subject"] = input("Enter new subject: ")

            save_students(students)

            print("Student Updated Successfully!")
            return

    print("Student not found")


# Delete student
def delete_student(students):

    name = input("Enter student name to delete: ")

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            save_students(students)

            print("Student Deleted Successfully!")
            return

    print("Student not found")


# Main Program
def main():

    students = load_students()

    while True:

        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

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
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


main()
