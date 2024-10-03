def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_max_min(numbers):
    return max(numbers), min(numbers)

# Dictionary to store student information
students = {}

# Main program loop
while True:
    # Display menu options
    print("\n1. Add student")
    print("2. View student")
    print("3. Calculate class average")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        grades = input("Enter student grades (separated by commas): ")
        grades = [float(grade) for grade in grades.split(',')]
        students[name] = grades
        print(f"Student {name} added successfully!")

    elif choice == '2':
        name = input("Enter student name: ")
        if name in students:
            print(f"Grades for {name}: {students[name]}")
        else:
            print(f"Student {name} not found!")

    elif choice == '3':
        if students:
            all_grades = [grade for grades in students.values() for grade in grades]
            print(f"Class average: {calculate_average(all_grades):.2f}")
            max_grade, min_grade = find_max_min(all_grades)
            print(f"Maximum grade: {max_grade:.2f}")
            print(f"Minimum grade: {min_grade:.2f}")
        else:
            print("No students added yet!")

    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again!")