def input_students():
    n_student = int(input("Number of students: "))

    students = []

    for i in range(n_student):
        student_id = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Student DoB: ")

        students.append((student_id, name, dob))

    return students


def input_courses():
    n_course = int(input("Number of courses: "))

    courses = []

    for i in range(n_course):
        course_id = input("Course ID: ")
        course_name = input("Course name: ")

        courses.append((course_id, course_name))

    return courses


def list_students(students):
    print("\nStudents:")

    for student in students:
        print(
            "ID:", student[0],
            "Name:", student[1],
            "DoB:", student[2]
        )


def list_courses(courses):
    print("\nCourses:")

    for course in courses:
        print(
            "Course ID:", course[0],
            "Course name:", course[1]
        )


def input_marks(students, courses):
    print("\nSelect a course:")

    for course in courses:
        print(
            "Course ID:", course[0],
            "-",
            "Course name:", course[1]
        )

    selected_course = input("Enter course ID to select: ")

    marks = {}

    for course in courses:
        if course[0] == selected_course:

            print("\nEnter marks for", course[1])

            marks[selected_course] = {}

            for student in students:
                mark = float(
                    input(f"Enter mark for {student[1]}: ")
                )

                marks[selected_course][student[0]] = mark

            return marks

    print("Course not found.")
    return {}


def show_student_marks(students, courses, marks):
    print("\nStudents with marks:")

    for course_id in marks:
        course_name = ""

        for course in courses:
            if course[0] == course_id:
                course_name = course[1]

        print("\nCourse:", course_name)

        for student in students:
            student_id = student[0]
            student_name = student[1]

            mark = marks[course_id][student_id]

            print(
                "Student ID:", student_id,
                "Name:", student_name,
                "Mark:", mark
            )


students = input_students()

courses = input_courses()

list_students(students)

list_courses(courses)

marks = input_marks(students, courses)

show_student_marks(students, courses, marks)