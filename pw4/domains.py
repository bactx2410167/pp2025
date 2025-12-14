class Student:
    def __init__(self, id=None, name=None, dob=None):
        self.id = id
        self.name = name
        self.dob = dob
    
    def input(self):
        self.id = input('Student ID: ')
        self.name = input('Student Name: ')
        self.dob = input('Date of birth: ')

    def list(self):
        from input import gpa_calc
        print(f'{self.id}: {self.name}, DOB: {self.dob}, GPA: {gpa_calc(self.id)}')

class Course:
    def __init__(self, id=None, name=None, credit=0):
        self.id = id
        self.name = name
        self.credit = credit

    def input(self):
        self.id = input('Course ID: ')
        self.name = input('Course Name: ')
        try:
            self.credit = int(input('Course Credit: '))
        except ValueError:
            print('Invalid credit')
            return

    def list(self):
        print(f'{self.id}: {self.name} ({self.credit} Credits)')
