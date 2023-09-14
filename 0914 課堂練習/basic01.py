import pandas as pd

csv_file_path_PL = 'PL.csv'
csv_file_path_WEB = 'WEB.csv'

df_PL = pd.read_csv(csv_file_path_PL)
df_WEB = pd.read_csv(csv_file_path_WEB)

student_names_PL = df_PL['姓名']
student_names_WEB = df_WEB['姓名']

student_names_PL_set = set(student_names_PL)
student_names_WEB_set = set(student_names_WEB)

print(student_names_PL_set&student_names_WEB_set)
