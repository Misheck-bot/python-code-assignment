# python-code-assignment
student management system python program
This is a Student Management System implemented in Python. It allows users to add, update, delete, and view student information.

FEATURES
Add New Student - Users can add a new student by providing the student's ID, name, age, and major.
Update Student Information - Users can update a student's information, such as name, age, and major.
Delete Student - Users can delete a student from the system by providing the student's ID.
View All Students - Users can view a list of all the students in the system.

CODE STRUCTURE

The code is divided into three main classes
Student - This class represents a student and contains the student's ID, name, age, and major. It also provides methods to update and display the student's information.
StudentDatabase - This class manages the list of students. It provides methods to add, remove, and retrieve students from the database.
StudentManagementSystem - This class is the main interface for the user. It uses the StudentDatabase class to perform the various actions, such as adding, updating, deleting, and displaying students.
The main_menu() function is the entry point of the program, which presents the user with the main menu and handles the user's choices.


CHANGES FROM THE PREVIOUS VERSION

In the previous version of the code, the StudentManagementSystem class had separate methods for each action (add, update, delete, and display). In this updated version, the manage_student() method in the StudentManagementSystem class handles all the actions by taking an action parameter to determine the operation to perform.

Additionally, the update() method in the Student class now uses the **kwargs syntax to allow for a variable number of keyword arguments, making it more flexible and easier to update student information.

The main functionality of the program remains the same, but the code structure and organization have been improved to make it more modular and maintainable.

USAGE
To run the Student Management System, follow these steps

Make sure you have Python installed on your system.
Save the code provided in the main.py file.
Open a terminal or command prompt and navigate to the directory where you saved the main.py file.
Run the following command to start the program

python main.py
