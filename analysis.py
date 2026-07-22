#LOAD DATASET
import pandas as pd

df = pd.read_csv("student_habits_analysis/student_habits_analysis.csv")
print(df)
print("Dataset Shape:")
print(df.shape)
print("Dataset Info:")
df.info()

#CREATION OF NEW COLUMN

def get_Performance_Status(Score):
    if Score >= 80:
        return "Excellent"
    elif Score >= 50:
        return "Average"
    else:
        return "Poor"
df["Performance_Status"] = df["Score"].apply(get_Performance_Status)
print(df["Performance_Status"])

#FILTERING

print("Student with the highest attendance:" ,df["Attendance"].max())  
print("\nAverage Score:" ,df["Score"].mean()) 
print("\nStudents studying above average hours:") 
print(df[df["Study_Hours"] > df["Study_Hours"].mean()])

#VISUALIZATION
import matplotlib.pyplot as plt
plt.figure()
plt.bar(df['Name'], df['Score'])
plt.xlabel('Name')
plt.ylabel('Scores')
plt.title('Bar Chart of Scores')
plt.savefig("Student_Habits_Analysis_Bar_Chart.png")
plt.show()
plt.figure()
plt.plot(df['Name'], df['Study_Hours'])
plt.xlabel('Name')
plt.ylabel('Study_Hours')
plt.title('Line Charts of Study Hours')
plt.savefig("Student_Habits_Analysis_Line_Chart.png")
plt.show()
plt.figure()
plt.pie(df['Performance_Status'].value_counts(), labels=df['Performance_Status'].unique(), autopct='%1.1f%%')
plt.title('Pie Chart of Performance_Status Counts')
plt.savefig("Student_Habits_Analysis_Pie_Chart.png")
plt.show()