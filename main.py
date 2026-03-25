
grades = {}
while True:
    print("""
        ****** choose an option *******
                1: Add student grade
                2: View all students
                3: Update grade
                4: Find student
                5: Show class average
                6: Exit 
""")
    choice = input("Enter your option: ")


    if choice == "1":
        student_name = input("Enter name: ")
        student_grade = float(input("Enter grade: "))
        grades[student_name] = student_grade

    if choice == "2":
        for name, grade in grades.items():
            print(f"{name} : {grade}")

    if choice == "3":
        name = input("Enter the name: ")
        if name in grades:
            new_grade = float(input("Enter the grade: "))
            grades[name] = new_grade
        
        else:
            print("No such name exist! ")

    if choice == "4":
        name = input("Enter the name: ")
        if name in grades:
            print(f"Grade: ", grades[name])
        else:
            print("No such student exist ")

    if choice == "5":
        if not grades:
            print("No students available.")
        else: 
            average = sum(grades.values()) / len(grades)
            print(f"Average of all student: ", {average})

    elif choice == "6":
        print("Good bye ! ")
        break
