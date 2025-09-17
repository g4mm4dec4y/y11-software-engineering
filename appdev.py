#defines the student classs
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Defining the attendance manager class within the student class allows each student to have their separate attendance data.
        self.attendance = AttendanceManager()


#defines the roll class
class Roll:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.roll_manager = RollManager()
    

#manages students on the roll
class RollManager:
    def __init__(self):
        self.members = []
#defining function to add a student
    def add_student(self, student, studentage):
        if student in self.members:
            raise ValueError("Student already exists.")
        self.members.append(Student(student, studentage))
#defines function to remove a student (not implemented in final program)
    def remove_student(self, student):
        if student not in self.members:
            raise ValueError("Student doesn't exist.")
        self.members.remove(student)
#Function returns a specified student for later use in obtaining percentages and attendance reports so that they are unique to the student
    def get_student(self, name):
        for student in self.members:
            if student.name == name:
                return student
            else:
                print("student doesn't exist.")
        

#gets all information from created class
class RollDatabase:
    def __init__(self):
        self.storage = [] #List to store all the classes

    def add_class(self, name, teacher):
        self.storage.append(Roll(name, teacher)) #Adds a class to the storage list

    def get_roll(self, name): #Returns specified roll for later use of selecting which roll to mark
        for roll in self.storage:
                if roll.name == name:
                   return roll
        return "n/a" #If roll doesn't exist, this value is returned

#Tracks and modifies attendance data for a student
class AttendanceManager():
    def __init__(self): #Initialises each student to start with no data; all values at 0
        self.absences = 0
        self.latenesses = 0
        self.total_periods = 0
#defines adding attendances to a student
    def add_absence(self):
        self.absences += 1
#defines adding a period to a student
    def add_period(self):
        self.total_periods = self.total_periods + 1
#calculates the percentage of periods a a student has attended.
    def calc_attendance(self):
        return (self.total_periods - self.absences)/self.total_periods * 100
    

#-----Facade-----

#defines the actual facade system
class StudentAttendanceSystemFacade:
    def __init__(self): #Initialises RollDatabase and RollManager functions within facade
        self.database = RollDatabase()
        self.roll_manager = RollManager()

#defines the class creation function
    def create_class(self, name, teacher):
        self.database.add_class(name, teacher) #Adds class name and teacher to database
        roll = self.database.get_roll(name)
        amount = int(input("\nHow many students are in the class?: "))
#User specifies how many students to add, and program iterates and creates a student until the counter is zero.
        while amount != 0:
            studentname = input("Enter name (FirstLast): ")
            age = str(input("Enter age: "))
            roll.roll_manager.add_student(studentname, age)
            amount = amount - 1
#function to print an attendance report (raw data of total classes and num of absences)
    def attendance_report(self, studentname):
        for roll in self.database.storage:
            student = roll.roll_manager.get_student(studentname)
            if student:
                attendance = "Student has attended " + str((student.attendance.total_periods - student.attendance.absences)) + " out of " + str(student.attendance.total_periods) + " classes."
                print(attendance)
            else:
                print("Student not found.")
#finds the attendance percent by referring to function within class AttendanceManager
    def attendance_percent(self, studentname):
        for roll in self.database.storage:
            student = roll.roll_manager.get_student(studentname)
            if student:
                percent = student.attendance.calc_attendance()
                print("Student attendance is at " + str(percent) + "%")
            else:
                print("Student not found.")
#defines the roll marking system
    def mark_roll(self, roll):
        roll = self.database.get_roll(roll)
        if roll == "n/a": #If class does not exist, program returns back instead of breaking.
            print("Class doesn't exist.")
            return
        print("\nFor each student, type 'a' for absent and 'p' for present.")
        for student in roll.roll_manager.members: #Iterates through all class members.
            status = input(student.name + ": ").lower() #.lower() function helps avoid confusion if user prints attendance using a capital letter
            completion = False #Completion of marking a particular student's attendance is initially set to be false 
            while completion == False:
#The while loop allows user to try again if they mistype 
                if status == "a":
                    student.attendance.add_period() #Total amount of classes is added to
                    student.attendance.add_absence() #Amount of absences is added to
                    completion = True
                    break
                elif status == "p":
                    student.attendance.add_period() #Only total classes are added to
                    completion = True
                    break
                else:
                    print("Try again")
                    completion == False

            if student.attendance.total_periods >= 0:
                attendance_percent = student.attendance.calc_attendance()
                if attendance_percent <= 70:
                    print("Alert: " + student.name + "'s attendance is below 70%. It is currently " + str(attendance_percent) + "%")
            


#-----Implementation-----

if __name__ == "__main__":
    system = StudentAttendanceSystemFacade()
#intro to the system
    print("\nWelcome to the Attendance System.")
    selection = input("Type 'continue' to enter main program. Type 'config' to configure information. Type 'exit' to quit.\n").lower()
#initial loop created that continues until user decides to quit
    while selection:
        if selection == "config":
            config_action = input("\nWhat would you like to do?\n1. Create a new class\n2. Go back\n")
	#starts a config loop to create classes and students for the main program.
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
            selection = input("Type 'continue' to enter main program. Type 'config' to configure information. Type 'exit' to quit.\n").lower()
	#starts loop for the actual attendance program; reliant on if/elif statements that determine what action user wants to take
        elif selection == "continue":
            action = input("\nWhat would you like to do? (enter number)...\n1. Mark a roll\n2. Access attendance data\n3. View attendance percentage\n")
            while action != "exit":
                if action == "1":
                    roll = input("\nWhat class would you like to mark? ")
                    system.mark_roll(roll)
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
                    selection = input("Type 'continue' to enter main program. Type 'config' to configure information. Type 'exit' to quit.\n").lower()
            selection = input("Type 'continue' to enter main program. Type 'config' to configure information. Type 'exit' to quit.\n").lower()
#user can select to exit the program through the quit() function
        elif selection == "exit":
            quit()
        else:
            print("Not an option.")