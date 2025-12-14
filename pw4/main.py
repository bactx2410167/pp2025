from input import input_stunum
from input import input_coursenum
from input import input_mark
from input import show_mark
from input import list_stu
from input import list_cor
from input import list_mark

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
            list_cor()
        elif choice == '5':
            list_stu()
        elif choice == '6':
            list_mark()
        elif choice == '7':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()