# This is the beginning of an demo project.
# Learning python ORMs.


import cmd


# Define a Student class
class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.corrections = []

    def add_correction(self, correction):
        self.corrections.append(correction)

# Define a Correction class


class Correction:
    def __init__(self, link):
        self.link = link

# Define a DataManager class for abstracting data operations


class Storage:
    def __init__(self):
        self.students = []

    def add_student(self, name, email):
        new_student = Student(name, email)
        self.students.append(new_student)
        # Placeholder: Add code to persist the student data

    def add_correction(self, student_email, link):
        for student in self.students:
            if student.email == student_email:
                correction = Correction(link)
                student.add_correction(correction)
                # Placeholder: Add code to persist the correction data

    def list_students(self):
        for student in self.students:
            print(f"Student: {student.name} ({student.email})")
            for correction in student.corrections:
                print(f"  Correction: {correction.link}")

    # Add methods for updating and removing data as needed
    # Placeholder: Add corresponding database operations

# Define a command-line interface using the cmd module


class StudentAssignmentCLI(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = ">> "
        self.intro = "Student Corrections Management Tool"

    def do_add_student(self, arg):
        """Add a student. Usage: add_student <student_name> <student_email>"""
        args = arg.split()
        if len(args) != 2:
            print("Usage: add_student <student_name> <student_email>")
            return
        name, email = args
        storage.add_student(name, email)

    def do_add_correction(self, arg):
        """Add a correction to a student.
        Usage: add_correction <student_email> <correction_link>"""
        args = arg.split()
        if len(args) != 2:
            print("Usage: add_correction <student_email> <correction_link>")
            return
        student_email, correction_link = args
        storage.add_correction(student_email, correction_link)

    def do_list_students(self, arg):
        """List all students and their corrections."""
        storage.list_students()

    def do_quit(self, arg):
        """Exit the program."""
        print("Exiting...")
        return True


if __name__ == "__main__":

    storage = Storage()
    cli = StudentAssignmentCLI()
    cli.cmdloop()
