# Student Performance Analyzer

This is a Python project that analyzes student performance data from a CSV file. It calculates individual and subject-wise average scores, and determines the top and bottom performers. The project demonstrates practical use of object-oriented programming, file handling, and basic data analysis in Python.

---
##  Concepts Used

- **Classes and Object-Oriented Programming**  
  Used to encapsulate student data and related behavior (like calculating averages).

- **File I/O and CSV Reading using `csv.DictReader`**  
  Reads structured student data from a CSV file into Python dictionaries.

- **List Comprehensions**  
  Efficiently aggregates scores across all student objects for averaging.

- **Lambda Functions**  
  Utilized for sorting and identifying top/bottom performers based on average scores.

- **Data Aggregation and Reporting**  
  Calculates subject-wise and student-wise averages, and presents the data in a readable format.

## Features

- Reads student records from a CSV file.
- Calculates each student's average score in:
  - Math
  - Science
  - English
- Computes subject-wise average scores across all students.
- Identifies the top and lowest performing students based on average.
- Displays a neatly formatted performance report.


##  How It Works

### 1. `Student` Class
Represents each student and stores:
- Name
- Subject scores (Math, Science, English)
- Automatically calculates the average score during initialization

### 2. `read_student_data(filename)`
- Reads the CSV file using Python's `csv.DictReader`
- Creates a list of `Student` objects from the file data

### 3. `calculate_subject_averages(students)`
- Aggregates all students' scores
- Calculates and returns the average score for each subject

### 4. `find_top_bottom_students(students)`
- Identifies the top-performing student (highest average)
- Identifies the lowest-performing student (lowest average)

### 5. `print_report(students, subject_averages, top_student, bottom_student)`
- Displays each student's subject scores and average
- Prints subject-wise average scores
- Highlights the top and bottom performers in the report

 


## Sample Output

**Student Performance Report**

Arnab: Math = 85, Science = 78, English = 92, Average = 85.0  
Oman: Math = 70, Science = 88, English = 75, Average = 77.67  
Pratik: Math = 95, Science = 85, English = 85, Average = 88.33  
Sindh: Math = 89, Science = 78, English = 92, Average = 86.33  

**Subject Averages:**  
- Math: 84.75  
- Science: 82.25  
- English: 86.0  

**Top Performer:** Pratik with Average = 88.33  
**Lowest Performer:** Oman with Average = 77.67



 ## Project Structure

```bash
student-performance-analyzer/
├── data.csv        # Input CSV file containing student data
├── main.py         # Python script with all functionalities
└── README.md       # Project documentation


