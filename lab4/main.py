import curses
from domains.models import School
import input
import output

def main(stdscr):
    stdscr.scrollok(True)
    school = School()
    
    input.input_students(stdscr, school)
    input.input_courses(stdscr, school)

    while True:
        input.input_marks(stdscr, school, output.list_courses)
        ans = input.get_input(stdscr, "\nDo you want to input marks for another course? (y/n): ")
        if ans.lower() != 'y':
            break

    while True:
        output.show_student_marks(stdscr, school, input.get_input)
        ans = input.get_input(stdscr, "\nDo you want to view marks for another course? (y/n): ")
        if ans.lower() != 'y':
            break

    output.sort_students_by_gpa(stdscr, school)
    
    stdscr.addstr("\nPress any key to exit...", curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)