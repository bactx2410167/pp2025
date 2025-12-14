import math
import numpy as np
from domains import Student
from domains import Course

student = []
course = []
mark = []

def list_stu():
    if not student:
        print('No students. Please input some students.')
        input_stunum()
    else:
        print('List of students (sorted by GPA descending): ')
        student.sort(key=lambda s: gpa_calc(s.id), reverse=True)
        for i in student:
            Student.list(i)

def list_cor():
    if not course:
        print('No courses. Please input some courses.')
        input_coursenum()
    else:
        print('List of courses: ')
        for i in course:
            Course.list(i)

def list_mark():
    if not mark:
        print('No marks.')
    else:
        show_mark()

def input_stunum():
    n = int(input('Input number of students: '))
    for i in range(n):
        i = Student()
        i.input()
        student.append(i)

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
                try:
                    m = float(input(f'Input mark for {s.name} (ID: {s.id}): '))
                except ValueError:
                    print('Invalid mark')
                    return
                m2 = math.floor(m * 10) / 10.0
                mark.append({'student_id': s.id, 'course_id': course_id, 'mark': m2})
            return
    print('Course ID not found.')

def gpa_calc(id):
    gpa_mark = []
    gpa_cred = []
    for m in mark:
        if m['student_id'] == id:
            gpa_mark.append(m['mark'])
            for c in course:
                if c.id == m['course_id']:
                    gpa_cred.append(c.credit)
                    break
    if not gpa_mark:
        return 'N/A'
    return round(float(np.sum(np.array(gpa_mark) * np.array(gpa_cred)) / np.sum(np.array(gpa_cred))), 2)

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
