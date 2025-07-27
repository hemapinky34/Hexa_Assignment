import pandas as pd


df = pd.read_csv("updated_college_student_placement_dataset.csv")

#################################################################################################################################################

# 1.How many students are in the dataset?

total_students = len(df)
print("1. Total students:", total_students)

#################################################################################################################################################

# 2. Display the number of male and female students.

gender_count = df['Gender'].value_counts()
print("\n2. Male and Female Count:\n", gender_count)

#################################################################################################################################################

#3.What is the average percentage in MBA?

avg_mba = df['MBA_Percentage'].mean()
print("\n3. Average MBA percentage:", round(avg_mba, 2))

#################################################################################################################################################

## 4. Students who scored > 80% in both SSC and HSC

high_scorers = df[(df['SSC_Percentage'] > 80) & (df['HSC_Percentage'] > 80)]
print("\n4. Students with >80% in SSC & HSC:\n", high_scorers)

#################################################################################################################################################

# 5. Students with prior work experience
experienced_students = df[df['Internship_Experience'] == 'Yes']
print("\n5. Students with prior internship experience:\n", experienced_students)

#################################################################################################################################################

# 6. Average MBA score per specialization
avg_mba_specialisation = df.groupby('specialisation')['MBA_Percentage'].mean()
print("\n6. Average MBA score per specialization:\n", avg_mba_specialisation)

##################################################################################################################################################

# 7. Count of placed vs not placed students

placement_status_count = df['Placement'].value_counts()
print("\n7. Placement count:\n", placement_status_count)

#################################################################################################################################################

# 8. Placement ratio per specialization

placement_ratio = df[df['status'] == 'Placed'].groupby('specialisation')['status'].count() / df.groupby('specialisation')['status'].count()
print("\n8. Placement ratio per specialization:\n", placement_ratio)

#################################################################################################################################################

# 9. Create new column 'placement_success'
def classify_success(row):
    if row['Placement'] == 'Placed':
        if row['Salary'] > 950000:
            return 'High'
        elif row['Salary'] <= 400000:
            return 'Average'
        else:
            return 'Moderate'
    else:
        return 'Unplaced'

df['Placement_success'] = df.apply(classify_success, axis=1)
print("\n9. Placement success column added:\n", df[['Placement', 'Salary', 'placement_success']].head())

#################################################################################################################################################

# 10. Degree percentage range that leads to highest average salary (for placed students)

placed_students = df[df['Placement'] == 'Yes']
def cgpa_range(CGPA):
    if CGPA < 6:
        return "<6"
    elif CGPA < 7:
        return "< 7"
    elif CGPA < 8:
        return "7-8"
    elif CGPA < 9:
        return "8-9"
    else:
        return "9+"
placed_students['cgpa_range'] = placed_students['CGPA'].apply(cgpa_range)
average_salary_by_cgpa = placed_students.groupby('cgpa_range')['Salary'].mean().sort_values(ascending= False)
print(average_salary_by_cgpa)
###################################################################################################################################################