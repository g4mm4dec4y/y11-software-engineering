#defines the student class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Defining the attendance manager class within the student class allows each student to have their separate attendances.
        self.attendance = AttendanceManager()
#defines the teacher class
class Teacher:
    def __init__(self, name):
        self.name = name
    classes = []
#Not actually functional.

#defines the roll class
class Roll:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

#manages students on the roll
class RollManager:
    def __init__(self):
        self.members = []
#defining adding a student function
    def add_student(self, student, studentage):
        if student in self.members:
            raise ValueError("Student already exists.")
        self.members.append(Student(student, studentage))
#defines removing a student function
    def remove_student(self, student):
        if student not in self.members:
            raise ValueError("Student doesn't exist.")
        self.members.remove(student)

    def get_student(self, name):
        for student in self.members:
            if student.name == name:
                return student

#gets all information from created class
class RollDatabase:
    def __init__(self):
        self.storage = []

    def add_class(self, name, teacher):
        self.storage.append(Roll(name, teacher))

#tracks the attendance for students
class AttendanceManager():
    def __init__(self):
        self.absences = 0
        self.latenesses = 0
        self.total_periods = 0
#defines adding attendances to a student
    def add_absence(self):
        self.absences += 1
#defines adding a period to a student
    def add_period(self):
        self.total_periods = self.total_periods + 1
#calculates the percentage of periodsa a student has attended
    def calc_attendance(self):
        return (self.total_periods - self.absences)/self.total_periods * 100
    

#-----Facade-----

#defines the actual facade system
class StudentAttendanceSystemFacade:
    def __init__(self):
        self.database = RollDatabase()
        self.roll_manager = RollManager()
#defines the class creation function
    def create_class(self, name, teacher):
        self.database.add_class(name, teacher)
        amount = int(input("\nHow many students are in the class?: "))
        while amount != 0:
            name = input("Enter name (FirstLast): ")
            age = str(input("Enter age: "))
            self.roll_manager.add_student(name, age)
            amount = amount - 1
#defines the attendance report
    def attendance_report(self, name):
        student = self.roll_manager.get_student(name)
        attendance = "Student has attended " + str((student.attendance.total_periods - student.attendance.absences)) + " out of " + str(student.attendance.total_periods) + " classes."
        print(attendance)
#finds the attendance percent
    def attendance_percent(self, name):
        student = self.roll_manager.get_student(name)
        percent = student.attendance.calc_attendance()
        print("Student attendance is at " + str(percent) + "%")
#defines the roll marking system
    def mark_roll(self):
        print("\nFor each student, type 'a' for absent and 'p' for present.")
        for student in self.roll_manager.members:
            status = input(student.name + ": ").lower()
            completion = False
            while completion == False:
                if status == "a":
                    student.attendance.add_period()
                    student.attendance.add_absence()
                    completion = True
                    break
                elif status == "p":
                    student.attendance.add_period()
                    completion = True
                    break
                else:
                    print("Try again")
                    completion == False

            if student.attendance.total_periods >= 0:
                attendance_percent = student.attendance.calc_attendance()
                if attendance_percent <= 70:
                    print(student.name, "'s attendance is below 70 percent and is", attendance_percent)


#-----Implementation-----

if __name__ == "__main__":
    system = StudentAttendanceSystemFacade()
#intro to the system
    print("\nWelcome to the Attendance System.")
    selection = input("Type 'continue' to enter main program. Type 'config' to configure information. Type 'exit' to quit.\n").lower()
#creates a loop
    while selection:
        if selection == "config":
            config_action = input("\nWhat would you like to do?\n1. Create a new class\n2. Go back\n")
	#starts a config loop until exited
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
	#starts loop for the rolls
        elif selection == "continue":
            action = input("\nWhat would you like to do? (enter number)...\n1. Mark a roll\n2. Access attendance data\n3. View attendance percentage\n")
            while action != "exit":
                if action == "1":
                    roll = input("\nWhat class would you like to mark? ")
                    system.mark_roll()
                    action = input("\nWhat would you like to do? (enter number)...\n1. Mark a roll\n2. Access attendance data\n3. View attendance percentage\n4. Go back\n")
                elif action == "2":
                    student = input("\nStudent: ")
                    system.attendance_report(student)
                    action = input("\nWhat would you like to do? (enter number)...\n1. Mark a roll\n2. Access attendance data\n3. View attendance percentage\n4. Go back\n")
                elif action == "3":
                    student = input("\nStudent: ")
                    system.attendance_percent(student)
                    action = input("\nWhat would you like to do? (enter number)...\n1. Mark a roll\n2. Access attendance data\n3. View attendance percentage\n4. Go back\n")
                elif action == "4":
                    selection = input("Type 'continue' to enter main program. Type 'config' to configure information.\n").lower()
            selection = input("Type 'continue' to enter main program. Type 'config' to configure information. Type 'exit' to quit.\n").lower()
#exits the loop
        elif selection == "quit":
            quit()
        else:
            print("Not an option.")
