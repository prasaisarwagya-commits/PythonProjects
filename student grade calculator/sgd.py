# Question 1: Student Grade Calculator

# Write a Python program that accepts a student's name and marks in three subjects.

# Requirements:

# - Calculate total marks and average.
# - Use conditional statements to determine the grade.
# - Create a function to calculate the average and return the result.
# - Display the student's name, total marks, average, and grade.
# - Validate that marks are between 0 and 100.



def average_marks(m1 , m2 , m3):
    return (m1 + m2+m3)/3



def main ():
    print('\n--STUDENT GRADE CALCULATOR--')
    print()
    student_name = input('Enter your name: ').capitalize()

    while True:
        try:
         mark1 = float(input('Enter your mark in subject1: '))
         if mark1 >=0 and mark1 <=100:
             break 
         print('Marks should be within 0-100. Please insert your correct mark. ')
        except ValueError:
         print('Invalid marks. Please insert valid input.')



    while True:
       try:
          mark2 = float(input('Enter your mark in subject2: '))
          if mark2 >=0 and mark2 <=100:
             break
          print('Marks should be within 0-100. Please insert your correct mark.')
       except ValueError:
          print('Invalid marks. Please insert valid input.')
         
         
    while True:
       try:
          mark3 = float(input('Enter your mark in subject3: '))
          if mark3 >=0 and mark3 <=100:
             break
          print('Marks should be within 0-100. Please insert your correct mark.')
       except ValueError:
           print('Invalid marks. Please insert valid input.')


    total_marks = mark1 + mark2 + mark3

    average_mark = average_marks(mark1 , mark2 , mark3)


    if average_mark > 90:
       grade = 'A'
    elif average_mark >= 80:
        grade = 'B'
    elif average_mark >= 70:
        grade = 'C'
    elif average_mark >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print()
    print(f' --STUDENT REPORT  --')
    print(f' Student name: {student_name}')
    print(f'Total marks obtained: {total_marks}')
    print(f'Average marks obtained: {average_mark:.2f}')
    print(f'Grade Obtained: {grade}')



   


    



    
    

main()

 