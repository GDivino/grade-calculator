gradeequivalents = {"A": str(4), "B+": str(3.5), "B": str(3), "C+": str(2.5), "C": str(2), "D": str(1.5), "F": str(1)}
print(gradeequivalents)

QPI = 0
units = 0
sum2 = 0
units1 = 0
qpiequivalent = 0
leave = "n"

print("")
while leave.lower() == "n":
    grade = str(input("Grade: "))
    if grade.upper() == "A":
        qpiequivalent = 4
    elif grade.upper() == "B+":
        qpiequivalent = float(3.5)
    elif grade.upper() == "B":
        qpiequivalent = 3
    elif grade.upper() == "C+":
        qpiequivalent = float(2.5)
    elif grade.upper() == "C":
        qpiequivalent = 2
    elif grade.upper() == "D":
        qpiequivalent = float(1.5)
    elif grade.upper() == "F":
        qpiequivalent = 0
    else:
        print("Invalid input")
        break

    units = int(input("Units: "))
    if units == str:
        print("Invalid input")
        break
    else:
        sum1 = qpiequivalent * units
        units1 += units
        sum2 += sum1
        QPI = sum2 / units1
        print("QPI: " + str(QPI))
        print("")

    leave = input("are you done? ")
    if leave.upper() == "y":
        print("Final QPI: " + str(qpiequivalent))
    else:
        continue

print("Final qpi = " + str(QPI))