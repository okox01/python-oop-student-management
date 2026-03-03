# ===============================
# Student Management System (OOP)
# ===============================


class Student:
    def __init__(self, name, roll, grades):
        self.name = name
        self.roll = roll
        self.__grades = grades  # Encapsulation (private attribute)

    # Method to display student info
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")

    # Getter method for grades
    def get_grades(self):
        return self.__grades

    # Method to calculate average grade
    def average_grade(self):
        return sum(self.__grades) / len(self.__grades)

    # Method to find highest grade
    def highest_grade(self):
        return max(self.__grades)


# Inheritance
class Graduate(Student):
    def __init__(self, name, roll, grades, thesis_title):
        super().__init__(name, roll, grades)
        self.thesis_title = thesis_title

    # Method overriding
    def display(self):
        super().display()
        print(f"Thesis Title: {self.thesis_title}")

    # Extra method for graduate
    def summary(self):
        print("----- Graduate Summary -----")
        self.display()
        print(f"Average Grade: {self.average_grade():.2f}")
        print(f"Highest Grade: {self.highest_grade()}")
        print("----------------------------")


# ===============================
# Simple Menu System
# ===============================

students = []


def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll: ")
    grades = list(map(int, input("Enter grades separated by space: ").split()))
    student = Student(name, roll, grades)
    students.append(student)
    print("Student added successfully!\n")


def add_graduate():
    name = input("Enter Name: ")
    roll = input("Enter Roll: ")
    grades = list(map(int, input("Enter grades separated by space: ").split()))
    thesis = input("Enter Thesis Title: ")
    graduate = Graduate(name, roll, grades, thesis)
    students.append(graduate)
    print("Graduate added successfully!\n")


def view_students():
    if not students:
        print("No students available.\n")
        return

    for i, student in enumerate(students, start=1):
        print(f"\nStudent {i}:")
        student.display()
        print(f"Average Grade: {student.average_grade():.2f}")
        print(f"Highest Grade: {student.highest_grade()}")
        print("--------------------------")


# ===============================
# Main Program
# ===============================

if __name__ == "__main__":

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Add Graduate")
        print("3. View Students")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_graduate()
        elif choice == "3":
            view_students()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")