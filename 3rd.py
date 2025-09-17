class Student:
    def __init__(self, name):
        self.name = name
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


class Roll:
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