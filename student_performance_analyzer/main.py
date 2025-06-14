import csv

#defining a student class to represent each student's data

class Student :
    def __init__(self,name,math,science,english):
        #initialising the student's attributes
        self.name=name
        self.math=math
        self.science=science
        self.english=english

        #now we have to store the average score during object creation
        self.average=self.calculate_average()

    def calculate_average(self):
        #this is a ethod to calcualte and return average of 3 sub
        return round((self.math+self.science+self.english)/3,2) #here we are rounding the result to 2 decimal places.
    
    def get_scores(self):
        #returning all scores and avg as a dictionary for display
        return {
            'Math': self.math,
            'Science': self.science,
            'English': self.english,
            'Average': self.average
        }
    

#now we will write function to read  student data from csv file and create student objects.

def read_student_data(filename): #here we use filename as a parameter makes the function reusable for any file.

    students=[]
    with open(filename, 'r') as file:
        reader = csv.DictReader(file) #reads csv rows as dictionarie

        for row in reader:
            #now creating a student object for each row and add it to the list
            student= Student(
                name=row['Name'],
                math=int(row['Math']),
                science=int(row['Science']),
                english=int(row['English'])
            )

            students.append(student)

    return students #return the list of student objects


#now we will create function to calculate avg score per sub across all student

def calculate_subject_averages(students):
    #using list comprehensions to sum all scores for each subject

    total_math= sum(s.math for s in students)
    total_science= sum(s.science for s in students)
    total_english = sum(s.english for s in students)
    count= len(students)  #total number of students

    #return sub-wise avg in a dictionary

    return {

        'Math': round(total_math/ count, 2),
        'Science': round(total_science/count, 2),
        'English': round(total_english/count, 2)
    }

#function to find the top and bottom performing students

def find_top_bottom_students(students):

    #use max and min with key as the student's avg


    top_student= max(students, key= lambda s: s.average)
    bottom_student= min(students, key=lambda s: s.average)
    return top_student, bottom_student


#now we erite function to display the report in a readable format

def print_report(students,subject_averages, top_student, bottom_student):
    print("\n Student Performance Report \n")

    #print each student's scores and avg

    for student in students:

        scores= student.get_scores()

        print(f"{student.name}: Math={scores['Math']}, Science={scores['Science']},"
              f"English={scores['English']}, Average={scores['Average']}")

    #print avg scores for each sub

    print("\nSubject Averages: ")
    for subject, avg in subject_averages.items():
        print(f"{subject}:{avg}")


    #print the top and bottom performer 

    print(f" \n Top Performer: {top_student.name} with Average= {top_student.average}")
    print(f" Lowest Performer: {bottom_student.name} with Average ={bottom_student.average}")


#main program execution



students= read_student_data('data.csv')

subject_averages= calculate_subject_averages(students)


top_student, bottom_student = find_top_bottom_students(students)

print_report(students, subject_averages, top_student,bottom_student)








