student = []
course = []
mark = []

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
        print(f'{self.id}: {self.name}, DOB: {self.dob}')

def input_stunum():
    n = int(input('Input number of students: '))
    for i in range(n):
        i = Student()
        i.input()
        student.append(i)

class Course:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def input(self):
        self.id = input('Course ID: ')
        self.name = input('Course Name: ')

    def list(self):
        print(f'{self.id}: {self.name}')

def input_coursenum():
    n = int(input('Input number of courses: '))
    for i in range(n):
        i = Course()
        i.input()
        course.append(i)

def input_mark():
    course_id = input('Input Course ID to enter marks: ')
    for c in course:
        if c.id == course_id:
            for s in student:
                m = float(input(f'Input mark for {s.name} (ID: {s.id}): '))
                if m < 0:
                    print('Invalid mark')
                    return
                mark.append({'student_id': s.id, 'course_id': course_id, 'mark': m})
            return
    print('Course ID not found.')

def show_mark():
    course_id = input('Input Course ID to show marks: ')
    for c in course:
        if c.id == course_id:
            print(f'Marks for {c.name}:')
            for m in mark:
                if m['course_id'] == course_id:
                    for s in student:
                        if s.id == m['student_id']:
                            print(f'{s.name} (ID: {s.id}): {m['mark']}')
            return
    print('Course ID not found.')

def main():
    while True:
        print('1. Input number of students')
        print('2. Input number of courses')
        print('3. Input marks for a course')
        print('4. List all courses')
        print('5. List all students')
        print('6. Show marks for a course')
        print('7. Exit')
        choice = input('Choose: ')
        if choice == '1':
            input_stunum()
        elif choice == '2':
            input_coursenum()
        elif choice == '3':
            input_mark()
        elif choice == '4':
            for i in course:
                Course.list(i)
        elif choice == '5':
            for i in student:
                Student.list(i)
        elif choice == '6':
            show_mark()
        elif choice == '7':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()