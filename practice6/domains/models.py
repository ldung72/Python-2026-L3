import math
import numpy as np

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
            
        course_marks = [self.marks[c.course_id] for c in courses if c.course_id in self.marks]
        course_credits = [c.credits for c in courses if c.course_id in self.marks]
        
        if not course_credits:
            self.gpa = 0.0
            return

        total_credits = np.sum(course_credits)
        if total_credits == 0:
            self.gpa = 0.0
        else:
            self.gpa = np.sum(np.array(course_marks) * np.array(course_credits)) / total_credits

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