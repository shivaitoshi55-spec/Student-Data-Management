import csv

class Student:
    all_students = []

    def __init__(self, name, roll, maths, physics, chemistry):  
        self.name = name
        self.roll = roll
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

    def display(self, index=None):
        if index is not None:
            print(f"{index}. Name: {self.name}, Roll: {self.roll}, "
                  f"Maths: {self.maths}, Physics: {self.physics}, Chemistry: {self.chemistry}")
        else:
            print(f"Name: {self.name}, Roll: {self.roll}, "
                  f"Maths: {self.maths}, Physics: {self.physics}, Chemistry: {self.chemistry}")

    @classmethod
    def add_student(cls):
        print("\n----- Add Student -----")
        name = input("Enter name: ")
        roll = int(input("Enter roll number: "))

        for s in cls.all_students:
            if s.roll == roll:
                print("Roll number already exists.\n")
                return

        maths = int(input("Enter Maths marks: "))
        physics = int(input("Enter Physics marks: "))
        chemistry = int(input("Enter Chemistry marks: "))

        student = Student(name, roll, maths, physics, chemistry)
        cls.all_students.append(student)

        cls.save_to_file()
        print("Student added successfully.\n")

    @classmethod
    def view_students(cls):
        print("\n----- Student List -----")
        if not cls.all_students:
            print("No students found.\n")
        else:
            for i, student in enumerate(cls.all_students, 1):
                student.display(i)
            print("------------------------\n")

    @classmethod
    def search_student(cls):
        print("\n----- Search Student -----")
        roll = int(input("Enter roll number: "))
        for student in cls.all_students:
            if student.roll == roll:
                print("Student found:")
                student.display()
                return
        print("Student not found.\n")

    @classmethod
    def update_student(cls):
        print("\n----- Update Student -----")
        roll = int(input("Enter roll number: "))
        for student in cls.all_students:
            if student.roll == roll:
                student.name = input("Enter new name: ")
                student.maths = int(input("Enter new Maths marks: "))
                student.physics = int(input("Enter new Physics marks: "))
                student.chemistry = int(input("Enter new Chemistry marks: "))

                cls.save_to_file()
                print("Student updated successfully.\n")
                return
        print("Student not found.\n")

    @classmethod
    def delete_student(cls):
        print("\n----- Delete Student -----")
        roll = int(input("Enter roll number: "))
        for student in cls.all_students:
            if student.roll == roll:
                confirm = input("Are you sure you want to delete? (y/n): ")
                if confirm.lower() == 'y':
                    cls.all_students.remove(student)
                    cls.save_to_file()
                    print("Student deleted successfully.\n")
                else:
                    print("Deletion cancelled.\n")
                return
        print("Student not found.\n")

    @classmethod
    def average_marks(cls):
        print("\n----- Student Average -----")
        roll = int(input("Enter roll number: "))

        for s in cls.all_students:
            if s.roll == roll:
                avg = (s.maths + s.physics + s.chemistry) / 3
                print(f"Average Marks of {s.name}: {avg:.2f}\n")
                return

        print("Student not found.\n")

    @classmethod
    def save_to_file(cls):
        with open("students.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Roll", "Maths", "Physics", "Chemistry"])
            for s in cls.all_students:
                writer.writerow([s.name, s.roll, s.maths, s.physics, s.chemistry])

    @classmethod
    def load_from_file(cls):
        try:
            with open("students.csv", "r") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    name, roll, m, p, c = row
                    cls.all_students.append(Student(name, int(roll), int(m), int(p), int(c)))
        except FileNotFoundError:
            pass


# Load data at start
Student.load_from_file()

# Menu
while True:
    print("========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Average")
    print("7. Exit")
    print("===============================================")

    choice = input("Enter your choice: ")

    if choice == '1':
        Student.add_student()
    elif choice == '2':
        Student.view_students()
    elif choice == '3':
        Student.search_student()
    elif choice == '4':
        Student.update_student()
    elif choice == '5':
        Student.delete_student()
    elif choice == '6':
        Student.average_marks()
    elif choice == '7':
        print("Exiting program. Data saved.")
        break
    else:
        print("Invalid choice. Try again.\n")