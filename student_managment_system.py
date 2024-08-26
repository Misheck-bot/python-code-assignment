# Student class to represent individual students
class Student:
    def __init__(self, id, name, age, major):
        # Initialize student attributes
        self.id = id
        self.name = name
        self.age = age
        self.major = major

    def update(self, **kwargs):
        # Update student attributes dynamically using keyword arguments
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def display(self):
        # Print out student information
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Major: {self.major}")

# StudentDatabase class to manage a collection of students
class StudentDatabase:
    def __init__(self):
        # Initialize an empty list to store students
        self.students = []

    def add_student(self, student):
        # Add a new student to the database
        self.students.append(student)

    def remove_student(self, student_id):
        # Remove a student from the database by their ID
        self.students = [s for s in self.students if s.id != student_id]

    def get_student(self, student_id):
        # Retrieve a student from the database by their ID
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def display_all_students(self):
        # Print out information for all students in the database
        for student in self.students:
            student.display()

# StudentManagementSystem class to handle student management operations
class StudentManagementSystem:
    def __init__(self):
        # Initialize a StudentDatabase object
        self.database = StudentDatabase()

    def manage_student(self, action, student_id, **kwargs):
        # Perform various student management actions (add, delete, update)
        if action == "add":
            # Create a new student and add it to the database
            student = Student(student_id, **kwargs)
            self.database.add_student(student)
            print(f"Student {student.name} added successfully.")
        elif action == "delete":
            # Remove a student from the database by their ID
            student = self.database.get_student(student_id)
            if student:
                self.database.remove_student(student_id)
                print(f"Student {student.name} deleted successfully.")
            else:
                print(f"Student with ID {student_id} not found.")
        elif action == "update":
            # Update the information of a student in the database
            student = self.database.get_student(student_id)
            if student:
                student.update(**kwargs)
                print(f"Student {student.name} updated successfully.")
            else:
                print(f"Student with ID {student_id} not found.")

    def display_all_students(self):
        # Display information for all students in the database
        self.database.display_all_students()

# Main function to run the Student Management System
def main_menu():
    # Create a StudentManagementSystem object
    system = StudentManagementSystem()

    # Display the main menu and handle user input
    while True:
        print("\nStudent Management System")
        print("1. Add New Student")
        print("2. Update Student Information")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # Add a new student to the database
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            major = input("Enter student major: ")
            system.manage_student("add", id, name=name, age=age, major=major)
        elif choice == "2":
            # Update the information of an existing student
            id = int(input("Enter student ID: "))
            name = input("Enter new name (to replace the current one): ")
            age = input("Enter new age (to replace the current onep): ")
            major = input("Enter new major (to replace the current one): ")
            kwargs = {}
            if name:
                kwargs["name"] = name
            if age:
                kwargs["age"] = int(age)
            if major:
                kwargs["major"] = major
            system.manage_student("update", id, **kwargs)
        elif choice == "3":
            # Delete a student from the database
            id = int(input("Enter student ID: "))
            system.manage_student("delete", id)
        elif choice == "4":
            # Display information for all students in the database
            system.display_all_students()
        elif choice == "5":
            # Exit the Student Management System
            print("Exiting Student Management System...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Run the main menu function to start the Student Management System
    main_menu()