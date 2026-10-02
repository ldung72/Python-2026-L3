import curses
from domains.models import Student, Course

def get_input(stdscr, prompt):
    stdscr.addstr(prompt)
    stdscr.refresh()
    curses.echo()
    s = stdscr.getstr().decode('utf-8')
    curses.noecho()
    stdscr.addstr("\n")
    return s

def input_students(stdscr, school):
    stdscr.clear()
    num_str = get_input(stdscr, "Enter the number of students: ")
    try:
        num_students = int(num_str)
    except ValueError:
        num_students = 0
        
    for _ in range(num_students):
        student_id = get_input(stdscr, "Enter student ID: ")
        name = get_input(stdscr, "Enter student name: ")
        dob = get_input(stdscr, "Enter student DoB (YYYY-MM-DD): ")
        school.students.append(Student(student_id, name, dob))

def input_courses(stdscr, school):
    stdscr.clear()
    num_str = get_input(stdscr, "Enter the number of courses: ")
    try:
        num_courses = int(num_str)
    except ValueError:
        num_courses = 0

    for _ in range(num_courses):
        course_id = get_input(stdscr, "Enter course ID: ")
        name = get_input(stdscr, "Enter course name: ")
        try:
            credits = int(get_input(stdscr, "Enter course credits: "))
        except ValueError:
            credits = 0
        school.courses.append(Course(course_id, name, credits))

def input_marks(stdscr, school, list_courses_func):
    stdscr.clear()
    if not school.students or not school.courses:
        stdscr.addstr("No students or courses available.\n")
        return

    list_courses_func(stdscr, school)
    selected_course_id = get_input(stdscr, "\nEnter the course ID to input marks for: ")
    selected_course = next((c for c in school.courses if c.course_id == selected_course_id), None)
    
    if not selected_course:
        stdscr.addstr("Invalid course ID.\n")
        return

    stdscr.addstr(f"\nInput marks for course: {selected_course.name}\n", curses.A_BOLD)
    for student in school.students:
        try:
            mark = float(get_input(stdscr, f"Enter mark for {student.name}: "))
            student.add_mark(selected_course_id, mark)
        except ValueError:
            stdscr.addstr("Invalid mark. Skipping.\n")