#initialize a empty list to store student data
students = []

def add_student():
    name = input("enter the student's name:")
    marks = []
    for subject in ["Math", "Science", "English"]:
        mark = int(input(f"enter the marks for {subject}: "))
        marks.append(mark)
    total, average = calculate_total_and_average(marks)
    status = determine_pass_fail(average)
    student = {"name": name, "marks": marks, "total": total, "average": average, "status": status}
    students.append(student)
    print(f"student {name} added successfully!\n")

#function to calculate total and average marks
def calculate_total_and_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

#function to determine pass and fail
def determine_pass_fail(average):
    return "pass" if average>=40 else "fail"

#function to display all student's details
def display_students():
    if not students:
        print("No students in record.\n")
        return
    print("\nStudents Details:")
    print("Name\t\tMath\tScience\tEnglish\tTotal\tAverage\tStatus")
    for student in students:
        print(f"{student['name']}\t\t{student['marks'][0]}\t{student['marks'][1]}\t{student['marks'][2]}\t{student['total']}\t{student['average']:.2f}\t{student['status']}")
    print()

#main program loop
while True:
    print("\nMENU:")
    print("1. Add a Student.")
    print("2. View All Students.")
    print("3. Exit")
    choice = int(input("enter your choice:"))
    if choice==1:
        add_student()
    elif choice==2:
        display_students()
    elif choice==3:
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.\n")