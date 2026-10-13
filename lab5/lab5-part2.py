import pandas as pd

df_students = pd.read_csv('students.csv')
df_scores = pd.read_csv('scores.csv')

print("Missing values in students data sheet")
print(df_students.isnull().sum())
print("\nMissing values in score datasheet")
print(df_scores.isnull().sum())

df_students_clean = df_students.dropna()
df_scores_clean = df_scores.dropna()

df_merged = pd.merge(df_students_clean, df_scores_clean, on = 'student_id')

score_columns = [col for col in df_scores.columns if col != 'student_id']
df_merged['average_score'] = df_merged[score_columns].mean(axis=1)

top_5_students = df_merged.sort_values(by='average_score', ascending=False).head(5)
print("\nTop 5 Students by Average Score: ")

print(top_5_students[['name', 'average_score']])

avg_score_by_major = df_merged.groupby('major')['average_score'].mean()
print("\nAverage Score by Major:")
print(avg_score_by_major)





