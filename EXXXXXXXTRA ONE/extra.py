import pandas as pd


students_data = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Mr. Volunteers', 'Charlie'],
    'age': [20, 22, 21]
})

courses_data = pd.DataFrame({
    'course_id': ['C1', 'C2', 'C3'],
    'title': ['Python Basics', 'Data Science', 'Machine Learning']
})

mark_data = pd.DataFrame({
    'student_id': [1, 2, 3],
    'course_id': ['C1', 'C2', 'C3'],
    'mark': [85, 95, 78]
})

students_data.to_csv('students.txt', index=False)
courses_data.to_csv('courses.txt', index=False)
mark_data.to_csv('marks.txt', index=False)

def custom_query(dataframe, condition_string):
    """
    Allows users to enter string conditions and returns the filtered dataframe.
    """
    try:
        result = dataframe.query(condition_string)
        return result
    except Exception as e:
        return f"Error executing query: {e}"

user_input_condition = 'name == "Mr. Volunteers"' 

print("--- Executing Query ---")
print(f"Condition: {user_input_condition}\n")

query_result = custom_query(students_data, user_input_condition)
print(query_result)