codecount = 0
subjectcount = int(input("How many subjects have you had this semester? "))
component = {}

while codecount < subjectcount:
    codecount += 1

    print()
    print("INSTRUCTIONS")
    print("This code calculates the grades of each of your subjects, so please type in a subject at a time")
    subject = str(input("Subject: "))
    units = int(input("Units: "))

    print()
    print("Note: You may find your subject's components and their percentages in the syllabus of your prog")
    print("Subject components: ")
    print("a) Quizzes")
    print("b) Long tests")
    print("c) Home works")
    print("d) Seat works")
    print("e) Projects")
    print("f) midterm exam")
    print("g) final exam")
    print("h) Recitation")
    print("i) Others")
    component_count = int(input("How many components do you have for this subject? "))

    for a in range(0, component_count):
        print()
        print("Note: Type in each component one by one")
        subcomponents = input("Type the letter of one of the components of this subject ")

        if subcomponents.lower() == "a":
            print()
            print("You chose Quizzes as one of your components")
            quizzes = float(input("What percentage of your grade is this? "))
            quizzes *= 0.01
            component["Quizzes"] = quizzes

        elif subcomponents.lower() == "b":
            print()
            print("You chose Long tests as one of your components")
            lt = float(input("What percentage of your grade is this? "))
            lt *= 0.01
            component["Long tests"] = lt

        elif subcomponents.lower() == "c":
            print()
            print("You chose Homeworks as one of your components")
            hw = float(input("What percentage of your grade is this? "))
            hw *= 0.01
            component["Homeworks"] = hw

        elif subcomponents.lower() == "d":
            print()
            print("You chose Seatworks as one of your components")
            sw = float(input("What percentage of your grade is this? "))
            sw *= 0.01
            component["Seat works"] = sw

        elif subcomponents.lower() == "e":
            print()
            print("You chose projects as one of your components")
            proj = float(input("What percentage of your grade is this? "))
            proj *= 0.01
            component["Projects"] = proj

        elif subcomponents.lower() == "f":
            print()
            print("You chose Midterm exam as one of your components")
            mid = float(input("What percentage of your grade is this? "))
            mid *= 0.01
            component["Midterms"] = mid

        elif subcomponents.lower() == "g":
            print()
            print("You chose final exam as one of your components")
            finals = float(input("What percentage of your grade is this? "))
            finals *= 0.01
            component["Final exam"] = finals

        elif subcomponents.lower() == "h":
            print()
            print("You chose recitation as one of your components")
            recit = float(input("What percentage of your grade is this? "))
            recit *= 0.01
            component["Recitation"] = recit

        elif subcomponents.lower() == "i":
            print()
            print("You chose others as one of your components")
            others = str(input("What is this component called? "))
            others_grade = float(input("What percentage of your grade is this? "))
            others_grade *= 0.01
            component[others] = others_grade

    print()
    print("The components of your grade are as follows: " + str(component))
