#Jayden Coulston
# Module_2_Lab_Case_Study.py
# This app accepts student names and GPAs and determines whether each student
# qualifies for the Dean's List or the Honor Roll.

while True:
    #Asks for students last name or zzz to stop the program
    last_name = input("Enter student's last name (or ZZZ to quit): ")

    #Checks if the user types ZZZ to end the program
    if last_name.upper() == "ZZZ":
        break

    #Asks user for their first name
    first_name = input("Enter student's first name: ")
    #Asks user for their gpa
    gpa = float(input("Enter student's GPA: "))

    #Checks if the user qualifies for the Deans's List
    if gpa >= 3.5:
        print(f"{first_name.title()} {last_name.title()} has made the Dean's List.")

    #Checks if the user qualifies for the Honor Roll
    if gpa >= 3.25:
        print(f"{first_name.title()} {last_name.title()} has made the Honor Roll.")

    #Checks if the user doesn't qualify for either
    else:
        print(f"{first_name.title()} {last_name.title()} has not made the Dean's List or Honor Roll.")
