import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def add_mark(self, course_id, mark):
        self.marks[course_id] = math.floor(mark * 10) / 10

    def calculate_gpa(self, courses):
        if not self.marks:
            self.gpa = 0.0
            return

        course_marks = []
        course_credits = []

        for course in courses:
            if course.course_id in self.marks:
                course_marks.append(self.marks[course.course_id])
                course_credits.append(course.credits)

        if not course_credits:
            self.gpa = 0.0
            return

        marks_array = np.array(course_marks)
        credits_array = np.array(course_credits)

        total_credits = np.sum(credits_array)
        if total_credits == 0:
            self.gpa = 0.0
        else:
            self.gpa = np.sum(marks_array * credits_array) / total_credits

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.2f}"

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Credits: {self.credits}"

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def get_input(self, stdscr, prompt):
        # Hàm hỗ trợ để thay thế chức năng của input() mặc định
        stdscr.addstr(prompt)
        stdscr.refresh()
        curses.echo()
        s = stdscr.getstr().decode('utf-8')
        curses.noecho()
        stdscr.addstr("\n")
        return s

    def input_students(self, stdscr):
        stdscr.clear()
        num_str = self.get_input(stdscr, "Enter the number of students: ")
        try:
            num_students = int(num_str)
        except ValueError:
            num_students = 0
            
        for _ in range(num_students):
            student_id = self.get_input(stdscr, "Enter student ID: ")
            name = self.get_input(stdscr, "Enter student name: ")
            dob = self.get_input(stdscr, "Enter student DoB (YYYY-MM-DD): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self, stdscr):
        stdscr.clear()
        num_str = self.get_input(stdscr, "Enter the number of courses: ")
        try:
            num_courses = int(num_str)
        except ValueError:
            num_courses = 0

        for _ in range(num_courses):
            course_id = self.get_input(stdscr, "Enter course ID: ")
            name = self.get_input(stdscr, "Enter course name: ")
            credits_str = self.get_input(stdscr, "Enter course credits: ")
            try:
                credits = int(credits_str)
            except ValueError:
                credits = 0
            self.courses.append(Course(course_id, name, credits))

    def list_students(self, stdscr):
        stdscr.addstr("\nList of Students:\n", curses.A_BOLD)
        for student in self.students:
            stdscr.addstr(f"{student}\n")
        stdscr.refresh()

    def list_courses(self, stdscr):
        stdscr.addstr("\nList of Courses:\n", curses.A_BOLD)
        for course in self.courses:
            stdscr.addstr(f"{course}\n")
        stdscr.refresh()

    def input_marks(self, stdscr):
        stdscr.clear()
        if not self.students or not self.courses:
            stdscr.addstr("No students or courses available.\n")
            return

        self.list_courses(stdscr)
        selected_course_id = self.get_input(stdscr, "\nEnter the course ID to input marks for: ")
        selected_course = next((c for c in self.courses if c.course_id == selected_course_id), None)
        
        if not selected_course:
            stdscr.addstr("Invalid course ID.\n")
            return

        stdscr.addstr(f"\nInput marks for course: {selected_course.name}\n", curses.A_BOLD)
        for student in self.students:
            mark_str = self.get_input(stdscr, f"Enter mark for {student.name}: ")
            try:
                mark = float(mark_str)
                student.add_mark(selected_course_id, mark)
            except ValueError:
                stdscr.addstr("Invalid mark. Skipping.\n")

    def show_student_marks(self, stdscr):
        stdscr.clear()
        if not self.courses:
            stdscr.addstr("No courses available.\n")
            return

        self.list_courses(stdscr)
        selected_course_id = self.get_input(stdscr, "\nEnter course ID to view marks: ")
        selected_course = next((c for c in self.courses if c.course_id == selected_course_id), None)

        if not selected_course:
            stdscr.addstr("Course not found.\n")
            return

        stdscr.addstr(f"\nMarks for Course: {selected_course.name}\n", curses.A_BOLD)
        for student in self.students:
            if selected_course_id in student.marks:
                stdscr.addstr(f"Student ID: {student.student_id}, Name: {student.name}, Mark: {student.marks[selected_course_id]}\n")
        stdscr.refresh()

    def sort_students_by_gpa(self, stdscr):
        stdscr.clear()
        for student in self.students:
            student.calculate_gpa(self.courses)
        self.students.sort(key=lambda x: x.gpa, reverse=True)
        
        stdscr.addstr("\nStudents sorted by GPA:\n", curses.A_BOLD)
        self.list_students(stdscr)
        stdscr.refresh()

# --- Main Program ---
def main(stdscr):
    # Cho phép thiết bị đầu cuối cuộn nội dung nếu dài hơn khung hình
    stdscr.scrollok(True)
    school = School()
    
    school.input_students(stdscr)
    school.input_courses(stdscr)

    while True:
        school.input_marks(stdscr)
        ans = school.get_input(stdscr, "\nDo you want to input marks for another course? (y/n): ")
        if ans.lower() != 'y':
            break

    while True:
        school.show_student_marks(stdscr)
        ans = school.get_input(stdscr, "\nDo you want to view marks for another course? (y/n): ")
        if ans.lower() != 'y':
            break

    school.sort_students_by_gpa(stdscr)
    
    stdscr.addstr("\nPress any key to exit...", curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    # curses.wrapper khởi tạo tự động stdscr và khôi phục giao diện terminal gốc khi tắt
    curses.wrapper(main)
