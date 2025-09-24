class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.absences = 0
        self.latenesses = 0
        self.total_periods = 0

    def add_absence(self):
        self.absences += 1

    def add_period(self):
        self.total_periods = self.total_periods + 1
    
    def calc_attendance(self):
        attendance = (self.total_periods - self.absences)/self.total_periods * 100
        print(attendance)

class Teacher:
    def __init__(self, name):
        self.name = name
    classes = []


class Roll:
#Class has teacher and a list of students.
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher


class RollManager:
    def __init__(self):
        self.members = []

    def add_student(self, student, studentage):
        if student in self.members:
            raise ValueError("Student already exists.")
        self.members.append(Student(student, studentage))

    def remove_student(self, student):
        if student not in self.members:
            raise ValueError("Student doesn't exist.")
        self.members.pop(student)

class RollDatabase:
    def __init__(self):
        self.storage = []

    def add_class(self, name, teacher):
        self.storage.append(Roll(name, teacher))


#class AttendanceManager(Student):
    #def __init__(self):
        
    

#-----Facade-----

class StudentAttendanceSystemFacade:
    def __init__(self):
        self.database = RollDatabase()
        self.roll_manager = RollManager()

    def create_class(self, name, teacher):
        self.database.add_class(name, teacher)
        amount = int(input("\nHow many students are in the class?: "))
        while amount != 0:
            name = input("Enter name (FirstLast): ")
            age = str(input("Enter age: "))
            self.roll_manager.add_student(name, age)
            amount = amount - 1

    def attendance_report(self, student):
        attendance = "Student has attended " + str((student.total_periods - student.absences)) + " out of " + str(student.total_periods) + " classes."
        print(attendance)

    def attendance_notify(self, student):
        print(student.calc_attendance())

    def mark_roll(self, roll):
        print("\nFor each student, type 'a' for absent and 'p' for present.")
        for student in self.roll_manager.members:
            status = input(student.name + ": ").lower()
            completion = False
            while completion == False:
                if status == "a":
                    student.add_period()
                    student.add_absence()
                    completion = True
                    break
                elif status == "p":
                    student.add_period()
                    completion = True
                    break
                else:
                    print("Try again")
                    completion == False

    

#-----Implementation-----

if __name__ == "__main__":
    system = StudentAttendanceSystemFacade()

    print("\nWelcome to the Attendance System.")
    selection = input("Type 'continue' to enter main program. Type 'config' to configure information. Type 'exit' to quit.\n").lower()
    while selection:
        if selection == "config":
            config_action = input("\nWhat would you like to do?\n1. Create a new class\n2. Go back\n")
            while config_action:
                if config_action == "1":
                    name = input("\nClass name: ")
                    teacher = input("Teacher name (FirstLast): ")
                    system.create_class(name, teacher)
                    print("Class created.\n")
                    break
                elif config_action == "2":
                    break
                else:
                    print("Not an action.")
            selection = input("Type 'continue' to enter main program. Type 'config' to configure information.\n").lower()
        elif selection == "continue":
            action = input("\nWhat would you like to do? (enter number)...\n1. Mark a roll\n2. Access attendance data\n3. View attendance percentage\n")
            while action:
                if action == "1":
                    roll = input("\nWhat class would you like to mark? ")
                    system.mark_roll(roll)
                    action = input("\nWhat would you like to do? (enter number)...\n1. Mark a roll\n2. Access attendance data\n3. View attendance percentage\n4. Go back\n")
                elif action == "2":
                    student = input("\nStudent: ")
                    system.attendance_notify(student)
                    action = input("\nWhat would you like to do? (enter number)...\n1. Mark a roll\n2. Access attendance data\n3. View attendance percentage\n4. Go back\n")
                elif action == "3":
                    student = input("\nStudent: ")
                    system.attendance_report(student)
                    action = input("\nWhat would you like to do? (enter number)...\n1. Mark a roll\n2. Access attendance data\n3. View attendance percentage\n4. Go back\n")
                elif action == "4":
                    selection = input("Type 'continue' to enter main program. Type 'config' to configure information.\n").lower()
        elif selection == "quit":
            quit()
        else:
            print("Not an option.")

