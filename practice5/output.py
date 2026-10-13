import curses

def list_students(stdscr, school):
    stdscr.addstr("\nList of Students:\n", curses.A_BOLD)
    for student in school.students:
        stdscr.addstr(f"{student}\n")
    stdscr.refresh()

def list_courses(stdscr, school):
    stdscr.addstr("\nList of Courses:\n", curses.A_BOLD)
    for course in school.courses:
        stdscr.addstr(f"{course}\n")
    stdscr.refresh()

def show_student_marks(stdscr, school, get_input_func):
    stdscr.clear()
    if not school.courses:
        stdscr.addstr("No courses available.\n")
        return

    list_courses(stdscr, school)
    selected_course_id = get_input_func(stdscr, "\nEnter course ID to view marks: ")
    selected_course = next((c for c in school.courses if c.course_id == selected_course_id), None)

    if not selected_course:
        stdscr.addstr("Course not found.\n")
        return

    stdscr.addstr(f"\nMarks for Course: {selected_course.name}\n", curses.A_BOLD)
    for student in school.students:
        if selected_course_id in student.marks:
            stdscr.addstr(f"Student ID: {student.student_id}, Name: {student.name}, Mark: {student.marks[selected_course_id]}\n")
    stdscr.refresh()

def sort_students_by_gpa(stdscr, school):
    stdscr.clear()
    for student in school.students:
        student.calculate_gpa(school.courses)
    school.students.sort(key=lambda x: x.gpa, reverse=True)
    
    stdscr.addstr("\nStudents sorted by GPA:\n", curses.A_BOLD)
    list_students(stdscr, school)
    stdscr.refresh()

def save_data(school):
    with open("students.txt", "w") as f:
        for student in school.students:
            f.write(f"{student.student_id},{student.name},{student.dob}\n")
            
    with open("courses.txt", "w") as f:
        for course in school.courses:
            f.write(f"{course.course_id},{course.name},{course.credits}\n")
            
    with open("marks.txt", "w") as f:
        for student in school.students:
            for course_id, mark in student.marks.items():
                f.write(f"{student.student_id},{course_id},{mark}\n")

import zipfile

def compress_data():
    with zipfile.ZipFile("students.dat", "w") as zf:
        zf.write("students.txt")
        zf.write("courses.txt")
        zf.write("marks.txt")